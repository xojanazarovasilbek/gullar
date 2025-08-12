from django.db import models

# Create your models here.
class Modele(models.Model):
    name = models.CharField(max_length=58)
    def __str__(self):
        return self.name

class Rang(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Name(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self):
        return self.name
    

class Gullar(models.Model):
    modele = models.ForeignKey(Modele, on_delete=models.CASCADE, related_name='modele')
    name = models.ForeignKey(Name, on_delete=models.CASCADE, related_name='gullar')
    rangi = models.ForeignKey(Rang, on_delete=models.CASCADE, related_name='rang')
    narxi = models.DecimalField(max_digits=10,decimal_places=2 )
    

    def __str__(self):
        return str(self.name)


