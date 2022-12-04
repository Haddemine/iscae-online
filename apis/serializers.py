from dataclasses import field
import imp
from rest_framework import serializers
from Inscrire import models

class inscriptinSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=models.Filiere_Licence
class Etudiant_Public_Licence_Niveau1Serializers(serializers.ModelSerializer):
    class Meta:
        fields=(
            'id',
            'nom' , 'photoEtudiant', 'nni', 'sexe','lieuNaissance','dateNaissance','telephone','email','carteIdentite', 'numBac', 'serie' , 'releveNote','session',  'moyenGeneral','pays','AnObtantionBac','filiere','niveau'
        )
        model=models.Etudiant_Public_Licence_Niveau1
class Etudiant_Public_Licence_Niveau2Serializers(serializers.ModelSerializer):
    class Meta:
        fields=(
            'id',
            'nom' , 'photoEtudiant', 'nni', 'sexe','lieuNaissance','dateNaissance','telephone','email','carteIdentite', 'numBac', 'serie' , 'releveNote','session',  'moyenGeneral','pays','AnObtantionBac','filiere','niveau'
        )
        model=models.Etudiant_Public_Licence_Niveau2
class Etudiant_Public_Licence_Niveau3Serializers(serializers.ModelSerializer):
    class Meta:
        fields=(
            'id',
            'nom' , 'photoEtudiant', 'nni', 'sexe','lieuNaissance','dateNaissance','telephone','email','carteIdentite', 'numBac', 'serie' , 'releveNote','session',  'moyenGeneral','pays','AnObtantionBac','filiere','niveau'
        )
        model=models.Etudiant_Public_Licence_Niveau3

class Etudiant_Prive_Licence_Niveau1Serializers(serializers.ModelSerializer):
    class Meta:
        fields=(
            'id',
            'nom' , 'photoEtudiant', 'nni', 'sexe','lieuNaissance','dateNaissance','telephone','email','carteIdentite', 'numBac', 'serie' , 'releveNote','session',  'moyenGeneral','pays','AnObtantionBac','filiere','niveau'
        )
        model=models.Etudiant_Prive_Licence_Niveau1

class Etudiant_Prive_Licence_Niveau2Serializers(serializers.ModelSerializer):
    class Meta:
        fields=(
            'id',
            'nom' , 'photoEtudiant', 'nni', 'sexe','lieuNaissance','dateNaissance','telephone','email','carteIdentite', 'numBac', 'serie' , 'releveNote','session',  'moyenGeneral','pays','AnObtantionBac','filiere','niveau'
        )
        model=models.Etudiant_Prive_Licence_Niveau2

class Etudiant_Prive_Licence_Niveau3Serializers(serializers.ModelSerializer):
    class Meta:
        fields=(
            'id',
            'nom' , 'photoEtudiant', 'nni', 'sexe','lieuNaissance','dateNaissance','telephone','email','carteIdentite', 'numBac', 'serie' , 'releveNote','session',  'moyenGeneral','pays','AnObtantionBac','filiere','niveau'
        )
        model=models.Etudiant_Prive_Licence_Niveau3

class Etudiant_Public_Master_Niveau1Serializers(serializers.ModelSerializer):
    class Meta:
        fields=(
            'id',
            'nom' , 'photoEtudiant', 'nni', 'sexe','lieuNaissance','dateNaissance','telephone','email','carteIdentite', 'numBac', 'serie' , 'releveNote','session',  'moyenGeneral','pays','AnObtantionBac','filiere','niveau'
        )
        model=models.Etudiant_Public_Master_Niveau1
class Etudiant_Public_Master_Niveau2Serializers(serializers.ModelSerializer):
    class Meta:
        fields=(
            'id',
            'nom' , 'photoEtudiant', 'nni', 'sexe','lieuNaissance','dateNaissance','telephone','email','carteIdentite', 'numBac', 'serie' , 'releveNote','session',  'moyenGeneral','pays','AnObtantionBac','filiere','niveau'
        )
        model=models.Etudiant_Public_Master_Niveau2

class Etudiant_Prive_Master_Niveau1Serializers(serializers.ModelSerializer):
    class Meta:
        fields=(
            'id',
            'nom' , 'photoEtudiant', 'nni', 'sexe','lieuNaissance','dateNaissance','telephone','email','carteIdentite', 'numBac', 'serie' , 'releveNote','session',  'moyenGeneral','pays','AnObtantionBac','filiere','niveau'
        )
        model=models.Etudiant_Prive_Master_Niveau1
class Etudiant_Prive_Master_Niveau2Serializers(serializers.ModelSerializer):
    class Meta:
        fields=(
            'id',
            'nom' , 'photoEtudiant', 'nni', 'sexe','lieuNaissance','dateNaissance','telephone','email','carteIdentite', 'numBac', 'serie' , 'releveNote','session',  'moyenGeneral','pays','AnObtantionBac','filiere','niveau'
        )
        model=models.Etudiant_Prive_Master_Niveau2