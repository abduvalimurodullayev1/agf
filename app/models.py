from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Users must have a phone number!')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        user = self.create_user(phone_number, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = models.CharField(max_length=155, unique=False, null=True, blank=True)
    first_name = models.CharField(max_length=155, unique=False, null=True, blank=True)
    last_name = models.CharField(max_length=155, unique=False, null=True, blank=True)
    phone_validator = RegexValidator(
        regex=r'^\+998\d{9}$',
        message="Yaroqsiz telefon raqam!"
    )
    phone_number = models.CharField(
        max_length=25,
        validators=[phone_validator],
        null=True,
        blank=True,
        unique=True
    )
    image = models.ImageField(upload_to="images", null=True, blank=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()


# class Blog(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.title
#
#
# class BlogImage(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="images")
#     image = models.ImageField(upload_to="images")
#
#     def __str__(self):
#         return self.blog.title


class UserRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requests")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class CategoryImage(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="images")
    image = models.URLField()

    def __str__(self):
        return self.category.title


class CategoryInnerDescription(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="descriptions")
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.category.title + self.title


class Plant(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="plants")
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class PlantImage(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name="images")
    image = models.URLField()

    def __str__(self):
        return self.plant.title


class PlantInnerDescription(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name="descriptions")
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.plant.title


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.plant.title