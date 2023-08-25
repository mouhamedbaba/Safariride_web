from django.urls import include, path

from admin_safari.views import home_admin

urlpatterns = [
    path('', home_admin ),
]