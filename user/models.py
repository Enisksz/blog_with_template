from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUserModel(AbstractUser):
    image = models.ImageField(upload_to='image/',blank=True,null=True,default='pngtree-blue-default-avatar-png-image_2813123.jpg')#resim yüklemek istemeyebiliriz ondan 
                                                                      #blank yaptık ve databasede de boş olması için null yaptık.

    class Meta:
        db_table='user'
        verbose_name='User'

    def __str__(self):
        return self.username       

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url          