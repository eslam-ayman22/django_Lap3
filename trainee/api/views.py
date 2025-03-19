from rest_framework import generics

from .serializers import TraineeSerializer
from trainee.models import Trainee


class ListTraineesAPI(generics.ListAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer


class AddTraineeAPI(generics.CreateAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer


class UpdateTraineeAPI(generics.UpdateAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer
    lookup_field = 'id'


class DeleteTraineeAPI(generics.DestroyAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer
    lookup_field = 'id'