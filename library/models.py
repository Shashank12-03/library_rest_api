from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=100,verbose_name='title', unique=True)
    author=models.CharField(max_length=100, verbose_name="Author")
    pub_date=models.DateField(verbose_name="Publication date",blank=True,null=True)
    ISBN=models.CharField(max_length=13, verbose_name="ISBN", unique=True)
    description=models.TextField(null=True, verbose_name="Description")
    
    def __str__(self):
        return self.title