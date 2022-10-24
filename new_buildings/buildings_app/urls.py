from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('api/v1/buildings_list', views.BuildingsApiView.as_view(), name='buildings_list'),
    path('api/v1/buildings_list/<int:pk>', views.BuildingApi.as_view()),
]
