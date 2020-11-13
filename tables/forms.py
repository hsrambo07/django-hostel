from django import forms
from .models import *  


class StuForm(forms.ModelForm):  
    class Meta:  
        model = Student  
        fields = "__all__"  

class WardenForm(forms.ModelForm):  
    class Meta:  
        model = Warden  
        fields = "__all__"  

class MessForm(forms.ModelForm):  
    class Meta:  
        model = Mess  
        fields = "__all__"  

class BlockForm(forms.ModelForm):  
    class Meta:  
        model = Block  
        fields = "__all__"  

class PtForm(forms.ModelForm):  
    class Meta:  
        model = Parent  
        fields = "__all__"  

class RoomForm(forms.ModelForm):  
    class Meta:  
        model = Room  
        fields = "__all__"  


class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('reg_no','s_name','s_address','s_contact') #Note that we didn't mention user field here.

    def save(self, force_insert=False,force_update=False,commit=True):
        student_profiles = super(UpdateStudentForm, self).save(commit=False)
        if commit:
            student_profiles.save()
        return student_profiles

