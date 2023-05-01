from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

#create new user

class MyAccountManager(BaseUserManager):
    def  create_user(self , email , username , password=None):
        if not email:
            raise ValueError("User must have an email")
        if not username:
            raise ValueError("user must have a username")
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self ,  email , password , username=None):
        if username == None:
            username=email.split("@")[0]
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

def get_profile_image_filepath(self):
    return f'profile_images/{self.pk}/{"profile_image.png"}'

def default_image ():
    return "media/default.png"

class Account(AbstractBaseUser):
    email = models.EmailField( verbose_name="Email", unique=True , max_length=254)
    username = models.CharField(verbose_name="Username", unique=True , max_length=50)
    date_joined = models.DateTimeField(verbose_name="Date joined" , auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="Last login" , auto_now=True)
    is_admin= models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.ImageField(max_length =255 , upload_to=get_profile_image_filepath, height_field=None, width_field=None,default=default_image , null=True , blank=True)
    hide_email = models.BooleanField(default= True)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['username']

    def __str__(self):
        return self.username
    
    def fet_profile_image_filename (self):
        return str(self.profile_image)[str (self.profile_image).index(f'profile_images/{self.pk}/'):]
    
    def has_perm(self , perm , obj=None):
        return self.is_admin
    
    def has_module_perms (self , app_lable):
        return True
