from accounts.models import User, Claims, Messages, Matches
from AutamaProfiles.models import AutamaProfile, AutamaGeneral
from django.http import HttpResponse


def add_test_data():
    gen = AutamaGeneral()
    gen.currentCount = 1
    gen.totalCount = 100
    gen.save()

    user = User()
    user.username = "testuser"
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
    user.currentAutama = 1
    user.save()

    ai_prof = AutamaProfile()
    ai_prof.creator = 'Bob'
    ai_prof.picture = 'a1.png'
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

    ai_prof2 = AutamaProfile()
    ai_prof2.creator = "Malefcient"
    ai_prof2.picture = 'a2.png'
    ai_prof2.first = "Cinderella"
    ai_prof2.last = "Princess"
    ai_prof2.nummatches = 0
    ai_prof2.owner = 'FREE'
    ai_prof2.pickle = 'PICKLE'
    ai_prof2.interest1 = "Fairy God Mothers"
    ai_prof2.interest2 = "Pumpkins"
    ai_prof2.interest3 = 'Interest3'
    ai_prof2.interest4 = 'Interest4'
    ai_prof2.interest5 = 'Interest5'
    ai_prof2.interest6 = 'Interest6'
    ai_prof2.save()

    ai_prof3 = AutamaProfile()
    ai_prof3.creator = 'Mufasa'
    ai_prof3.picture = 'a3.png'
    ai_prof3.first = 'Simba'
    ai_prof3.last = 'Lion'
    ai_prof3.nummatches = 0
    ai_prof3.owner = 'FREE'
    ai_prof3.pickle = 'PICKLE'
    ai_prof3.interest1 = 'Pride Rock'
    ai_prof3.interest2 = 'Playing'
    ai_prof3.interest3 = 'Interest3'
    ai_prof3.interest4 = 'Interest4'
    ai_prof3.interest5 = 'Interest5'
    ai_prof3.interest6 = 'Interest6'
    ai_prof3.save()

    ai_prof4 = AutamaProfile()
    ai_prof4.creator = 'Disney'
    ai_prof4.picture = 'a4.png'
    ai_prof4.first = 'Benny'
    ai_prof4.last = 'TheCab'
    ai_prof4.nummatches = 0
    ai_prof4.owner = 'FREE'
    ai_prof4.pickle = 'PICKLE'
    ai_prof4.interest1 = 'Yellow'
    ai_prof4.interest2 = 'Cabs'
    ai_prof4.interest3 = 'Interest3'
    ai_prof4.interest4 = 'Interest4'
    ai_prof4.interest5 = 'Interest5'
    ai_prof4.interest6 = 'Interest6'
    ai_prof4.save()

    ai_prof5 = AutamaProfile()
    ai_prof5.creator = 'Disney'
    ai_prof5.picture = 'a5.png'
    ai_prof5.first = 'Ariel'
    ai_prof5.last = 'Mermaid'
    ai_prof5.nummatches = 0
    ai_prof5.owner = 'FREE'
    ai_prof5.pickle = 'PICKLE'
    ai_prof5.interest1 = 'Marine Science'
    ai_prof5.interest2 = 'Singing'
    ai_prof5.interest3 = 'Interest3'
    ai_prof5.interest4 = 'Interest4'
    ai_prof5.interest5 = 'Interest5'
    ai_prof5.interest6 = 'Interest6'
    ai_prof5.save()

    ai_prof6 = AutamaProfile()
    ai_prof6.creator = 'Disney'
    ai_prof6.picture = 'a6.png'
    ai_prof6.first = 'Ursula'
    ai_prof6.last = 'Octopus'
    ai_prof6.nummatches = 0
    ai_prof6.owner = 'FREE'
    ai_prof6.pickle = 'PICKLE'
    ai_prof6.interest1 = 'Magic'
    ai_prof6.interest2 = 'Being Evil'
    ai_prof6.interest3 = 'Interest3'
    ai_prof6.interest4 = 'Interest4'
    ai_prof6.interest5 = 'Interest5'
    ai_prof6.interest6 = 'Interest6'
    ai_prof6.save()

    ai_prof7 = AutamaProfile()
    ai_prof7.creator = 'Disney'
    ai_prof7.picture = 'a7.png'
    ai_prof7.first = 'Louis'
    ai_prof7.last = 'Chef'
    ai_prof7.nummatches = 0
    ai_prof7.owner = 'FREE'
    ai_prof7.pickle = 'PICKLE'
    ai_prof7.interest1 = 'Cooking'
    ai_prof7.interest2 = 'Crabs'
    ai_prof7.interest3 = 'Sebastion'
    ai_prof7.interest4 = 'Interest4'
    ai_prof7.interest5 = 'Interest5'
    ai_prof7.interest6 = 'Interest6'
    ai_prof7.save()

    ai_prof8 = AutamaProfile()
    ai_prof8.creator = 'Disney'
    ai_prof8.picture = 'a8.png'
    ai_prof8.first = 'LeFou'
    ai_prof8.last = ''
    ai_prof8.nummatches = 0
    ai_prof8.owner = 'FREE'
    ai_prof8.pickle = 'PICKLE'
    ai_prof8.interest1 = 'Gaston'
    ai_prof8.interest2 = 'Gaston'
    ai_prof8.interest3 = 'Gaston'
    ai_prof8.interest4 = 'Gaston'
    ai_prof8.interest5 = 'Gaston'
    ai_prof8.interest6 = 'Gaston'
    ai_prof8.save()

    return HttpResponse('Test Data Added')