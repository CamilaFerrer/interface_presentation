# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib import admin
from .models import Presentation, Slide

class SlideInline(admin.StackedInline):
    model = Slide
    fk_name = "presentation"
    extra = 0
    fields = ["content"]


class PresentationAdmin(admin.ModelAdmin):
    model = Presentation
    save_on_top = True
    inlines = [SlideInline]
    list_display = ['get_author_name',
                    'title',
                    'date_creation',
                    'date_modification']

    def get_author_name(self, obj):
        return obj.get_author()
    get_author_name.admin_order_field  = 'author'
    get_author_name.short_description = 'Autor'


class SlideAdmin(admin.ModelAdmin):
    model = Presentation

    list_display = ['get_author_name',
                    'get_title',
                    'content']

    search_fields = ['get_author_name',
                     'get_title']

    def get_author_name(self, obj):
        return obj.presentation.get_author()
    get_author_name.admin_order_field  = 'author'
    get_author_name.short_description = 'Autor'

    def get_title(self, obj):
        return obj.presentation.title
    get_title.admin_order_field  = 'title'
    get_title.short_description = 'Título'



admin.site.register(Presentation, PresentationAdmin)
admin.site.register(Slide, SlideAdmin)