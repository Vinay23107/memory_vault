from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Vacation_name(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='vac')
    user=models.ForeignKey(User, on_delete=models.CASCADE)

class Vacation_image(models.Model):
    v_name=models.ForeignKey(Vacation_name, on_delete=models.CASCADE)
    v_image=models.ImageField(upload_to='v_images')