from django.urls import path
from . import views

urlpatterns =[
    path('' , views.ListOfTrainee , name='ListOfTrainee'),
    path('add', views.AddTrainee , name='AddTrainee'),
    path('update/<int:id>' , views.UpdateTrainee , name='UpdateTrainee'),
    path('delete/<int:id>' , views.DeleteTrainee , name='DeleteTrainee'),
    path('login' , views.login , name='Login'),
    path('register' , views.register , name='register')
]