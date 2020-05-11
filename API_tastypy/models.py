from django.db import models
from tastypie.resources import ModelResource
from AutamaProfiles.models import AutamaProfile

# Create your models here.
class AutamaResource(ModelResource):
    class Meta:
        queryset = AutamaProfile.objects.all()
        resource_name = 'autamas'
