from django.db import models

class Author(models.Model):  
    full_name = models.TextField()  
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)
    def __str__(self): return self.full_name

class Book(models.Model):  
    ISBN = models.CharField(max_length=13)  
    title = models.TextField()  
    description = models.TextField()  
    year_release = models.SmallIntegerField()  
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    copy_count = models.SmallIntegerField(default=1, blank=True, null=True)
    price = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=7)
    redaction = models.ForeignKey('Redaction', blank=True, null=True, on_delete=models.CASCADE, related_name='books')
    def __str__(self): return self.title

class Redaction(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self): return self.name

    
