from django.db import models

# Create your models here.

class fort(models.Model):
    f_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    add = models.CharField(max_length=255)
    add3d = models.CharField(max_length=255)
    info = models.TextField()

    def __str__(self):
        return self.name

class Contact_form(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'message from : ' + self.name