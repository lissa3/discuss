from django.shortcuts import render,get_object_or_404,Http404
from django.contrib import messages
from django.views.generic import DetailView,UpdateView
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from utils.mixins import OwnerMixin
from .forms import ProfileForm,ProfileDisplayNameForm

class ProfileDetail(LoginRequiredMixin,OwnerMixin,DetailView):
    model = Profile    

class EditProfile(LoginRequiredMixin,OwnerMixin,UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name_suffix = '_update_form'

class DisplayNameChange(LoginRequiredMixin,OwnerMixin,UpdateView):
    model = Profile
    form_class = ProfileDisplayNameForm
    template_name = 'profiles/change_name.html'
    # success_url = reverse_lazy('/')

    def form_valid(self, form):
        messages.success(self.request, 'Display name has been updated!')
        return super().form_valid(form)   


