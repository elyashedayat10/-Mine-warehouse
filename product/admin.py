from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


@admin.register(Rejected)
class PersonAdmin(ImportExportModelAdmin):
    pass


@admin.register(Loaded)
class PersonAdmin(ImportExportModelAdmin):
    pass


@admin.register(ExportalProduct)
class PersonAdmin(ImportExportModelAdmin):
    pass


@admin.register(InternalProduct)
class PersonAdmin(ImportExportModelAdmin):
    pass

admin.site.register(LinedProducts),
admin.site.register(LinedProductMember),
admin.site.register(InternalMainPic),
admin.site.register(ExportalMainPic),
admin.site.register(InternalMainPicFile),
admin.site.register(ProductBase),
admin.site.register(ExportalGalleries),
admin.site.register(InternalGalleries)
