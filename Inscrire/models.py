from contextlib import nullcontext
from tokenize import blank_re
from django.db import models

# Create your models here.

class Filiere(models.Model):
     nom= models.CharField(max_length=200)
     
     def __str__ (self):
         return self.nom
class Filiere_Licence(Filiere):
     class Meta:
        verbose_name = 'Filière de licence'
        verbose_name_plural = 'Filières de licence'
     def __str__ (self):
         return self.nom

class Filiere_Master(Filiere):
     class Meta:
        verbose_name = 'Filière de master'
        verbose_name_plural = 'Filières de master'
     def __str__ (self):
         return self.nom
class Departement(models.Model):
     nom= models.CharField(max_length=200)
     filiere= models.ManyToManyField(Filiere, related_name='filiere', blank=True)
     class Meta:
        verbose_name = 'Departement'
        verbose_name_plural = 'Departements'
     def __str__ (self):
         return self.nom
class Orientation(models.Model):
     nom= models.CharField(max_length=200)
     nni=models.IntegerField()
     dateNaissance=models.DateField()
     lieuNaissance= models.CharField(max_length=200)
     serie= models.CharField(max_length=200)
     moyenGeneral=models.FloatField()
     filiere=models.CharField(max_length=200)
     niveau=models.CharField(max_length=200, null=True)
     class Meta:
        verbose_name = 'Orinetation'
        verbose_name_plural = 'Orientations'
     def __str__(self):  
        return self.nom 


class Etudiant(models.Model):
     nom= models.CharField(max_length=200)
     photoEtudiant=models.ImageField(null=True)
     nni=models.IntegerField()
     sexe=models.CharField(max_length=200)
     dateNaissance=models.DateField()
     lieuNaissance= models.CharField(max_length=200)
     telephone = models.CharField(max_length=200)
     email = models.CharField(max_length=200)
     carteIdentite=models.ImageField(null=True)
     numBac=models.IntegerField()
     serie= models.CharField(max_length=200)
     releveNote=models.ImageField(null=True)
     session= models.CharField(max_length=200)
     moyenGeneral=models.FloatField()
     pays= models.CharField(max_length=200)
     AnObtantionBac=models.DateField()
     niveau=models.CharField(max_length=200, null=True)

     class Meta:
          abstract=True
class Etudiant_Master(Etudiant):
     licence= models.CharField(max_length=200)
     filiere=models.ForeignKey(Filiere_Master, on_delete=models.CASCADE)

class Etudiant_Licence(Etudiant):
     filiere=models.ForeignKey(Filiere_Licence, on_delete=models.CASCADE) 

class Etudiant_Public_Master(Etudiant_Master):
     def __str__(self):  
        return self.nom

class Etudiant_Prive_Master(Etudiant_Master):
     def __str__(self):  
        return self.nom


class Etudiant_Public_Licence(Etudiant_Licence):
     def __str__(self):  
        return self.nom

class Etudiant_Prive_Licence(Etudiant_Licence):
     def __str__(self):  
        return self.nom

class Etudiant_Public_Master_Niveau1(Etudiant_Public_Master):
     class Meta:
        verbose_name = 'Master public M1'
        verbose_name_plural = 'Master public M1'
     def __str__(self):  
        return self.nom
class Etudiant_Public_Master_Niveau2(Etudiant_Public_Master):
     class Meta:
        verbose_name = 'Master public M2'
        verbose_name_plural = 'Master public M2'
     def __str__(self):  
        return self.nom
class Etudiant_Prive_Master_Niveau1(Etudiant_Prive_Master):
     class Meta:
        verbose_name = 'Master privé M1'
        verbose_name_plural = 'Master privé M1'
     def __str__(self):  
        return self.nom
class Etudiant_Prive_Master_Niveau2(Etudiant_Prive_Master):
     class Meta:
        verbose_name = 'Master privé M2'
        verbose_name_plural = 'Master privé M2'
     def __str__(self):  
        return self.nom

class Etudiant_Public_Licence_Niveau1(Etudiant_Public_Licence):
     class Meta:
        verbose_name = 'Licence public L1'
        verbose_name_plural = 'Licence public L1'
     def __str__(self):  
        return self.nom 

class Etudiant_Public_Licence_Niveau2(Etudiant_Public_Licence):
     class Meta:
        verbose_name = 'Licence public L2'
        verbose_name_plural = 'Licence public L2'
     def __str__(self):  
        return self.nom

class Etudiant_Public_Licence_Niveau3(Etudiant_Public_Licence):
     class Meta:
        verbose_name = 'Licence public L3'
        verbose_name_plural = 'Licence public L3'
     def __str__(self):  
        return self.nom

class Etudiant_Prive_Licence_Niveau1(Etudiant_Prive_Licence):
     class Meta:
        verbose_name = 'Licence privé L1'
        verbose_name_plural = 'Licence privé L1'
     def __str__(self):  
        return self.nom

class Etudiant_Prive_Licence_Niveau2(Etudiant_Prive_Licence):
     class Meta:
        verbose_name = 'Licence privé L2'
        verbose_name_plural = 'Licence privé L2'
     def __str__(self):  
        return self.nom

class Etudiant_Prive_Licence_Niveau3(Etudiant_Prive_Licence):
     class Meta:
        verbose_name = 'Licence privé L3'
        verbose_name_plural = 'Licence privé L3'
     def __str__(self):  
        return self.nom

class Arrchive(models.Model):
   commantire=models.CharField(max_length=500)
   fich=models.FileField(blank=True)
   img=models.ImageField(blank=True)
   def __str__ (self):
         return self.commantire