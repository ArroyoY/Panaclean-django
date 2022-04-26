from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Zone)
admin.site.register(District)
admin.site.register(Township)
admin.site.register(Tour)
admin.site.register(Client)
admin.site.register(Price)
admin.site.register(Schedule)
admin.site.register(Bill)
admin.site.register(Corrale)
admin.site.register(Collaborator)
admin.site.register(Collection_Service)
admin.site.register(User)
admin.site.register(report)