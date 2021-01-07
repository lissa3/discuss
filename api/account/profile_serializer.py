from rest_framework import serializers as ser
from profiles.models import Profile


class ProfileSerializer(ser.ModelSerializer):
    name = ser.CharField(source='user.get_name', default="", read_only=True)
    # user=serializers.StringRelatedField(read_only=True)
    # user = ser.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model=Profile
        fields = ('user_id','unid','display_name','first_name','last_name','website','linkedin_profile','image','name') 


        