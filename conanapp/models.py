from django.db import models



class Allteam(models.Model):
    person_name = models.CharField(max_length=30,unique=True , default='name')
    field = models.CharField(max_length=30)
    image = models.ImageField()
    arabic = models.BooleanField(default=False)
    myteam = models.BooleanField(default=False)

    

class Package(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    points = models.TextField()
    arabic = models.BooleanField(default=False)
    
    
class Frequentlyquestion(models.Model):
    question = models.CharField(max_length=50)
    ask = models.CharField(max_length=100)
    arabic = models.BooleanField(default=False)
    
    
    
class Services(models.Model):
    choices= [
        ('website','website'),
        ('ux ui','ux ui'),
        ('Motion graphic','Motion graphic'),
        ]        
    name = models.CharField(max_length=30)
    image = models.ImageField()
    mockup = models.ImageField()
    type = models.CharField(max_length=20,choices=choices,default="ux ui")
    url = models.CharField(max_length=250)
    
    
    
class Graphicdesign(models.Model):
    filter=[
        ('social media','social media'),
        ('Branding','Branding'),
        ]
    name = models.CharField(max_length=30)
    image = models.ImageField()
    mockup = models.ImageField()
    url = models.CharField(max_length=250)
    type = models.CharField(max_length=20,choices=filter)
    
    
class Socialmedia(models.Model):
    filter=[
        ('facebook','facebook'),
        ('instagram','instagram'),
        ('behance','behance'),
        ]
    name = models.CharField(max_length=30)
    image = models.ImageField()
    mockup = models.ImageField()
    url = models.CharField(max_length=250)
    type = models.CharField(max_length=20,choices=filter)
    
   
class Mobileapplication(models.Model):
    filter=[
        ('android','android'),
        ('ios','ios'),
        ]
    name = models.CharField(max_length=30)
    image = models.ImageField()
    mockup = models.ImageField()
    url = models.CharField(max_length=250)
    type = models.CharField(max_length=20,choices=filter)
    
    
                     

class Subscription(models.Model):
    email = models.EmailField(unique=True)
    
    
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()     