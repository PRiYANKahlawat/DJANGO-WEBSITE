from django.contrib import admin

#MANUALLY  ADDED
# this step is to register my model 
from HOME_first_app.models import  Contact  #first import the model u want to register from the respective app ( contacts     is the model in this case )
# Register your models here.

admin.site.register(Contact)  # write this exact thing down ...this will show the model data/submit data to admin