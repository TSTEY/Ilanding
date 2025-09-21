from django.db import models
from django.contrib.auth.models import AbstractUser

class Header(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
class BlockOne(models.Model):
    name_1 = models.CharField(max_length=250)
    name_2 = models.CharField(max_length=250)
    button_1 = models.CharField(max_length=250)
    button_2 = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name_1
    
class BlockTwo(models.Model):
    name = models.CharField(max_length=250)
    text = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
class BlockThree(models.Model):
    name = models.CharField(max_length=250)
    text = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
class BlockFour(models.Model):
    name = models.CharField(max_length=250)
    text = models.CharField(max_length=250)
    button = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
class BlockFive(models.Model):
    imges = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    profession = models.CharField(max_length=250)
    text = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
class BlockSix(models.Model):
    number = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
class BlockSeven(models.Model):
    name = models.CharField(max_length=250)
    text = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
class BlockEight(models.Model):
    name = models.CharField(max_length=250)
    text = models.CharField(max_length=250)
    text_2 = models.CharField(max_length=250)
    text_3 = models.CharField(max_length=250)
    text_4 = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
class BlockNine(models.Model):
    name = models.CharField(max_length=250)
    text = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
    
class BlockTen(models.Model):
    name = models.CharField(max_length=250)
    text = models.CharField(max_length=250)
    button = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
class Footer(models.Model):
    name_1 = models.CharField(max_length=250)
    name_2 = models.CharField(max_length=250)
    name_3 = models.CharField(max_length=250)
    name_4 = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name_1
    

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)