from ast import Param
from operator import truediv
from pickle import FALSE
from django import forms
from django.forms.utils import ErrorList


class ParagraphErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()
    def as_divs(self):
        if not self: return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<p class="small error">%s</p>' % e for e in self])


class Etudiant_Licence_Public_L1Form(forms.Form):
    nom= forms.CharField(label='',required=True, widget=forms.TextInput(
        attrs={
            'placeholder':'Votre nom ici',
        }
    ))
    photoEtudiant= forms.ImageField(required=True, widget=forms.FileInput(
        attrs={
        }
    ))
    nni= forms.RegexField(regex='/^(2|3|4)[0-9]{7}/gi',label='',required=True, widget=forms.NumberInput(
        attrs={
            'placeholder':'Votre nni ici',
        }
    ))
    lieuNaissance= forms.CharField(label='',required=True, widget=forms.TextInput(
        attrs={
            'placeholder':'Votre lieu de naissance ici',
        }
    ))
    email= forms.EmailField(label='',required=False, widget=forms.EmailInput(
        attrs={
            'placeholder':'Email',
        }
    ))
    carteIdentite= forms.ImageField(required=True, widget=forms.FileInput(
        attrs={
        }
    ))
    releveNote= forms.ImageField(required=True, widget=forms.FileInput(
        attrs={
        }
    ))
    # telephone=forms.RegexField(regex=r'^\+?1?\d{9,15}$', error_messages=("Incorret"))
    # class Meta:
    #      model = Etudiant_Licence_Public_L1
    #      fields = ['nom' , 'photoEtudiant', 'nni', 'sexe','lieuNaissance','dateNaissance','telephone','email','carteIdentite', 'numBac', 'bac' , 'releveNote','session',  'moyen','pays','annObBac','filiere']
         