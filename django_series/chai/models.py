from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class chaivarity(models.Model):
    CHAI_TYPE=[
        ('ML','MASALA'),
        ('GR','GINGER'),
        ('KL','KIWI'),
        ('PL','PLAIN'),
        ('EL','ELACHI')
    ]
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='chais/')
    date_added=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2,choices=CHAI_TYPE)
    description=models.TextField(default='')
    
    def __str__(self):
        return self.name
    
#one to many
class chaiReview(models.Model):
    chai=models.ForeignKey(chaivarity,on_delete=models.CASCADE,related_name='review')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.IntegerField()
    comment=models.TextField()
    date_added=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    
#many to many
class store(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    chai_varity=models.ManyToManyField(chaivarity,related_name='store')
    
    def __str__(self):
        return self.name
    
#one to one
class chaicertificate(models.Model):
    chai=models.OneToOneField(chaivarity,on_delete=models.CASCADE,related_name='certificate')
    certificate_number=models.CharField(max_length=100)
    issued_date=models.DateTimeField(default=timezone.now)
    valid_untill=models.DateTimeField()
    
    def __str__(self):
        return f'certificate for {self.name.chai}'   
