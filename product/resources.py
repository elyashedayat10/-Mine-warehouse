from .models import *

from import_export import resources


class Internal_Product_Resource(resources.ModelResource):
    class Meta:
        model = InternalProduct


class Exportal_Product_Resource(resources.ModelResource):
    class Meta:
        model = ExportalProduct


class Loaded_Product_Resource(resources.ModelResource):
    class Meta:
        model = Loaded


class Rejected_Product_Resource(resources.ModelResource):
    class Meta:
        model = Rejected
