from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from PIL import Image


class CustomUserManager(BaseUserManager):

    # CustomUserManager methods not inherited
    def create_superuser(self, email, username, password, **other_fields):

        # setdefault gotten from django backend session
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError("Superuser must be assigned to is_staff=True")

        if other_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True")

        return self.create_user(email, username, password, **other_fields)




        # making use of the create_user method in this place 


    # CustomUserManager methods not inherited
    def create_user(self, email, username, password, **other_fields):
        if not email:
            raise ValueError("You must provide an email address")

        # Using the methods from the inherited class (BaseUserManager): normalize_email, set_password
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    class Types(models.TextChoices):
        CLIENT = "CLIENT", "Client"
        INDIVIDUAL = "INDIVIDUAL", "Individual"
        EMPLOYEE = "EMPLOYEE", "Employee"

    email = models.EmailField(_('email address'), unique=True)
    # password has been defined at the AbstractBaseUser class
    username = models.CharField(max_length=50)
    full_name = models.CharField(_('Full Name'),max_length=50)
    type = models.CharField(max_length=15, choices=Types.choices, default=Types.INDIVIDUAL)
    date_joined = models.DateTimeField(default=timezone.now)
    bio = models.TextField(_('biography'), max_length=500, blank=True, default='')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    #  

    is_individual = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return self.username
        

class ClientManager(models.Manager):
    # client for bringing jobs of schools, bulk cloth sowing
    # in form of large, small and medium sizes with the required quantity
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(type=User.Types.CLIENT)
        return queryset
        

class Client(User):

    class Meta:
        proxy = True

    objects = ClientManager()

    def save(self, *args, **kwargs):
        self.type = User.Types.CLIENT
        self.is_client = True
        self.is_active = True
        # Overiding the save method and calling it back
        return super().save(*args, **kwargs)



class IndividualManager(models.Manager):
    # A single user account
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(type=User.Types.INDIVIDUAL)
        return queryset
        

class Individual(User):

    class Meta:
        proxy = True

    objects = IndividualManager()

    def save(self, *args, **kwargs):
        self.type = User.Types.INDIVIDUAL
        self.is_individual = True
        self.is_active = True
        # Overiding the save method and calling it back
        return super().save(*args, **kwargs)
        


class EmployeeManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(type=User.Types.EMPLOYEE)
        return queryset
        

class Employee(User):

    class Meta:
        proxy = True

    objects = EmployeeManager()

    def save(self, *args, **kwargs):
        self.type = User.Types.EMPLOYEE
        self.is_employee = True
        # can login
        self.is_active = True

        # self.is_staff can be set to true here too
        # Overiding the save method and calling it back
        return super().save(*args, **kwargs)
        

class Profile(models.Model):
    GENDER_CHOICES = [
            ('Male', "Male"),
            ('Female', "Female")
            ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    address = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=25, choices=GENDER_CHOICES)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    
    class Meta:
      #  proxy = True
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
       #  abstract = True

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)





        

"""


class ClientProfile(Profile):
    
    class Meta:
        verbose_name = "ClientProfile"
        verbose_name_plural = "ClientProfiles"


class IndividualProfile(Profile):
    
    
    class Meta:
        verbose_name = "IndividualProfile"
        verbose_name_plural = "IndividualProfiles"


"""
