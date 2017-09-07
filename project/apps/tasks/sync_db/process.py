from __future__ import absolute_import

import logging
from django.db import transaction
from core.models import *


def run(title):
    try:
        with transaction.atomic():
            logging.getLogger('debug').debug("Processing... %s - %s" % (title['title'], str(title['imdb_id'])))
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

                if 'directors_summary' in title and title['directors_summary']:
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

                if 'cast_summary' in title and title['cast_summary']:
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

                if 'writers_summary' in title and title['writers_summary']:
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

                if 'genres' in title and title['genres']:
                    for rank, genre in enumerate(title['genres']):
                        Genre.objects.create(name=genre, title=title_instance, rank=rank+1)

                if 'trailers' in title and title['trailers']:
                    for rank, trailer in enumerate(title['trailers']):
                        Trailer.objects.create(name=trailer['url'], title=title_instance, format=trailer['format'], rank=rank+1)

                if 'trailer_image_urls' in title and title['trailer_image_urls']:
                    for rank, trailer_image in enumerate(title['trailer_image_urls']):
                        TrailorImageUrl.objects.create(title=title_instance, name=trailer_image, rank=rank+1)

    except Exception as e:
        logging.getLogger('error').error(str(id)+str(e), exc_info=True)
