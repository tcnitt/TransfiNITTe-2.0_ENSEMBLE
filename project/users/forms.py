from django import forms

from .models import user

class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    class Meta:
        model = user
        fields = ('username','password','first_name','last_name','email','year','department','cgpa','github_link','linkedin_link','resume_link','transcript_link','areas_of_interest')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = 'Enter your roll no.'