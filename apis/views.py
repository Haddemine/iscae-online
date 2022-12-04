from django.shortcuts import render
from yaml import serialize
from Inscrire import models
from .serializers import Etudiant_Prive_Licence_Niveau1Serializers, Etudiant_Prive_Licence_Niveau2Serializers, Etudiant_Prive_Licence_Niveau3Serializers, Etudiant_Prive_Master_Niveau1Serializers, Etudiant_Prive_Master_Niveau2Serializers, Etudiant_Public_Licence_Niveau1Serializers, Etudiant_Public_Licence_Niveau2Serializers, Etudiant_Public_Licence_Niveau3Serializers, Etudiant_Public_Master_Niveau1Serializers, Etudiant_Public_Master_Niveau2Serializers, inscriptinSerializers
from rest_framework import generics

# Create your views here.

class ListFilier_Licence(generics.ListCreateAPIView):
    queryset=models.Filiere_Licence.objects.all()
    serializer_class= inscriptinSerializers  

class DetailFilier_Licence(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Filiere_Licence.objects.all()
    serializer_class= inscriptinSerializers   

class ListEtudiant_Public_Licence_Niveau1(generics.ListCreateAPIView):
    queryset=models.Etudiant_Public_Licence_Niveau1.objects.all()
    serializer_class= Etudiant_Public_Licence_Niveau1Serializers 

class DetailEtudiant_Public_Licence_Niveau1(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Etudiant_Public_Licence_Niveau1.objects.all()
    serializer_class= Etudiant_Public_Licence_Niveau1Serializers 

class ListEtudiant_Public_Licence_Niveau2(generics.ListCreateAPIView):
    queryset=models.Etudiant_Public_Licence_Niveau2.objects.all()
    serializer_class= Etudiant_Public_Licence_Niveau2Serializers 

class DetailEtudiant_Public_Licence_Niveau2(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Etudiant_Public_Licence_Niveau2.objects.all()
    serializer_class= Etudiant_Public_Licence_Niveau2Serializers 

class ListEtudiant_Public_Licence_Niveau3(generics.ListCreateAPIView):
    queryset=models.Etudiant_Public_Licence_Niveau3.objects.all()
    serializer_class= Etudiant_Public_Licence_Niveau3Serializers 

class DetailEtudiant_Public_Licence_Niveau3(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Etudiant_Public_Licence_Niveau3.objects.all()
    serializer_class= Etudiant_Public_Licence_Niveau3Serializers 

class ListEtudiant_Prive_Licence_Niveau1(generics.ListCreateAPIView):
    queryset=models.Etudiant_Prive_Licence_Niveau1.objects.all()
    serializer_class= Etudiant_Prive_Licence_Niveau1Serializers 

class DetailEtudiant_Prive_Licence_Niveau1(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Etudiant_Prive_Licence_Niveau1.objects.all()
    serializer_class= Etudiant_Prive_Licence_Niveau1Serializers 

class ListEtudiant_Prive_Licence_Niveau2(generics.ListCreateAPIView):
    queryset=models.Etudiant_Prive_Licence_Niveau2.objects.all()
    serializer_class= Etudiant_Prive_Licence_Niveau2Serializers 

class DetailEtudiant_Prive_Licence_Niveau2(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Etudiant_Prive_Licence_Niveau2.objects.all()
    serializer_class= Etudiant_Prive_Licence_Niveau2Serializers 

class ListEtudiant_Prive_Licence_Niveau3(generics.ListCreateAPIView):
    queryset=models.Etudiant_Prive_Licence_Niveau3.objects.all()
    serializer_class= Etudiant_Prive_Licence_Niveau3Serializers 

class DetailEtudiant_Prive_Licence_Niveau3(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Etudiant_Prive_Licence_Niveau3.objects.all()
    serializer_class= Etudiant_Prive_Licence_Niveau3Serializers 

class ListEtudiant_Public_Master_Niveau1(generics.ListCreateAPIView):
    queryset=models.Etudiant_Public_Master_Niveau1.objects.all()
    serializer_class= Etudiant_Public_Master_Niveau1Serializers 

class DetailEtudiant_Public_Master_Niveau1(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Etudiant_Public_Master_Niveau1.objects.all()
    serializer_class= Etudiant_Public_Master_Niveau1Serializers 

class ListEtudiant_Public_Master_Niveau2(generics.ListCreateAPIView):
    queryset=models.Etudiant_Public_Master_Niveau2.objects.all()
    serializer_class= Etudiant_Public_Master_Niveau2Serializers 

class DetailEtudiant_Public_Master_Niveau2(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Etudiant_Public_Master_Niveau2.objects.all()
    serializer_class= Etudiant_Public_Master_Niveau2Serializers 

class ListEtudiant_Prive_Master_Niveau1(generics.ListCreateAPIView):
    queryset=models.Etudiant_Prive_Master_Niveau1.objects.all()
    serializer_class= Etudiant_Prive_Master_Niveau1Serializers 

class DetailEtudiant_Prive_Master_Niveau1(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Etudiant_Prive_Master_Niveau1.objects.all()
    serializer_class= Etudiant_Prive_Master_Niveau1Serializers 

class ListEtudiant_Prive_Master_Niveau2(generics.ListCreateAPIView):
    queryset=models.Etudiant_Prive_Master_Niveau2.objects.all()
    serializer_class= Etudiant_Prive_Master_Niveau2Serializers 

class DetailEtudiant_Prive_Master_Niveau2(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Etudiant_Prive_Master_Niveau2.objects.all()
    serializer_class= Etudiant_Prive_Master_Niveau2Serializers 