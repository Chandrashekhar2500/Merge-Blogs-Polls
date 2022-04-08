from django import forms
from .models import Comments, Post , User , Category 
from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author','title', 'text', 'thumbnailImage', 'featureImage','category','tag')

class User_Signup(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','mobile_number','mail','company','designation','state','country','about','image')

class AuthenticationForm(forms.Form):
    class Meta:
        model = User
        fields = ('mail','password')

class User_Category(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ('name','description')


class User_Update(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('username','mobile_number','mail','company','designation','state','country','about','image')


class Insert_Comment(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('mail','comment')
