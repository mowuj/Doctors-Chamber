from .models import *
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control bg-light badge-pill p-2 m-2', 'type': 'password', 'name': 'password', 'placeholder': 'Enter Password'}),
        label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control bg-light badge-pill p-2 m-2', 'type': 'password', 'name': 'password', 'placeholder': 'Confirm Password'}),
        label='Password')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                               'placeholder': 'UserName..', 'label': 'Department Name'}),

        }


class RelatedImagesForm(forms.ModelForm):
    class Meta:
        model = RelatedImages
        fields = '__all__'
        exclude = ['user', 'id']
        widgets = {
            'caption': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                           'placeholder': 'Add Description'}),
            "photo": forms.ClearableFileInput(attrs={"class": "form-control"})
        }
class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = '__all__'
        exclude = ['user', 'id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                           'placeholder': 'Enter Announcement'}),
            
        }

class LabAddForm(forms.ModelForm):
    class Meta:
        model=Lab
        fields='__all__'
        widgets={
        'name': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                       'placeholder': 'Enter Lab Name'}),
            'manager': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                       'placeholder': 'Enter Lab Manager'}),
            'address': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                       'placeholder': 'Enter Lab Address'}),
            
        "photo": forms.ClearableFileInput(attrs={"class": "form-control"
        })
        }

class DepartmentAddForm(forms.ModelForm):
    class Meta:
        model=Department
        fields='__all__'
        widgets={
        'name': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                       'placeholder': 'Enter Department Name'}),
            'manager': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                       'placeholder': 'Enter Department Manager'}),
            'start_date': forms.DateInput(format=('%d/%m/%y'), attrs={'class': 'form-control bg-light badge-pill p-2', 'type': 'date'}),
        "photo": forms.ClearableFileInput(attrs={"class": "form-control"
        })
        }
class DoctorAddForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields='__all__'
        exclude=['user','id']
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                        'placeholder': 'Enter Doctor Name'}),
            'doctor_id': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                        'placeholder': 'Enter Doctor Id'}),
            'title': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                        'placeholder': 'Enter Doctor Title'}),
            'email': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                        'placeholder': 'Enter Doctor Email'}),
            'nid': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                        'placeholder': 'Enter Doctor"s NID'}),
            'phone': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                        'placeholder': 'Enter Doctor"s Phone'}),
            'gender': forms.Select(attrs={'class': 'form-control bg-light badge-pill p-2',
                                            'placeholder': 'Enter Doctor Gender'}),
            'department': forms.Select(attrs={'class': 'form-control bg-light badge-pill p-2',
                                            'placeholder': 'Enter Doctor Department'}),
            'college': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                        'placeholder': 'Enter Doctor College'}),
            'institute': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                                'placeholder': 'Enter Doctor institute'}),
            'degree': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                                'placeholder': 'Enter Doctor Degree'}),
            'hospital': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                                'placeholder': 'Enter Doctor Hospital'}),
            'permanent_address': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2','placeholder': 'Enter Permanent Address'}),
            'present_address': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2','placeholder': 'Enter Present Address'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2','placeholder': 'Enter Father Name'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2','placeholder': 'Enter Mother Name'}),
            'visit_day':forms.CheckboxSelectMultiple(attrs={'multiple':True}),
            'birth_date': forms.DateInput(format=('%d/%m/%y'), attrs={'class': 'form-control bg-light badge-pill p-2', 'type': 'date'}),
            'join_date': forms.DateInput(attrs={'class': 'form-control  bg-light badge-pill p-2 m-2', 'type': 'date-local'}, format='%Y-%m-%d'),
            
            'start_time': forms.TimeInput(format=('%H:%M'), attrs={'type': 'time', 'class': 'form-control bg-light badge-pill  p-2 m-2'}),
            'end_time': forms.TimeInput(format=('%H:%M'), attrs={'type': 'time', 'class': 'form-control bg-light badge-pill  p-2 m-2'}),
            "photo":forms.ClearableFileInput(attrs={"class":"form-control"}),
        }


class StaffAddForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'
        exclude = ['user', 'id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                           'placeholder': 'Enter Staff Name'}),
            'doctor': forms.Select(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                              'placeholder': 'Enter Doctor Name'}),
            'staff_id': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                                'placeholder': 'Enter Staff Id'}),
            'title': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                            'placeholder': 'Enter Staff Title'}),
            'email': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                            'placeholder': 'Enter Staff  Email'}),
            'nid': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                          'placeholder': 'Enter Staff NID'}),
            'phone': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                            'placeholder': 'Enter Staff  Phone'}),
            'gender': forms.Select(attrs={'class': 'form-control bg-light badge-pill p-2',
                                          'placeholder': 'Enter Staff  Gender'}),
           
            'ssc': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                          'placeholder': 'Enter Staff SSC Result'}),
            'hsc': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                          'placeholder': 'Enter Staff HSC Result'}),
            'honor': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                             'placeholder': 'Enter Staff Honers Result'}),
            'permanent_address': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2', 'placeholder': 'Enter Permanent Address'}),
            'present_address': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2', 'placeholder': 'Enter Present Address'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2', 'placeholder': 'Enter Father Name'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2', 'placeholder': 'Enter Mother Name'}),
           
            'birth_date': forms.DateInput(attrs={'class': 'form-control bg-light badge-pill p-2 ', 'type': 'date-local'}, format='%Y-%m-%d'),
            'join_date': forms.DateInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2', 'type': 'date-local'}, format='%Y-%m-%d'),

            "photo": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }
