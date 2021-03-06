from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not username:
            raise ValueError('Users must have an username address')
        user = self.model(
            username=(username),
        )
        user.set_password(password)
        user.save()
        return user

    def create_staffuser(self, username, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            username,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            username,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    class Meta:
        verbose_name = 'Accounts'
        verbose_name_plural = 'Accounts'

    picture = models.FileField(verbose_name='pic', upload_to='user_picture/', default='user_picture/avatar5.png',
                               blank=True)
    first_name = models.CharField(max_length=60, verbose_name='name', blank=True)
    last_name = models.CharField(max_length=60, verbose_name='last name', blank=True)
    username = models.CharField(max_length=60, verbose_name='username', null=True, blank=True, unique=True, )
    phone_number = models.BigIntegerField(default=0, verbose_name='phone', blank=True, null=True)
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
        blank=True,
        null=True
    )
    is_active = models.BooleanField(default=True, verbose_name='isactive')
    staff = models.BooleanField(default=True, verbose_name='')
    isownerHotel = models.BooleanField(default=False, verbose_name='isOwnHotel')  # a admin user; non super-user
    admin = models.BooleanField(default=False, verbose_name='isadmin')  # a superuser
    join_date = models.DateField(auto_now_add=True, verbose_name="join_date")

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []  # Email & Password are required by default.

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    objects = UserManager()



class City(models.Model):
    name=models.CharField(verbose_name="City", max_length=100)