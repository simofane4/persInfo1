from django.db import models



# Create your models here.
class Contact(models.Model):
   #image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
   nom = models.CharField( max_length=50)
   prenom = models.CharField( max_length=50)
   matricule = models.CharField( max_length=50)
   adresse = models.CharField(max_length=50)
   email = models.CharField( max_length=50)

   def __str__(self) :
       return self.nom,self.prenom




