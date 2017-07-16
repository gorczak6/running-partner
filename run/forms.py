from django.forms import ModelForm, forms, CharField

from run.models import UserLogin


class LoginForm(ModelForm):

    class Meta:
        model = UserLogin
        fields = ['username', 'password']


class AddCommentForm(forms.Form):
    content = CharField(label='komentarz')
