from django.contrib import admin
from .models import * 


# class BrotherAdmin(admin.ModelAdmin):

#     list_display = ['name', 'age']
#     search_fields = ['name']    




class Arts_Admin(admin.ModelAdmin):

    list_display = ['title']
    search_fields = ['title']

class LayoutAdmin(admin.ModelAdmin):

    list_display = ['title'] 


admin.site.register(Layout, LayoutAdmin)
admin.site.register(Art_Work, Arts_Admin)
admin.site.site_header = "MEPKIN ABBEY ADMIN"



