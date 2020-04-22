from django import forms 
from .models import post

class PostForm(forms.ModelForm):
    # tags = forms.CharField(widget=forms.TextInput(attrs={"data-role":"tagsinput"}))


    class Meta:
        model = post
        fields = "__all__"