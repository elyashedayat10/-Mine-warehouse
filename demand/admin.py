from django.contrib import admin

from demand.models import Hold, Visit, Sample

admin.site.register(Hold),
admin.site.register(Visit),
admin.site.register(Sample)
