from django import forms
from .models import Profile
from django.utils.translation import gettext_lazy as _
from django.core import validators

class ProfileForm(forms.ModelForm):    
    class Meta:
        model = Profile
        fields = (
            'first_name','last_name',
            'linkedin_profile','website','image'
            )
                  

    

class ProfileDisplayNameForm(forms.ModelForm):    
    class Meta:
        model = Profile
        fields = ('display_name',)
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['display_name'].help_text="You can change this display name but it should be unique"        

    def clean_display_name(self):
        print("clean method calling")
        display_name = self.cleaned_data.get('display_name')
        flag = Profile.objects.filter(display_name=display_name).exists()
        if flag:
            print("display name already in use")
            raise validators.ValidationError(_('This name is already in use'))  
        return display_name     
    