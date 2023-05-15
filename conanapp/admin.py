from django.contrib import admin
from .models import *
# Register your models here.

class NewAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Allteam._meta.get_fields()]
    search_fields = ['person_name' , 'field']
    
class NewAdmin1(admin.ModelAdmin):
    list_display = [field.name for field in Contact._meta.get_fields()]
    search_fields = ['name']
    
    
class NewAdmin2(admin.ModelAdmin):
    list_display = [field.name for field in Frequentlyquestion._meta.get_fields()]
    search_fields = ['question']
    
    
class NewAdmin3(admin.ModelAdmin):
    list_display = [field.name for field in Graphicdesign._meta.get_fields()]
    search_fields = ['name']
    
    
class NewAdmin4(admin.ModelAdmin):
    list_display = [field.name for field in Mobileapplication._meta.get_fields()]
    search_fields = ['name']
    
    
class NewAdmin5(admin.ModelAdmin):
    list_display = [field.name for field in Package._meta.get_fields()]
    search_fields = ['name']
    
    
class NewAdmin6(admin.ModelAdmin):
    list_display = [field.name for field in Services._meta.get_fields()]
    search_fields = ['name']
    
    
class NewAdmin7(admin.ModelAdmin):
    list_display = [field.name for field in Socialmedia._meta.get_fields()]
    search_fields = ['name']
    
    
class NewAdmin8(admin.ModelAdmin):
    list_display = [field.name for field in Subscription._meta.get_fields()]
    search_fields = ['email']
    
        
    


admin.site.register(Allteam,NewAdmin)
# admin.site.register(Package,NewAdmin5)
admin.site.register(Services,NewAdmin6)
admin.site.register(Graphicdesign,NewAdmin3)
admin.site.register(Socialmedia,NewAdmin7)
admin.site.register(Mobileapplication,NewAdmin4)
admin.site.register(Subscription,NewAdmin8)
admin.site.register(Frequentlyquestion,NewAdmin2)
admin.site.register(Contact,NewAdmin1)

admin.site.site_header = 'ConanPlus'
admin.site.site_title = ' ConanPlus'