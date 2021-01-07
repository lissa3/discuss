from django.urls import path
from .views import IdeaList,IdeaDetail,foo

app_name = 'ideas'

urlpatterns = [    
    path('', IdeaList.as_view(),name='list'),
    path('detail-idea/<slug:slug>/', IdeaDetail.as_view(),name='detail'),
    path('bar/', foo),
    
    
]
