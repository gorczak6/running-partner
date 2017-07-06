import datetime

from django.http.response import Http404
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import CreateView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from run.models import Training, Person, Comments
from run.serializers import TrainingSerializer, PersonSerializer


class TrainingsViewAPI(APIView):
    def get(self, request, format=None):
        trainings = Training.objects.all()
        serializer = TrainingSerializer(trainings, many=True, context={"request": request})
        return Response(data=serializer.data)


class TrainingViewAPI(APIView):

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


class PeopleViewAPI(APIView):
    def get(self, request, format=None):
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True, context={"request": request})
        return Response(serializer.data)


class PersonViewAPI(APIView):
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


class HomeView(View):
    def get(self, request):
        trainings = Training.objects.order_by('date', 'time').filter(date__gte=datetime.datetime.now())
        return render(request, "home.html", {"trainings": trainings})


class TrainingView(View):
    def get(self, request, training_id):
        training = Training.objects.get(pk=training_id)
        comments = Comments.objects.filter(pk=training_id)
        return render(request, "training-details.html", {"request": request,
                                                         "training": training,
                                                         "comments": comments})


class AddTrainingView(CreateView):
    model = Training
    fields = ['date', 'time', 'city', 'street', 'number', 'distance', 'pace', 'description', 'author']
    success_url = '/'
