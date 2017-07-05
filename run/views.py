from django.http.response import Http404
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import CreateView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from run.models import Training, Person
from run.serializers import TrainingSerializer, PersonSerializer


class TrainingsView(APIView):
    def get(self, request, format=None):
        trainings = Training.objects.all()
        serializer = TrainingSerializer(trainings, many=True, context={"request": request})
        return Response(data=serializer.data)


class TrainingView(APIView):

        def get_object(self, pk):
            try:
                return Training.objects.get(pk=pk)
            except Training.DoesNotExist:
                raise Http404

        def get(self, request, pk, format=None):
            training = self.get_object(pk)
            serializer = TrainingSerializer(training, context={"request": request})
            return Response(serializer.data)

        def delete(self, request, pk, format=None):
            training = self.get_object(pk)
            training.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        def put(self, request, pk, format=None):
            training = self.get_object(pk)
            serializer = TrainingSerializer(training, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def post(self, request, format=None):
            serializer = TrainingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PeopleView(APIView):
    def get(self, request, format=None):
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True, context={"request": request})
        return Response(serializer.data)


class PersonView(APIView):
    def get_object(self, pk):
        try:
            return Person.objects.get(pk=pk)
        except Training.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        person = self.get_object(pk)
        serializer = PersonSerializer(person, context={"request": request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class AddTrainingView(CreateView):
#     model = Training
#     exclude = ['added_date', 'author']
#     success_url = '/'

class HomeView(View):
    def get(self, request):
        trainings = Training.objects.all()
        return render(request, "base.html", {"request": request})