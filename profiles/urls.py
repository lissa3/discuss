from django.urls import path,re_path
from .views import ProfileDetail,EditProfile, DisplayNameChange

app_name = 'profiles'

urlpatterns = [     
    path('<profile_unid>/',ProfileDetail.as_view(),name="profile-info"),
    path('edit/<profile_unid>/',EditProfile.as_view(),name="profile-edit"),
    path('edit-name/<profile_unid>/',DisplayNameChange.as_view(),name="name-edit"),
    
]