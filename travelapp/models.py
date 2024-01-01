from django.db import models

# Create your models here.
class blog(models.Model):
    date=models.IntegerField()
    month=models.TextField()
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=50)
    b_img=models.ImageField(upload_to='picture')
    b_desc=models.TextField()

class place(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)

