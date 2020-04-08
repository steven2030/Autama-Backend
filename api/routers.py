# router that allows optional trailing slash on endpoints
#  https://stackoverflow.com/questions/46163838/how-can-i-make-a-trailing-slash-optional-on-a-django-rest-framework-simplerouter

from rest_framework.routers import DefaultRouter


class OptionalSlashRouter(DefaultRouter):
    def __init__(self, *args, **kwargs):
        super(DefaultRouter, self).__init__(*args, **kwargs)
        self.trailing_slash = '/?'
