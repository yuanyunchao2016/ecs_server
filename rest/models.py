from django.db import models

# Create your models here.
class User(models.Model):
    userId = models.IntegerField(db_index=True,default=0);
    username = models.CharField(db_index = True ,max_length=20,blank=True)
    password = models.CharField(max_length=20,blank=True)
    def __str__(self):
        return self.username

class log(models.Model):
    userId = models.IntegerField(db_index=True,default=0);
    time = models.DateTimeField(auto_now_add=True,db_index = True);
    context = models.CharField(max_length=1000,default="");

