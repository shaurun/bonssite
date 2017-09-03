from django.contrib import admin

# Register your models here.
from bonssite.models import Section, Article

admin.site.register([Section, Article]);