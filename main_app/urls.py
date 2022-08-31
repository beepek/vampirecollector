from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bats/', views.bats_index, name='index'),
    #localhost:8000/bats/9
    path('bats/<int:bat_id>/', views.bats_detail, name="detail"),
    #
    path('bats/create/', views.BatCreate.as_view(), name='bats_create'),
    # pk is what the django views is expecting as a param if we need one, which is short for primary key
   
    path('bats/<int:pk>/update/', views.BatUpdate.as_view(), name='bats_update'),
    path('bats/<int:pk>/delete/', views.BatDelete.as_view(), name='bats_delete'),
        path('bats/<int:bat_id>/add_feeding/',######################
         views.add_feeding, name='add_feeding'),
    path('bats/<int:bat_id>/assoc_victim/<int:victim_id>/', views.assoc_victim, name='assoc_victim'),
    path('victims/', views.VictimList.as_view(), name='victims_index'),
    path('victims/<int:pk>/', views.VictimDetail.as_view(), name='victims_detail'),
    path('victims/create/', views.VictimCreate.as_view(), name='victims_create'),
    path('victims/<int:pk>/update/', views.VictimUpdate.as_view(), name='victims_update'),
    path('victims/<int:pk>/delete/', views.VictimDelete.as_view(), name='victims_delete'),
]