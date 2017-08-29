from __future__ import absolute_import, unicode_literals

from django.db import models
import util


class Title(models.Model):
    imdb_id = models.CharField(max_length=50, null=False, blank=False, unique=True, db_index=True)
    name = models.CharField(max_length=200, null=False, blank=False, db_index=True)
    type = models.CharField(max_length=50, null=False, blank=False)
    year = models.CharField(max_length=5, null=True, blank=True)
    tagline = models.TextField(max_length=200, null=True, blank=True)
    plot_outline = models.TextField(max_length=200, null=True, blank=True)
    rating = models.FloatField(default=0, null=False, blank=True)
    votes = models.BigIntegerField(default=0, null=False, blank=True)
    runtime = models.BigIntegerField(default=0, null=False, blank=True)
    poster_url = models.TextField(max_length=200, null=True, blank=True)
    cover_url = models.TextField(max_length=200, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    certification = models.CharField(max_length=5, null=True, blank=True)

    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Title"
        verbose_name_plural = "Title"
        ordering = ('name', 'created_at',)

    def __repr__(self):
        return '<Title: {0} - {1}>'.format(repr(self.name),
                                           repr(self.imdb_id))

    def __unicode__(self):
        return '<Title: {0} - {1}>'.format(self.name, self.imdb_id)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = util.current_time()
        self.updated_at = util.current_time()
        return super(Title, self).save(*args, **kwargs)


class Person(models.Model):
    imdb_id = models.CharField(max_length=200, null=False, blank=False, unique=True, db_index=True)
    name = models.CharField(max_length=200, null=False, blank=False, db_index=True)
    photo_url = models.TextField(max_length=500, null=True, blank=True)

    attr = models.TextField(max_length=500, null=True, blank=True)
    job = models.TextField(max_length=500, null=True, blank=True)

    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Person"
        ordering = ('name', 'created_at',)

    def __repr__(self):
        return '<Person: {0} - {1}>'.format(repr(self.imdb_id), repr(self.name))

    def __unicode__(self):
        return '<Person: {0} - {1}>'.format(repr(self.imdb_id), repr(self.name))

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = util.current_time()
        self.updated_at = util.current_time()
        return super(Person, self).save(*args, **kwargs)


class Genre(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True, db_index=True)
    title = models.ForeignKey('core.Title', related_name='genres', related_query_name='genre')

    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"
        ordering = ('name', 'created_at',)

    def __repr__(self):
        return '<Genre: {0} - {1}>'.format(repr(self.name), repr(self.title))

    def __unicode__(self):
        return '<Genre: {0} - {1}>'.format(repr(self.name), repr(self.title))

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = util.current_time()
        self.updated_at = util.current_time()
        return super(Genre, self).save(*args, **kwargs)


class Plot(models.Model):
    name = models.TextField(max_length=500, null=False, blank=False)
    title = models.ForeignKey('core.Title', related_name='plots', related_query_name='plot', db_index=True)

    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Plot"
        verbose_name_plural = "Plots"
        ordering = ('title', 'name', 'created_at',)

    def __repr__(self):
        return '<Plot: {0} - {1}>'.format(repr(self.name), repr(self.title))

    def __unicode__(self):
        return '<Plot: {0} - {1}>'.format(repr(self.name), repr(self.title))

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = util.current_time()
        self.updated_at = util.current_time()
        return super(Plot, self).save(*args, **kwargs)


class TrailorImageUrl(models.Model):
    name = models.TextField(max_length=500, null=False, blank=False)
    title = models.ForeignKey('core.Title', related_name='trailer_image_urls', related_query_name='trailer_image_url', db_index=True)

    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Trailor Image Url"
        verbose_name_plural = "Trailor Image Urls"
        ordering = ('title', 'name', 'created_at',)

    def __repr__(self):
        return '<TrailorImageUrl: {0} - {1}>'.format(repr(self.name), repr(self.title))

    def __unicode__(self):
        return '<TrailorImageUrl: {0} - {1}>'.format(repr(self.name), repr(self.title))

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = util.current_time()
        self.updated_at = util.current_time()
        return super(TrailorImageUrl, self).save(*args, **kwargs)


class Trailer(models.Model):
    name = models.TextField(max_length=500, null=False, blank=False)
    title = models.ForeignKey('core.Title', related_name='trailers', related_query_name='trailer', db_index=True)

    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Trailer"
        verbose_name_plural = "Trailers"
        ordering = ('title', 'name', 'created_at',)

    def __repr__(self):
        return '<Trailer: {0} - {1}>'.format(repr(self.name), repr(self.title))

    def __unicode__(self):
        return '<Trailer: {0} - {1}>'.format(repr(self.name), repr(self.title))

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = util.current_time()
        self.updated_at = util.current_time()
        return super(Trailer, self).save(*args, **kwargs)


class TitleImage(models.Model):
    url = models.TextField(max_length=500, null=False, blank=False)
    caption = models.TextField(max_length=500, null=True, blank=True)

    title = models.ForeignKey('core.Title', related_name='images', related_query_name='image', db_index=True)

    width = models.FloatField(default=0, null=True, blank=True)
    height = models.FloatField(default=0, null=True, blank=True)

    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Title Image"
        verbose_name_plural = "Title Images"
        ordering = ('caption', 'created_at',)

    def __repr__(self):
        return '<TitleImage: {0}>'.format(repr(self.caption))

    def __unicode__(self):
        return '<TitleImage: {0}>'.format(self.caption.encode('utf-8'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = util.current_time()
        self.updated_at = util.current_time()
        return super(TitleImage, self).save(*args, **kwargs)


class PersonImage(models.Model):
    url = models.TextField(max_length=500, null=False, blank=False)
    caption = models.TextField(max_length=500, null=True, blank=True)

    person = models.ForeignKey('core.Person', related_name='images', related_query_name='image', db_index=True)

    width = models.FloatField(default=0, null=True, blank=True)
    height = models.FloatField(default=0, null=True, blank=True)

    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Person Image"
        verbose_name_plural = "Person Images"
        ordering = ('caption', 'created_at',)

    def __repr__(self):
        return '<PersonImage: {0}>'.format(repr(self.caption))

    def __unicode__(self):
        return '<PersonImage: {0}>'.format(self.caption.encode('utf-8'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = util.current_time()
        self.updated_at = util.current_time()
        return super(PersonImage, self).save(*args, **kwargs)


class TitlePerson(models.Model):
    title = models.ForeignKey('core.Title', related_query_name='cast', related_name='casts', db_index=True)
    person = models.ForeignKey('core.Person', related_query_name='work', related_name='works')

    job = models.CharField(max_length=100, blank=False, null=False)

    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Title Person"
        verbose_name_plural = "Title Persons"
        ordering = ('title', 'person', 'created_at',)

    def __repr__(self):
        return '<TitlePerson: {0} - {1}>'.format(repr(self.title), repr(self.person))

    def __unicode__(self):
        return '<TitlePerson: {0} - {1}>'.format(repr(self.title), repr(self.person))

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = util.current_time()
        self.updated_at = util.current_time()
        return super(TitlePerson, self).save(*args, **kwargs)


class Episode(models.Model):
    imdb_id = models.CharField(max_length=200, null=False, blank=False, unique=True, db_index=True)
    serial = models.ForeignKey('core.Title', related_name='episodes', related_query_name='episode', db_index=True)
    release_date = models.DateField(null=True, blank=True)
    type = models.CharField(max_length=200, null=True, blank=True)
    year = models.CharField(max_length=5, null=True, blank=True)
    season = models.FloatField(null=False, blank=False)
    episode = models.FloatField(null=False, blank=False)

    title = models.CharField(max_length=200, null=False, blank=False, db_index=True)

    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Episode"
        verbose_name_plural = "Episodes"
        ordering = ('serial', 'title', 'created_at',)

    def __repr__(self):
        return '<Episode: {0} - {1}>'.format(repr(self.title), repr(self.serial))

    def __unicode__(self):
        return '<Episode: {0} - {1}>'.format(repr(self.title), repr(self.serial))

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = util.current_time()
        self.updated_at = util.current_time()
        return super(Episode, self).save(*args, **kwargs)


class Review(models.Model):
    username = models.CharField(max_length=200, null=False, blank=False, db_index=True)
    text = models.TextField(max_length=1000, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    rating = models.FloatField(null=False, blank=False)
    summary = models.TextField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=100, null=False, blank=False)
    user_location = models.CharField(max_length=100, null=False, blank=False)
    user_score = models.FloatField(default=0, null=True, blank=True)
    user_score_count = models.FloatField(default=0, null=True, blank=True)

    title = models.CharField(max_length=200, null=False, blank=False, db_index=True)

    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ('title', 'rating', 'created_at',)

    def __repr__(self):
        return '<Review: {0}, {1}>'.format(str(self.rating), repr(self.text[:20]))

    def __unicode__(self):
        return '<Review: {0}, {1}>'.format(str(self.rating), self.text[:20].encode('utf-8'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = util.current_time()
        self.updated_at = util.current_time()
        return super(Review, self).save(*args, **kwargs)