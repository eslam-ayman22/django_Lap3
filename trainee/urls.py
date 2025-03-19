from django.urls import path ,include
from . import views
from .views import ListTraineeView ,AddTraineeView ,UpdateTrainee
urlpatterns =[
    path('', ListTraineeView.as_view(), name="trainee_list"),
    path("trainees/add/", AddTraineeView.as_view(), name="add_trainee"),
    path('update/<int:trainee_id>/', UpdateTrainee.as_view(), name='UpdateTrainee'),
    path('delete/<int:trainee_id>' , views.DeleteTrainee , name='DeleteTrainee'),

    path('api/', include('trainee.api.urls')),

]