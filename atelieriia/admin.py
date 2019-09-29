from django.contrib import admin

# Register your models here.
from .models import Profile,Question,Comment_to_question,Response_to_comments


from django.contrib.auth.models import User



admin.site.register(Profile)
admin.site.register(Question)

admin.site.register(Comment_to_question)
admin.site.register(Response_to_comments)