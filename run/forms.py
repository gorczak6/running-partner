from django.forms import ModelForm

from run.models import UserLogin, Comment


class LoginForm(ModelForm):

    class Meta:
        model = UserLogin
        fields = ['username', 'password']


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['author', 'text']
