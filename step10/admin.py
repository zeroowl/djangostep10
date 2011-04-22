# -*- coding: utf-8 -*-
from django.contrib import admin
from step10.models import *

#class AuthorAdmin(admin.ModelAdmin):
#    list_display = ('first_name', 'last_name', 'email')
#    search_fields = ('first_name', 'last_name')
#
#class BookAdmin(admin.ModelAdmin):
#    list_display = ('title', 'publisher', 'publication_date')
#    list_filter = ('publication_date',)
#    date_hierarchy = 'publication_date'
#    fields = ('title', 'authors', 'publisher', 'publication_date')
#    filter_horizontal = ('authors',)
#    raw_id_fields = ('publisher',)
class SavedAnswerInline(admin.StackedInline):
    model = SavedAnswer
    #extra = 15

class AnswerSetAdmin(admin.ModelAdmin):
    inlines = [SavedAnswerInline]
    list_display   = ('date', 'author', 'count')

#admin.autodiscover()

admin.site.register(Question)
admin.site.register(QuestionType)
admin.site.register(AnswerSet,AnswerSetAdmin)
admin.site.register(SavedAnswer)
admin.site.register(QuestionSet)
__author__ = 'zeroowl'
  
