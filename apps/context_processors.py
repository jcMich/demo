__author__ = 'root'
import django
from apps.home.models import userProfile

def user_image(request):
    try:
        image = None
        user = request.user
        up = userProfile.objects.get(user=user)
        image =  '/%s'%up.photo
    except:
        image = '/static/img/user.gif'
    return image



def my_processor(request):
    context ={
        'django_version':django.get_version(),
        'get_image_profile':user_image(request),
    }
    return context