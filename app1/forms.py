from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class CareerForm(forms.Form):
    full_name = forms.CharField(label="Full Name", max_length=100)
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    age = forms.IntegerField()
    ug_course = forms.ChoiceField(choices=[('BTech', 'B.Tech'), ('BSc', 'B.Sc'), ('BA', 'B.A')])
    ug_specialization = forms.CharField(label="UG Specialization")
    cgpa = forms.FloatField(min_value=0.0, max_value=10.0)
    interests = forms.CharField(help_text="Comma-separated, e.g., AI, Web")
    skills = forms.CharField(help_text="Comma-separated, e.g., Python, SQL")
    certifications = forms.CharField(help_text="Comma-separated, e.g., Coursera ML")
    working = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')])
    current_job = forms.CharField(label="Current Job Title (or NA)", required=False)
    masters = forms.CharField(label="Master's Degree Field (or NA)", required=False)











# app1/forms.py

from django import forms
from .models import ResumeInput

class ResumeInputForm(forms.ModelForm):
    class Meta:
        model = ResumeInput
        # Exclude generated_resume and generated_at as they are set by the system
        exclude = ['user', 'generated_resume', 'generated_at']
        widgets = {
            'summary': forms.Textarea(attrs={'rows': 4}),
            'education_details': forms.Textarea(attrs={'rows': 3}),
            'experience_details': forms.Textarea(attrs={'rows': 5}),
            'previous_experience': forms.Textarea(attrs={'rows': 5}),
            'skills': forms.TextInput(attrs={'placeholder': 'e.g., Python, JavaScript, SQL, Machine Learning'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'project_description': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Tailwind CSS classes to all form fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm p-2'




# your_app_name/forms.py
from django import forms
from .models import Profile # Import your Profile model

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar'] # Only include the avatar field for the upload form            