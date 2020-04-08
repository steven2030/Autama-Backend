from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse


# user model info
# would it be useful for the user model to have a numMatches trait?
class User(AbstractUser):
    gender = models.IntegerField(verbose_name="gender",
                                 choices=((0, 'Rather Not Say'), (1, 'Male'), (2, 'Female'),
                                          (3, 'Non-Conforming'), (4, 'Other')), default=0)
    image = models.ImageField(max_length=1000, upload_to='avatar', verbose_name=u'picture', null=True, blank=True)
    interest1 = models.TextField()
    interest2 = models.TextField()
    interest3 = models.TextField()
    interest4 = models.TextField()
    interest5 = models.TextField()
    interest6 = models.TextField()
    # what about email? password?

    # Overrides method in AbstractBaseUser
    def __str__(self):
        return '{id} {username} {first} {last}'.format(id=self.id, username=self.username,
                                                       first=self.first_name, last=self.last_name)


# autama model info
class AutamaProfile(models.Model):
    autamaID = models.CharField(max_length=100, default="0")
    creator = models.CharField(max_length=100, default='Team Autama OGs')
    picture = models.ImageField(upload_to='Images', blank=True)
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    num_matches = models.CharField(max_length=100, default='0000000', editable=False)
    # TODO: change owner to User.ForeignKey ?
    owner = models.CharField(max_length=100, default='Team Autama OGs')
    pickle = models.CharField(max_length=100, default='PICKLE')  # do we still need this?
    interest1 = models.CharField(max_length=100)
    interest2 = models.CharField(max_length=100)
    interest3 = models.CharField(max_length=100)
    interest4 = models.CharField(max_length=100)
    interest5 = models.CharField(max_length=100)
    interest6 = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, null=True, blank=True, default='')

    # overrides method in Model
    # def __str__(self):
    #     return '{pk} {first} {last}'.format(pk=self.pk, first=self.first, last=self.last)

    def get_slug(self):
        slug = '{} {}'.format(self.first, self.last)
        return slugify(slug)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk, 'slug': self.get_slug()})


# user-autama matches model
# needs to return a list of autamaIDs the user is matched with -- one-to-many ret
class Matches(models.Model):
    matchID = models.IntegerField(primary_key=True, default=None)
    userID = models.ForeignKey(User, on_delete=models.CASCADE,)
    autamaID = models.ForeignKey(AutamaProfile, on_delete=models.CASCADE,)
    # matchID = models.IntegerField(primary_key=True)  # pk
    # userID = models.ForeignKey('User', on_delete=CASCADE)
    # autamaID = models.ForeignKey('AutamaProfile', on_delete=CASCADE)

    # overrides method in model
    #def __str__(self):
    #    return '{userID} {autamaID}'.format(userID=self.userID, autamaID=self.autamaID)


# messages for specific conversations bot-to-user
class Messages(models.Model):
    # Constants used for enum in sender
    USER = 'User'
    AUTAMA = 'Autama'
    SENDER_CHOICES = [
        (USER, 'User'),
        (AUTAMA, 'Autama'),
    ]

    matchID = models.ForeignKey('Matches', on_delete=models.CASCADE)
    userID = models.ForeignKey('User', on_delete=models.CASCADE)  # del later?
    autamaID = models.ForeignKey('AutamaProfile', on_delete=models.CASCADE)  # del later?
    timeStamp = models.DateTimeField(auto_now_add=True)
    sender = models.CharField(max_length=6, choices=SENDER_CHOICES)
    messageTxt = models.TextField()

    # overrides method in model
    #def __str__(self):
    #    return '{sender} {timeStamp} {messageTxt}'.format(sender=self.sender,
    #                                                      timeStamp=self.timeStamp, messageTxt=self.messageTxt)

