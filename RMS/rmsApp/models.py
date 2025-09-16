from django.db import models

# Create your models here.
class Recipe(models.Model):
  name=models.CharField(max_length=200)
  created_at=models.DateTimeField(auto_now_add=True)
  description=models.TextField(max_length=50000)
  ingredients=models.TextField(max_length=50000)
  instructions=models.TextField(max_length=50000)
  image=models.ImageField(upload_to='recipes/',null=True,blank=True)

  def __str__(self):
    return self.name
  