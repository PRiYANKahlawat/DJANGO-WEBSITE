from django.db import models
# Create your models here.

class Contact(models.Model):
    # to make it easy class is a  table/excel sheet/data base and given below are different columns/category
    name=models.CharField(max_length=122)
    email=models.CharField( max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):  
        return self.name  #this function is to show form entries in admin panel by name 

# model is something which defines our data base

# after this 2 steps are very important
        # 1. register your model- go to admin.py inside the app on which u working import the model and then write admin.site.register(model_name)
        # 2. register your app  by coping the name from apps.py and pasting it in settings.py>installed apps 

# after this write python manage.py makemigrations in the terminal and then python manage.py migrate
    # makemigrations - create changes and store in a file 
    # migrate- apply the pending changes created by makemigrations
  
  
  