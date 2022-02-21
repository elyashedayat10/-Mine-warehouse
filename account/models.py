from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from product.models import InternalProduct, ExportalProduct, ProductBase
from .managers import MyUserManager


# Create your models here.
class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=125, null=True, blank=True)
    last_name = models.CharField(max_length=125, null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    position = models.CharField(max_length=125, null=True, blank=True)
    activity_field = models.CharField(max_length=255)
    company_name = models.CharField(max_length=125, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_special = models.BooleanField(default=False)
    is_potential = models.BooleanField(default=False)
    is_possible = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    is_expire = models.BooleanField(default=False)
    password_change = models.DateField(null=True, blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("first_name",)
    objects = MyUserManager()

    #
    # def save(self, *args, **kwargs):
    #     self.password=self.pin
    #     return super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="like")
    product = models.ForeignKey(ProductBase, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} likes {self.product}"


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to="is_admin")
    file_name = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)


class SiteActivity(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
