from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse
from Nucleus.pancake import Pancake


# A function to create a new Autama profile. origin is the username of the user the Autama was based off
def create_new_autama(personality: list, creator: str = "Happy Slackers", origin: str = "Happy Slackers"):
    pancake = Pancake()  # For handling name generating
    REQUIRED = 6  # The required amount of traits
    amount = len(personality)

    # Make sure personality has the required amount of traits
    if amount == REQUIRED:
        picture = "Images/a1.png"
        first = pancake.generate_male_name()
        last = "last name"
        interest1 = personality[0]
        interest2 = personality[1]
        interest3 = personality[2]
        interest4 = personality[3]
        interest5 = personality[4]
        interest6 = personality[5]

        hybrid_autama = AutamaProfile.objects.create(creator=creator, picture=picture, first=first, last=last,
                                                     pickle=origin,
                                                     interest1=interest1, interest2=interest2,
                                                     interest3=interest3, interest4=interest4,
                                                     interest5=interest5, interest6=interest6)
        hybrid_autama.save()


class AutamaProfile(models.Model):
    creator = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='Images', blank=False)
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    nummatches = models.CharField(max_length=100, default='0000000', editable=False)
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

