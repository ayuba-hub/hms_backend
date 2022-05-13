from random import choices
from django.db import models
from django.contrib.auth.models import User

choices =(
    ('cashier','Cashier'),
    ('receptionist','Receptionist'),
    ('admin','Admin')
)

gender = (
    ('Male','Male'),
    ('Female','Female')
)

religion = (
    ('CHRISTIANITY','CHRISTIANITY'),
    ('ISLAM','ISLAM'),
    ('TRADITIONALIST','TRADITIONALIST')
)

marital_status = (
    ('Single','Single'),
    ('Married','Married'),
    ('Divorsed','Divorsed')
)

relationship = (
    ('Father','Father'),
    ('Mother','Mother'),
    ('Husband','Husband'),
    ('Wife','Wife'),
    ('Son','Son'),
    ('Daughter','Daughter'),
    ('Other','Other')
)

class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.department}'

class JobPosition(models.Model):
    position = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.position}'

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=20,null=True,blank=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    position = models.CharField(max_length=100,choices=choices,default='')

    def __str__(self):
        return f'{self.user}'

class Patient(models.Model):
    folder_number = models.CharField(max_length=1000,help_text='for existing patients')
    enviro_ID = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20,help_text='surname')
    first_name = models.CharField(max_length=20)
    other_names = models.CharField(max_length=20,null=True,blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11,default='')
    date_of_birth = models.DateField(auto_now=False,auto_now_add=False)
    estimated_age = models.IntegerField(null=True,blank=True,help_text='Date of birth is approximate, leave blank if sure of date of birth')
    gender = models.CharField(max_length=10,choices=gender)
    religion = models.CharField(max_length=20,choices=religion)
    marital_status = models.CharField(max_length=20,choices=marital_status)
    occupation = models.CharField(max_length=100)
    state_of_residence = models.CharField(max_length=20)
    LGA = models.CharField(max_length=30)
    residential_address = models.CharField(max_length=100)
    state_of_origin = models.CharField(max_length=20)
    LGA = models.CharField(max_length=30)
    address_of_origin = models.CharField(max_length=100)
    next_of_kin = models.CharField(max_length=40)
    next_of_kin_relationship = models.CharField(max_length=20,choices=relationship)
    next_of_kin_phone_number = models.CharField(max_length=11)
    next_of_kin_address = models.CharField(max_length=100)

    def __str__(self):
        return '{} {}'.format(self.first_name,self.last_name)