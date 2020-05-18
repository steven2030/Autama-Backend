from django.db import models
from tastypie.resources import ModelResource
from AutamaProfiles.models import AutamaProfile
from accounts.models import User
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication, BasicAuthentication
from tastypie.models import ApiKey
from django.urls import path
from django.conf.urls import url
from django.db import IntegrityError
from tastypie.exceptions import BadRequest


# Create your models here.
class AutamaResource(ModelResource):
    class Meta:
        queryset = AutamaProfile.objects.all()
        resource_name = 'autamas'
        fields = ['id', 'creator', 'first', 'last', 'interest1', 'interest2', 'interest3', 'interest4', 'interest5',
                  'interest6']


class AccountAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        return object_list.filter(id=bundle.request.user.id)


class AccountsResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'accounts'
        fields = ['id', 'username']
        filtering = {
            'username': ['exact']
        }

        #authorization = Authorization()
        authorization = AccountAuthorization()
        #authentication = ApiKeyAuthentication()
        authentication = BasicAuthentication()


class RegistrationResource(ModelResource):
    class Meta:
        resource_name = 'register'
        allowed_methods = ['post']
        object_class = User
        include_resource_uri = False

    def obj_create(self, bundle, request=None, **kwargs):
        try:
            user = User.objects.create(username=bundle.data.get('username'))
            user.set_password(bundle.data.get('password'))
            user.save()
            apikey = bundle.data.get('apikey')
            user = User.objects.get(username=bundle.data.get('username'))
            apikey = ApiKey.objects.create(key=apikey, user=user)
            apikey.save()
        except IntegrityError:
            raise BadRequest('That username already exists')
        return bundle





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