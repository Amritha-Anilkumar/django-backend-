from django.contrib import admin
from mainapp.models import Register,Teacher,GalleryImage
from django.utils.html import format_html

# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email', 'phone', 'preference') 
    search_fields = ('fname', 'lname', 'email')  
    list_filter = ('preference',)  
admin.site.register(Register,RegisterAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'photo_tag')  
    search_fields = ('name', 'specialization')              
    list_filter = ('specialization',)                       

    def photo_tag(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:50%;" />', obj.photo.url)
        return "No Photo"

    photo_tag.short_description = 'Photo'

admin.site.register(Teacher,TeacherAdmin)

admin.site.register(GalleryImage)