from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse


class AutamaProfile(models.Model):
    autamaid = models.CharField(max_length=100, default="0")
    creator = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='Images', blank=True)
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    nummatches = models.CharField(max_length=100, default='0000000', editable=False)
    owner = models.CharField(max_length=100, default='FREE')
    pickle = models.CharField(max_length=100, default='PICKLE')
    interests = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, null=True, blank=True, default='')

    def __str__(self):
        return '{pk} {first} {last}'.format(pk=self.pk, first=self.first, last=self.last)

    def get_slug(self):
        slug = '{} {}'.format(self.first, self.last)
        return slugify(slug)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk, 'slug': self.get_slug()})

