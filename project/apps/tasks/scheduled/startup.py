from __future__ import absolute_import

import logging
from imdbpie import Imdb
from django.db import transaction
from core.models import *


def sync_db():
    imdb = Imdb(anonymize=True)  # to proxy requests

    imdb_ids = list(IMDB.objects.filter())
    for id in imdb_ids:
        try:
            with transaction.atomic():
                logging.getLogger('debug').debug("Processing... %s" % id.imdb_id)
                title = imdb.get_title_by_id('tt0468569').__dict__
                saved_title = Title.objects.filter(imdb_id=title['imdb_id'])
                if not saved_title.exists():
                    title_instance = Title.objects.create(imdb_id=title['imdb_id'], name=title['title'])
                    title_data = {
                        'name': title['title'],
                        'type': title['type'],
                        'year': title['year'],
                        'tagline': title['tagline'],
                        'plot_outline': title['plot_outline'],
                        'rating': title['rating'],
                        'votes': title['votes'],
                        'runtime': title['runtime'],
                        'poster_url': title['poster_url'],
                        'cover_url': title['cover_url'],
                        'release_date': title['release_date'],
                        'certification': title['certification']
                    }
                    Title.objects.filter(id=title_instance.id).update(**title_data)

                    for rank, person in enumerate(title['directors_summary']):
                        person = person.__dict__
                        saved_person = Person.objects.filter(imdb_id=person['imdb_id'])
                        if saved_person.exists():
                            person_instance = saved_person[0]
                        else:
                            person_instance = Person.objects.create(imdb_id=person['imdb_id'])
                            person_data = {'name': person['name'], 'job': person['job'], 'attr': person['attr'], 'photo_url': person['photo_url']}
                            Person.objects.filter(id=person_instance.id).update(**person_data)
                        credit = Credit.objects.create(person=person_instance, title=title_instance, rank=rank+1,
                                                       job='director')
                        for rank,role in enumerate(person['roles']):
                            Role.objects.create(credit=credit, rank=rank+1, name=role)

                    for rank, person in enumerate(title['cast_summary']):
                        person = person.__dict__
                        saved_person = Person.objects.filter(imdb_id=person['imdb_id'])
                        if saved_person.exists():
                            person_instance = saved_person[0]
                        else:
                            person_instance = Person.objects.create(imdb_id=person['imdb_id'])
                            person_data = {'name': person['name'], 'job': person['job'], 'attr': person['attr'], 'photo_url': person['photo_url']}
                            Person.objects.filter(id=person_instance.id).update(**person_data)
                        credit = Credit.objects.create(person=person_instance, title=title_instance, rank=rank+1,
                                                       job='principal_cast')
                        for rank,role in enumerate(person['roles']):
                            Role.objects.create(credit=credit, rank=rank+1, name=role)

                    for rank, person in enumerate(title['writers_summary']):
                        person = person.__dict__
                        saved_person = Person.objects.filter(imdb_id=person['imdb_id'])
                        if saved_person.exists():
                            person_instance = saved_person[0]
                        else:
                            person_instance = Person.objects.create(imdb_id=person['imdb_id'])
                            person_data = {'name': person['name'], 'job': person['job'], 'attr': person['attr'],
                                           'photo_url': person['photo_url']}
                            Person.objects.filter(id=person_instance.id).update(**person_data)
                        credit = Credit.objects.create(person=person_instance, title=title_instance, rank=rank+1,
                                                       job='writer')
                        for rank, role in enumerate(person['roles']):
                            Role.objects.create(credit=credit, rank=rank+1, name=role)

                    for rank, person in enumerate(title['credits']):
                        person = person.__dict__
                        saved_person = Person.objects.filter(imdb_id=person['imdb_id'])
                        if saved_person.exists():
                            person_instance = saved_person[0]
                        else:
                            person_instance = Person.objects.create(imdb_id=person['imdb_id'])
                            person_data = {'name': person['name'], 'job': person['job'], 'attr': person['attr'], 'photo_url': person['photo_url']}
                            Person.objects.filter(id=person_instance.id).update(**person_data)
                        credit, created = Credit.objects.get_or_create(person=person_instance, title=title_instance)
                        Credit.objects.filter(id=credit.id).update(rank=rank+1, job=person['token'])
                        for rank,role in enumerate(person['roles']):
                            Role.objects.create(credit=credit, rank=rank+1, name=role)

                    for rank, genre in enumerate(title['genres']):
                        Genre.objects.create(name=genre, title=title_instance, rank=rank+1)

                    for rank, trailer in enumerate(title['trailers']):
                        Trailer.objects.create(name=trailer['url'], title=title_instance, format=trailer['format'], rank=rank+1)

                    for rank, plot in enumerate(title['plots']):
                        Plot.objects.create(name=plot, title=title_instance, rank=rank+1)

                    for rank, trailer_image in enumerate(title['trailer_image_urls']):
                        TrailorImageUrl.objects.create(title=title_instance, name=trailer_image, rank=rank+1)

        except Exception as e:
            logging.getLogger('error').error(str(id)+str(e), exc_info=True)
