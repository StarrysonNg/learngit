# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Article
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'content', 'pub_time')
	list_filter = ('pub_time', )
	search_fields = ('title', )
	
admin.site.register(Article, ArticleAdmin)
