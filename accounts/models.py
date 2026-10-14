from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    """Cria usuário usando o email no lugar do username."""

    use_in_migrations = True

    def _create_user(self, email, **extra_fields):
        if no email:
            raise valueError('O email é obrigatorio.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email,password, **extra_fields)

    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff, True)
        extra_fields.setdefault('os_superuser', True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Usuário que entra com email: o username sai e o email vira unico."""

    username= Nome

    email = models.EmailField('e-mail', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    0bjects = UserManager()

    def __str__(self):
        return self.email

