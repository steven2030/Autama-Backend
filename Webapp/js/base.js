
// from django.contrib.auth.backends import ModelBackend
// from api.views import *
//
//
//
// class CustomBackend(ModelBackend):
//
//     def authenticate(self, request, username=None, password=None, **kwargs):
//         try:
//             username = request.POST.get("username", "")
//             password = request.POST.get("password", "")
//             user = UserInfo.objects.get(Q(username=username) | Q(email=username))
//             if user.check_password(password):
//                 return user
//         except Exception as e:
//             return None
//
// class LoginRequiredMixin(object):
//     """
//     """
//     @classmethod
//     def as_view(cls, **initkwargs):
//         view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
//         return login_required(view, login_url='/login/')
//
