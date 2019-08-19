from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class app1Model(models.Model):
    name=models.CharField(max_length=250)
    completed=models.BooleanField(default=False)
    owner=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    
    def get_absolute_url(self):
        return reverse("details",kwargs={"pk":self.pk})
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
  