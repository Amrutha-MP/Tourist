from django.db import models

# Create your models here.
class Category_DB(models.Model):
    Category_Name=models.CharField(max_length=50,null=True,blank=True)
    Description=models.CharField(max_length=50,null=True,blank=True)
    Category_Image=models.ImageField(upload_to="Category Images",null=True,blank=True)
class Package_DB(models.Model):
    CategoryName=models.CharField(max_length=50,null=True,blank=True)
    Package_Name=models.CharField(max_length=50,null=True,blank=True)
    Package_Description=models.CharField(max_length=50,null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Days=models.CharField(max_length=50,null=True,blank=True)
    Description1=models.CharField(max_length=50,null=True,blank=True)
    Description2 = models.CharField(max_length=50, null=True, blank=True)
    Description3 = models.CharField(max_length=50, null=True, blank=True)
    Image1=models.ImageField(upload_to="Package Images",null=True,blank=True)
    Image2 = models.ImageField(upload_to="Package Images", null=True, blank=True)
    Image3 = models.ImageField(upload_to="Package Images", null=True, blank=True)