class LabAssistantForm(forms.ModelForm):
    class Meta:
        model = LabAssistant
        fields = '__all__'
        exclude = ['user', 'id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                           'placeholder': 'Enter Staff Name'}),
            
            'staff_id': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
            'lab': forms.Select(attrs={'class': 'form-control bg-light badge-pill p-2',
                                          'placeholder': 'Enter Staff  Gender'}),
                                                'placeholder': 'Enter Staff Id'}),
            'title': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                            'placeholder': 'Enter Staff Title'}),
            'email': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                            'placeholder': 'Enter Staff  Email'}),
            'nid': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                          'placeholder': 'Enter Staff NID'}),
            'phone': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                            'placeholder': 'Enter Staff  Phone'}),
            'gender': forms.Select(attrs={'class': 'form-control bg-light badge-pill p-2',
                                          'placeholder': 'Enter Staff  Gender'}),
           
            'degree1': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                          'placeholder': 'Enter Staff Degree'}),
            'institute1': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                          'placeholder': 'Enter Institute'}),
            'degree2': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                          'placeholder': 'Enter Staff Degree'}),
            'institute2': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                          'placeholder': 'Enter Institute'}),
            'degree3': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                          'placeholder': 'Enter Staff Degree'}),
            'institute3': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                          'placeholder': 'Enter Institute'}),
            
            'permanent_address': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2', 'placeholder': 'Enter Permanent Address'}),
            'present_address': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2', 'placeholder': 'Enter Present Address'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2', 'placeholder': 'Enter Father Name'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2', 'placeholder': 'Enter Mother Name'}),
           
            'birth_date': forms.DateInput(attrs={'class': 'form-control bg-light badge-pill p-2 ', 'type': 'date-local'}, format='%Y-%m-%d'),
            'join_date': forms.DateInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2', 'type': 'date-local'}, format='%Y-%m-%d'),

            "photo": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }

class SerialForm(forms.ModelForm):
    class Meta:
        model=Serial
        fields="__all__"
        exclude=['waiting_status','submit_status','done_status']
        widgets={
            'doctor': forms.Select(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                          'placeholder': 'Enter Doctor Name'}),
            'number': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                             'placeholder': 'Enter Patient Serial'}),
            'name': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                           'placeholder': 'Enter Patient Name'}),
            'gender': forms.Select(attrs={'class': 'form-control bg-light badge-pill p-2',
                                          'placeholder': 'Enter Patient  Gender'}),
            'age': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                             'placeholder': 'Enter Patient Age'}),
            'weight': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                             'placeholder': 'Enter Patient Name'}),
            'pressure': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                             'placeholder': 'Enter Patient Name'}),
            'visit_date': forms.DateInput(format=('%d/%m/%y'), attrs={'class': 'form-control bg-light badge-pill p-2', 'type': 'date'}),
            'issue_date': forms.DateInput(format=('%d/%m/%y'), attrs={'class': 'form-control bg-light badge-pill p-2', 'type': 'date'}),
            'address': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2 m-2',
                                              'placeholder': 'Enter Patient Address'}),
            'paid': forms.CheckboxInput(),
        }


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields =['name']


class SymptomForm(forms.ModelForm):
    class Meta:
        model = Symptom
        fields = ['symptom']

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields =['name']

class TestReportForm(forms.ModelForm):
    class Meta:
        model = TestReport
        fields =['point']

class MedicineForm(forms.ModelForm):
    class Meta:
        model=Medicine
        fields="__all__"
        exclude=['patient']
        widgets={
            'name': forms.TextInput(attrs={'size': 10}),
            'before_breakfast': forms.TextInput(attrs={'size': 2}),
            'morning': forms.TextInput(attrs={'size': 2}),
            'before_lunch': forms.TextInput(attrs={'size': 2}),
            'midday': forms.TextInput(attrs={'size': 2}),
            'before_dinner': forms.TextInput(attrs={'size': 2}),
            'night': forms.TextInput(attrs={'size': 2}),

        }
        labels = {
            'name':'Medicine',
            'before_breakfast':'Before',
            'before_dinner':"Before"
        }