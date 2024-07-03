from django.contrib import admin
from .models import Question

# Making the poll app modifiable in the admin
admin.site.register(Question)