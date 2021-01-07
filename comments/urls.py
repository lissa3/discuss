from django.urls import path,re_path
# from django.conf.urls import url
from .views import show_comment,EditComment

app_name = 'comments'

urlpatterns = [ 
    path('',show_comment,name="com"),    
    path('edit-comment/',EditComment.as_view(),name="edit-comment"),    
    # path('edit-comment/<slug:slug>/<int:id>/',EditComment.as_view(),name="edit-comment"),    
    # path('edit-name/<profile_unid>/',DisplayNameChange.as_view(),name="name-edit"),
    
]