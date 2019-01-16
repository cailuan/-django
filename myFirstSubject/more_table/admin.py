from django.contrib import admin
from .models import Student , Student_Detail,Deparment,Course

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['d_id','d_name']
    list_display_links = ['d_id','d_name']
    search_fields = ['d_name','d_id']
    list_per_page = 2
    fields = ['d_id']


admin.site.register(Student_Detail)
admin.site.register(Student)
admin.site.register(Deparment,DepartmentAdmin)
admin.site.register(Course)
