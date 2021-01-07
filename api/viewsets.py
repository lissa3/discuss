from django.shortcuts import render
from rest_framework import  viewsets #, permissions
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
from .serializers import IdeaSerializer
from ideas.models import Idea
from .permissions import IsAuthorOrIsStaffOrReadOnly
# from .filters import IdeaFilter


User = get_user_model()
"""
tat@mail.com
"""

class IdeaViewSet(viewsets.ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer  
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]    
    # filter by categ_id,author_id
    filter_fields = ['categ','author','status'] #['categ__name']
    # search_fields = ['author__profile_display_name']
    search_fields = ['title','lead_text','main_text']
    ordering_fields = ['created_at']    
    permission_classes = (IsAuthorOrIsStaffOrReadOnly,) 


    def create(self, request, *args, **kwargs):
        """ user object will be 100% because auth-ed already"""
        # ????indicate how to create the serializer. want to populate the read_only author field with the requesting user then populate the serializer with this value.
        data = request.data
        data['author'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def perform_create(self,serializer):
    #     """take parent method from create and substitute it with custom behaviour"""
    #     #no success: cause user ! null in db 
    #     # object = super().perform_create(serializer)
    #     print("custom perform calling")
    #     print("ser valid data", serializer.validated_data)
    #     serializer.validated_data['author'] = self.request.user.id
    #     serializer.save()
            

        

    
         

