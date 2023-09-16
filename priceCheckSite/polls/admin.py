from django.contrib import admin
from .models import Choice, Question

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInLine]
#This tells Django that Choice objects are edited on the Question admin page, and by default provides 3 fields for choices

    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"] #Adds a filter to sort by date published
    search_fields = ["question_text"] #Adds a seach box at the top of the change list

admin.site.register(Question, QuestionAdmin) #Allows admin page to interact with Question objects

admin.site.register(Choice)
