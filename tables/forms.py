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