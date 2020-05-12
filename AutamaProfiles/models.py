from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse


class AutamaGeneral(models.Model):
    currentCount = models.IntegerField()
    totalCount = models.IntegerField()

    def __str__(self):
        return '{currentCount} {totalCount}'.format(currentCount=self.currentCount, totalCount=self.totalCount)


class AutamaProfile(models.Model):
    creator = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='Images', blank=False)
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    nummatches = models.IntegerField(default=0, editable=False)
    owner = models.CharField(max_length=100, default='FREE')
    pickle = models.CharField(max_length=100, default='PICKLE')
    interest1 = models.CharField(max_length=100)
    interest2 = models.CharField(max_length=100)
    interest3 = models.CharField(max_length=100)
    interest4 = models.CharField(max_length=100)
    interest5 = models.CharField(max_length=100)
    interest6 = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, null=True, blank=True, default='')
    report_count = models.IntegerField(default=0)

    def __str__(self):
        return '{pk} {first} {last}'.format(pk=self.pk, first=self.first, last=self.last)

    def get_slug(self):
        slug = '{} {}'.format(self.first, self.last)
        return slugify(slug)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk, 'slug': self.get_slug()})

