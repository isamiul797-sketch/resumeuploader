from django import forms 
from app.models import Resume

GENDER_CHOICES = [
 ('Male', 'Male'),
 ('Female', 'Female')
]

JOB_CITY_CHOICES = (
    ('Dhaka', 'Dhaka'),
    ('Chattogram', 'Chattogram'),
    ('Khulna', 'Khulna'),
    ('Rajshahi', 'Rajshahi'),
    ('Sylhet', 'Sylhet'),
)

class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(choices=JOB_CITY_CHOICES,label='Preferred Job Locations', widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Resume
        fields = ['id','name','dob','gender','locality','city','pin','state','mobile','email','job_city','profile_image','my_file']

        labels = {'name':'Full Name','dob':'Date Of Birth','locality':'Locality','city':'City','pin':'Pin No.','state':'State','mobile':'Mobile No.','email':'Email Address','job_city':'Job City','profile_image':'Profile Photo','my_file':'Documents'}

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }