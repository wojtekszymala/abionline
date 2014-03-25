from django.contrib import admin

# Register your models here.
from .models import SignUP


class SignUpAdmin(admin.ModelAdmin):
    class Meta:
        model = SignUP

admin.site.register(SignUP,SignUpAdmin)