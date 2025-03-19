from django.urls import path
from .views import ListTraineesAPI, AddTraineeAPI, UpdateTraineeAPI, DeleteTraineeAPI

urlpatterns = [
    path('trainees/', ListTraineesAPI.as_view(), name='list_trainees_api'),
    path('trainees/add/', AddTraineeAPI.as_view(), name='add_trainee_api'),
    path('trainees/update/<int:id>/', UpdateTraineeAPI.as_view(), name='update_trainee_api'),
    path('trainees/delete/<int:id>/', DeleteTraineeAPI.as_view(), name='delete_trainee_api'),
]
