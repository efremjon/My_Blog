from tkinter import Widget
from django import forms
from .models import Post,Catagory


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_tag','author','catagory2','body')
        Widget = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'catagory2':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }


class UpdatePosForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_tag','body')
        Widget = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }


class PostFormNew(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_tag','author','catagory2','body')
        Widget = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'catagory2':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }