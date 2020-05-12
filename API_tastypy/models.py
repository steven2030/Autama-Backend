from django.db import models
from tastypie.resources import ModelResource
from AutamaProfiles.models import AutamaProfile
from accounts.models import User
from tastypie.authorization import Authorization


# Create your models here.
class AutamaResource(ModelResource):
    class Meta:
        queryset = AutamaProfile.objects.all()
        resource_name = 'autamas'
        fields = ['id', 'creator', 'first', 'last', 'interest1', 'interest2', 'interest3', 'interest4', 'interest5',
                  'interest6']

class AccountsResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'accounts'
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'interest1', 'interest2', 'interest3',
                  'interest4', 'interest5', 'interest6']
        authorization = Authorization()



'''

(<django.db.models.fields.AutoField: id>,
 <django.db.models.fields.CharField: password>,
 <django.db.models.fields.DateTimeField: last_login>,
 <django.db.models.fields.BooleanField: is_superuser>,
 <django.db.models.fields.CharField: username>,
 <django.db.models.fields.CharField: first_name>,
 <django.db.models.fields.CharField: last_name>,
 <django.db.models.fields.EmailField: email>,
 <django.db.models.fields.BooleanField: is_staff>,
 <django.db.models.fields.BooleanField: is_active>,
 <django.db.models.fields.DateTimeField: date_joined>,
 <django.db.models.fields.IntegerField: sex>,
 <django.db.models.fields.files.ImageField: image>,
 <django.db.models.fields.TextField: interests1>,
 <django.db.models.fields.TextField: interests2>,
 <django.db.models.fields.TextField: interests3>,
 <django.db.models.fields.TextField: interests4>,
 <django.db.models.fields.TextField: interests5>,
 <django.db.models.fields.TextField: interests6>,
 <django.db.models.fields.IntegerField: currentAutama>)


'''