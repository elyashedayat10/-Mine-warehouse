from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, password):
        if not email:
            raise ValueError("This Field is required")
        if not first_name:
            raise ValueError("this Field is required")

        user = self.model(email=self.normalize_email(email), first_name=first_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, password):
        if not email:
            raise ValueError("this Field is required")
        if not first_name:
            raise ValueError("this Field is required")
        user = self.create_user(email=email, first_name=first_name, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user
