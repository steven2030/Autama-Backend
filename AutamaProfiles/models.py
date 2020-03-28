from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.


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
        return self.autamaid


def prepare_for_save(sender, **kwargs):
    instance = kwargs['instance']
    new_slug = '{first} {last} {pk}'.format(first=instance.first, last=instance.last, pk=instance.pk)
    instance.slug = slugify(new_slug)

    instance.auamaid = '{letter}{pk}'.format(letter='a', pk=instance.pk)


pre_save.connect(prepare_for_save, sender=AutamaProfile)
