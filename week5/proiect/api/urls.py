from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register('location', views.LocationViewSet)

urlpatterns = [
    path('',  include(router.urls))
]

"""
CRUD
C -> Create: POST
R -> Read: GET
U -> Update: PUT
D -> Delete: DESTROY
"""
