from . import views
from django.urls import path

from rest_framework import routers

from .viewsets import LotoMAchineViewSet

from .views import autologin

route = routers.SimpleRouter()
route.register('autologin', LotoMAchineViewSet)

urlpatterns = [
    path('autologin/', autologin)
]