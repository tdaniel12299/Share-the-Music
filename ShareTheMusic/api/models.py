from django.db import models
import string
import random #these will be used to generate random codes for the rooms

def uniqCode():
    length = 6 

    while True:
        #random uses a func of choices which takes string and length module params (k), the string module
        # has a method of ascii that allows us to select the type of chars we randomly generate
        code = ''.join(random.choices(string.ascii_uppercase, k=length))

        #checks to make sure code is unique, filters through the objects in Room targeting the code object
        #in Room and comparing to the generated code, count method compares list
        if Room.objects.filter(code=code).count() == 0:
            break

    return code

# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=8, default='',unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=2)
    created_at = models.DateTimeField(auto_now_add=True)