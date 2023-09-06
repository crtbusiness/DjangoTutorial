from django.contrib import admin
from .models import Question

admin.site.register(Question) #Allows admin page to interact with Question objects