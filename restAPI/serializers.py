from dataclasses import fields
from django.contrib.auth.models import User, Group
from .models import JobPosition,Department,Profile,Patient
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class JobPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosition
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    #position = JobPositionSerializer(instance=JobPositionSerializer)
    department = DepartmentSerializer(instance=DepartmentSerializer)
    
    class Meta:
        model = Profile
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'