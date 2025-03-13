from django.urls import path
from . import views

urlpatterns =[
    path('' , views.ListOfCourse, name='ListOfCourse') ,
    path('addcourse',views.AddCourse , name='addcourse'),
    path('updatecourse/<int:id>' ,views.UpdateCourse , name='updatecourse'),
    path('deletecourse/<int:id>', views.UpdateCourse, name='updatecourse')
]