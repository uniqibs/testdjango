from django.db import models
class blog(models.Model):
    title = models.CharField(max_length=151)
    name = models.CharField(max_length=100)
    Content = models.TextField()
    mod = models.DateField(auto_now_add=True)
    
    update = models.models.DateField((""), auto_now=False, auto_now_add=False)