from django.contrib import admin

# Register your models here.

from .models import Course, Step_Course, Sub_Step_Course, Review

class PostAdmin(admin.ModelAdmin):
	readonly_fields = [
		'slug',
	]

admin.site.register(Course,PostAdmin)
admin.site.register(Step_Course,PostAdmin)
admin.site.register(Sub_Step_Course)
admin.site.register(Review)
