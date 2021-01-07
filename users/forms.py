# from django import forms
# from django.core import validators
# from django.utils.translation import gettext_lazy as _
# from .models import Follower

# class FollowerForm(forms.ModelForm):
#     class Meta:
#         model = Follower
#         fields = ('following','follower')

#     def clean(self):
#         data = super().clean()
#         follower = data['follower']
#         following = data['following']
#         if follower == following:
#             raise validatiors.ValidationError(_('Not possible to follow yourself'))    

       