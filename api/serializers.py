from rest_framework import serializers as ser
from django.contrib.auth import get_user_model
from ideas.models import Idea

User = get_user_model()


class IdeaSerializer(ser.ModelSerializer):
    owner_idea = ser.CharField(source='author.get_name', default="", read_only=True)
    class Meta:
        model = Idea
        fields = ('id','title','author','lead_text','main_text','owner_idea','categ','created_at','status','thumbnail')               
        # fields = ('slug','view_count','thumbnail')
               

class IdeaTestSerializer(ser.ModelSerializer):
    """ ONLY FOR TESTING:excl created_at: for testing """
    owner_idea = ser.CharField(source='author.get_name', default="", read_only=True)
    class Meta:
        model = Idea
        fields = (
            'id','title','author','lead_text','main_text','owner_idea','categ','status'
            )              
        # fields = ('slug','view_count','thumbnail') 

