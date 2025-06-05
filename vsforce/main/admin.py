from django.contrib import admin
from .models import Service, StaffMember
from .models import ContactMessage

admin.site.register(Service)
admin.site.register(StaffMember)



admin.site.register(ContactMessage)
