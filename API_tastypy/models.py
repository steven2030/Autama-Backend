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
from accounts.models import Messages
from Nucleus.ham import Ham


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
        #fields = ['password'] # Seems like atleast one of the fields in the post must be mentioned here to have them included in post response.
        #always_return_data = True # Seems to need this get posted data returned in response.

    def obj_create(self, bundle, request=None, **kwargs):
        try:
            user = User.objects.create(username=bundle.data.get('username'))
            user.set_password(bundle.data.get('password'))
            user.save()
            apikey = bundle.data.get('apikey')
            user = User.objects.get(username=bundle.data.get('username'))
            apikey = ApiKey.objects.create(key=apikey, user=user)
            apikey.save()
            bundle.obj = user  # HAVE to update the bundle object to include its data in post response.
        except IntegrityError:
            raise BadRequest('That username already exists')
        return bundle

    ''' # can use this to make null fields sent that I don't want returned in the post response.
    def dehydrate(self, bundle):
        if bundle.request.method == 'POST':
            bundle.data['apikey'] = 'nope'
            bundle.data['password'] = 'also nope'

        return bundle
    '''

class MessagingAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        autama_id = int(bundle.request.headers.get('AutamaID'))
        autama = AutamaProfile.objects.get(pk=autama_id)
        user = bundle.request.user
        return object_list.filter(userID=user).filter(autamaID=autama)


class MessagingResource(ModelResource):
    class Meta:
        queryset = Messages.objects.all()
        resource_name = 'messages'
        authorization = MessagingAuthorization()
        authentication = BasicAuthentication()
        include_resource_uri = False
        fields = ['userID', 'autamaID', 'message', 'sender', 'timeStamp'] # Seems like atleast one of the fields in the post must be mentioned here to have them included in post response.
        always_return_data = True # Seems to need this get posted data returned in response.
        allowed_methods = ['post', 'get']

    def hydrate(self, bundle):
        user = User.objects.get(username=bundle.data.get("username"))
        autama = AutamaProfile.objects.get(pk=int(bundle.data.get("autamaID")))
        message = bundle.data.get("message")
        sender = bundle.data.get("sender")
        message = Messages.objects.create(userID=user, autamaID=autama, sender=sender, message=message)
        #message.save() # somewhere in the hydrate cycle tastypie calls save for us
        bundle.obj = message

        return bundle

    def dehydrate(self, bundle):
        # Include the request IP in the bundle.
        #bundle.data['request_ip'] = bundle.request.META.get('REMOTE_ADDR')
        return bundle




'''
    message = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True)
    userID = models.ForeignKey('User', on_delete=models.CASCADE)
    autamaID = models.ForeignKey('AutamaProfiles.AutamaProfile', on_delete=models.CASCADE)
    sender = models.CharField(max_length=6, choices=SENDER_CHOICES)
'''







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