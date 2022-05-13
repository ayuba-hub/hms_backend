from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from yaml import serialize_all
from .models import Department, JobPosition, Profile,Patient

from .serializers import (
    UserSerializer,
    GroupSerializer,
    DepartmentSerializer,
    ProfileSerializer,
    JobPositionSerializer,
    PatientSerializer
    )

class DepartmentVieSet(viewsets.ModelViewSet):
    """
    API endpoint for department
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class JobPositionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for job position
    """
    queryset = JobPosition.objects.all()
    serializer_class = JobPositionSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint for profile
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    #permission_classes = [permissions.IsAuthenticated]

class PatientViewSet(viewsets.ModelViewSet):
    """
    API endpoint for all patients
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims

        token['username'] = user.username
        token['firstname'] = user.first_name
        token['middlename'] = user.profile.middle_name
        token['lastname'] = user.last_name
        token['email'] = user.email
        token['position'] = user.profile.position
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer