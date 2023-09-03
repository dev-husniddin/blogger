from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    nickname = models.CharField("Nickname", max_length=50, unique=True)
    phone = models.CharField("Phone", max_length=13, null=True, blank=True)
    image = models.ImageField("Avatar", upload_to="users/avatar", null=True, blank=True)
    registration_date = models.DateTimeField("Time of creation", auto_now_add=True)
    update_time = models.DateTimeField("Update time", auto_now=True)
    status = models.BooleanField("Status(active)", default=True)
    role = models.CharField(max_length=50, choices=[('admin', 'Administrator'), ('user', 'Regular user')])
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    REQUIRED_FIELDS = ['email']

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_users',
        blank=True,
        verbose_name='Groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_users',
        blank=True,
        verbose_name='User permissions',
        help_text='Specific permissions for this user.',
    )

    def __str__(self):
        return self.nickname
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = 'Users'

    

