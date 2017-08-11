import datetime

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views import View
from django.views.generic import CreateView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from run.forms import CommentForm
from run.models import Training, Person, Comment
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


class TrainingView(LoginRequiredMixin, View):
    template_name = 'templates/registration/login.html'

    def get(self, request, training_id):
        training = Training.objects.get(pk=training_id)
        return render(request, "training-details.html", {"request": request,
                                                         "training": training,
                                                         "training_id": training_id})


class AddTrainingView(CreateView):
    model = Training
    fields = ['date', 'time', 'city', 'street', 'number', 'distance', 'pace', 'description', 'author']
    success_url = '/'


# class AddCommentView(View):
#     def get(self, request, training_id):
#         form = AddCommentForm
#         training = Training.objects.get(pk=training_id)
#         ctx = {"training": training,
#                "training_id": training_id,
#                "form": form}
#         return render(request, "add_comment.html", ctx)
#
#     def post(self, request, training_id):
#         form = AddCommentForm(request.POST)
#         if form.is_valid():
#             content = form.cleaned_data['content']
#             # author = request.user.username
#             result = Comments.objects.create(content=content,
#                                              author=request.user,
#                                              training_id=training_id)
#
#             ctx = {"form": form,
#                    "result": result,
#                    "training_id": training_id
#                    }
#         return redirect(request, 'training-details', ctx)
#         # return render(request, "training-details.html", ctx)

def add_comment_to_training(request, training_id):
    training = get_object_or_404(Training, pk=training_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.training = training
            comment.save()
            return redirect('training-details', training_id=training_id)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_training.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
