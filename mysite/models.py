from django.db import models

# Create your models here.

# Contact Form Table Information

class contactinfo(models.Model): # Tablename

    # Columns Define 

    # Columnname = models.fieldtype(parameters required)
    name = models.CharField(max_length=50, null=False)
    mail = models.EmailField(max_length=50, null=False)
    contact = models.IntegerField(null=False)
    subject = models.CharField(max_length=50, null=False)
    message = models.CharField(max_length=150, null=True)


# Creating a table for products uploaded from admin side

class products(models.Model):

    category= models.CharField(max_length=50)
    name = models.CharField(max_length=60)
    price= models.IntegerField(default=0)
    description= models.CharField(max_length=250, default='', blank=True, null= True)
    image= models.ImageField(upload_to='uploads/products/')

    class Meta:
        db_table = 'products'

