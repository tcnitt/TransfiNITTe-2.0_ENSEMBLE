from django import forms

from .models import user,professor

class UserForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ('username','password','first_name','last_name','email','year','department','cgpa','github_link','linkedin_link','resume_link','transcript_link','areas_of_interest')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = 'Enter your roll no.'


class ProfForm(forms.ModelForm):
    class Meta:
        model = professor
        fields = ('name','department','email','password','research_areas','google_scholar')