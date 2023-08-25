from django.shortcuts import render
from django.contrib.auth.models import User
from avatar.models import Avatar


# Create your views here.
def home_admin(request):
    user = request.user
    try :
        avatar = Avatar.objects.get(pk = user.pk)
    except Avatar.DoesNotExist:
        avatar = None
    print(avatar)
    context = {
        'user' : user,
        'avatar' : avatar
    }
    return render(request, 'admin_safari/home.html', context)