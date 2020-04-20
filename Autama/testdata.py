from accounts.models import User, Claims, Messages, Matches
from AutamaProfiles.models import AutamaProfile
from django.http import HttpResponse


def add_test_data():
    user = User()
    user.username = "testuser2000"
    user.first_name = "test"
    user.last_name = "user"
    user.email = "test@user.com"
    user.sex = 2
    user.interests1 = "Int1"
    user.interests2 = "Int2"
    user.interests3 = "Int3"
    user.interests4 = "Int4"
    user.interests5 = "Int5"
    user.interests6 = "Int6"
    user.set_password('testuser')
    user.save()

    ai_prof = AutamaProfile()
    ai_prof.creator = 'Bob'
    ai_prof.picture = ''
    ai_prof.first = 'Bob'
    ai_prof.last = 'TheBuilder'
    ai_prof.nummatches = 0
    ai_prof.owner = 'FREE'
    ai_prof.pickle = 'PICKLE'
    ai_prof.interest1 = 'Building'
    ai_prof.interest2 = 'Architecture'
    ai_prof.interest3 = 'Interest3'
    ai_prof.interest4 = 'Interest4'
    ai_prof.interest5 = 'Interest5'
    ai_prof.interest6 = 'Interest6'
    ai_prof.save()

    ai_prof.creator = "Malefcient"
    ai_prof.first = "Cinderella"
    ai_prof.last = "Princess"
    ai_prof.interest1 = "Fairy God Mothers"
    ai_prof.interest2 = "Pumpkins"
    ai_prof.save()

    ai_prof.creator = 'Mufasa'
    ai_prof.first = 'Simba'
    ai_prof.last = 'Lion'
    ai_prof.interest1 = 'Pride Rock'
    ai_prof.interest2 = 'Playing'
    ai_prof.save()

    return HttpResponse('Test Data Added')