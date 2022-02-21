from django.db import models
import geocoder
from django.utils.text import slugify
import product
from django.db.models import Sum

mapbox_access_token = "pk.eyJ1IjoiZWx5YXNoIiwiYSI6ImNreXg0cmwwZjBmM3YybnFpcGt0YzlxcWMifQ.UgG6ExGXtchCMXDFojpHHA"


# Create your models here.
class Mine(models.Model):
    name = models.CharField(max_length=255)
    stone_type = models.CharField(max_length=255)
    discovery_license_number = models.CharField(max_length=125)
    date_of_issuance_of_the_discovery_license_number = models.DateField()
    operating_license_number = models.CharField(max_length=125)
    date_of_issuance_of_operating_license_number = models.DateField()
    minimum_operating_tonnage = models.IntegerField()
    government_law = models.IntegerField()
    province = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/madan/")
    description = models.TextField()
    address = models.TextField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)
    summary=models.TextField()
    bold=models.TextField()
    sub_bold=models.TextField()

    def total_operation(self):
        exportal = product.models.ExportalProduct.objects.filter(mine=self.id).aggregate(Sum("approximate_tonnage"))["approximate_tonnage__sum"]
        internal = product.models.InternalProduct.objects.filter(mine=self.id).aggregate(Sum("approximate_tonnage"))["approximate_tonnage__sum"]
        return exportal + internal

    def total_loaded(self):
        return product.models.Loaded.objects.filter(mine__name=self.name).aggregate(Sum("weight_of_scales"))["weight_of_scales__sum"]

    def __str__(self):
        return self.name
    #
    # def save(self, *args, **kwargs):
    #     g = geocoder.mapbox(self.address, key=mapbox_access_token)
    #     g = g.latlng
    #     self.lat = g[0]
    #     self.long = g[0]
    #     return super(Mine, self).save(*args, **kwargs)
