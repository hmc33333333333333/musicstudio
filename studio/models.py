from django.db import models
from django.contrib.auth.models import User

# Producer Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)

    name= models.CharField(default='Elie Hmc (Default)', max_length=200, null= True)

    title= models.CharField(default='Elie Hmc (Default)', max_length=200, null= True)

    desc_text=  'Hey there is a default text about you that yu can change.'

    desc= models.CharField(default=desc_text, max_length=200, null= True)
    
    profile_img= models.ImageField(default='img/logo.jpg', upload_to = 'images ',null=True, blank= True)


    def __str__(self):
        return self.name
    
