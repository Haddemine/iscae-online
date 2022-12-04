from contextlib import nullcontext
from http.client import HTTPResponse
import imp
import re
from multiprocessing import context
from multiprocessing.spawn import import_main_path
from django.shortcuts import get_object_or_404, render
from django.http.response import HttpResponse

from Inscrire.forms import Etudiant_Licence_Public_L1Form
from .models import  Arrchive, Etudiant_Prive_Licence_Niveau1, Etudiant_Prive_Licence_Niveau2, Etudiant_Prive_Licence_Niveau3, Etudiant_Prive_Master_Niveau1, Etudiant_Prive_Master_Niveau2, Etudiant_Public_Licence_Niveau1, Etudiant_Public_Licence_Niveau2, Etudiant_Public_Licence_Niveau3, Etudiant_Public_Master_Niveau1, Etudiant_Public_Master_Niveau2, Filiere,  Filiere_Licence, Filiere_Master, Orientation
from django.db import transaction, IntegrityError
from django.http import FileResponse
import os

prefixes=[20,22]
sufix="^\d{6}$"
# Create your views here.
def index(request):
    
    nombrelprn1=Etudiant_Prive_Licence_Niveau1.objects.count()
    nombrelprn2=Etudiant_Prive_Licence_Niveau2.objects.count()
    nombrelprn3=Etudiant_Prive_Licence_Niveau3.objects.count()
    nombrelpun1=Etudiant_Public_Licence_Niveau1.objects.count()
    nombrelpun2=Etudiant_Public_Licence_Niveau2.objects.count()
    nombrelpun3=Etudiant_Public_Licence_Niveau3.objects.count()
    nombremaster=0
    context = {
    
    'nombremaster':nombremaster,
    "nombrelprn1":nombrelprn1,
    "nombrelprn2":nombrelprn2,
    "nombrelprn3":nombrelprn3,
    "nombrelpun1":nombrelpun1,
    "nombrelpun2":nombrelpun2,
    "nombrelpun3":nombrelpun3,
    }
    return render(request, 'Inscrire/index.html',context)

def arrchive(request):
    arrchives=Arrchive.objects.all()
    context = {
    'arrchives': arrchives
    }
    return render(request, 'Inscrire/arrchive.html',context)
def openfile(request):
    filepath = os.path.join('static', 'sample.pdf')
    return FileResponse(open('9._GIT.pdf', 'rb'), content_type='application/pdf')
def stat(request):
    nombrelprn1=Etudiant_Prive_Licence_Niveau1.objects.count()
    nombrelprn2=Etudiant_Prive_Licence_Niveau2.objects.count()
    nombrelprn3=Etudiant_Prive_Licence_Niveau3.objects.count()
    nombrelpun1=Etudiant_Public_Licence_Niveau1.objects.count()
    nombrelpun2=Etudiant_Public_Licence_Niveau2.objects.count()
    nombrelpun3=Etudiant_Public_Licence_Niveau3.objects.count()
    ok=Etudiant_Public_Master_Niveau1.objects.count()
    nombremasterpub2=Etudiant_Public_Master_Niveau2.objects.count()
    nombremasterpri1=Etudiant_Prive_Master_Niveau1.objects.count()
    nombremasterpri2=Etudiant_Prive_Master_Niveau2.objects.count()

    context = {
    'nombremasterpri1':nombremasterpri1,
    'nombremasterpri2':nombremasterpri2,
    'nombremasterpub2':nombremasterpub2,
    'ok':ok,
    "nombrelprn1":nombrelprn1,
    "nombrelprn2":nombrelprn2,
    "nombrelprn3":nombrelprn3,
    "nombrelpun1":nombrelpun1,
    "nombrelpun2":nombrelpun2,
    "nombrelpun3":nombrelpun3,
    }
    return render(request, 'Inscrire/stat.html',context)

def listing(request):
    filieres=Filiere.objects.all()
    context = {
    'filieres': filieres
    }
    return render(request, 'Inscrire/inscrire.html',context)
def listingEtudiant(request):
    return render(request, 'Inscrire/listingEtudiant.html')









def listl1pu(request):
    etudiants=Etudiant_Public_Licence_Niveau1.objects.all()
    context = {
    'etudiants': etudiants
    }
    return render(request, 'Inscrire/listl1pu.html',context)

def listl2pu(request):
    etudiants=Etudiant_Public_Licence_Niveau2.objects.all()
    context = {
    'etudiants': etudiants
    }
    return render(request, 'Inscrire/listl1pu.html',context)

def listl1pri(request):
    etudiants=Etudiant_Prive_Licence_Niveau1.objects.all()
    context = {
    'etudiants': etudiants
    }
    return render(request, 'Inscrire/listl2pu.html',context)

def listl2pri(request):
    etudiants=Etudiant_Prive_Licence_Niveau2.objects.all()
    context = {
    'etudiants': etudiants
    }
    return render(request, 'Inscrire/listl1pri.html',context)











def inscrirel2(request):
    return render(request, 'Inscrire/inscrirel2.html')



def detail(request):
    try:
        if request.method == 'POST':
        
            
            nom= request.POST.get('nom')
            photoEtudiant=request.POST.get('photoEtudiant')
            nni=request.POST.get('nni')
            sexe=request.POST.get('sexe')
            lieuNaissance=request.POST.get('lieuNaissance')
            dateNaissance=request.POST.get('dateNaissance')
            telephone=request.POST.get('telephone')
            preValid=int(telephone[:2])in prefixes
            sufValid=re.search(sufix,telephone[2:])
            email=request.POST.get('email')
            carteIdentite=request.POST.get('carteIdentite')
            numBac=request.POST.get('numBac')
            bac=request.POST.get('bac')
            releveNote=request.POST.get('releveNote')
            session=request.POST.get('session')
            moyen=request.POST.get('moyen')
            pays=request.POST.get('pays')
            annObBac=request.POST.get('annObBac')
            niveau=request.POST.get('niveau')
            filiere=request.POST.get('filiere')
            filiere=Filiere_Licence.objects.get(nom=filiere)
            if not preValid or not sufValid:
                return
            if niveau=='L1':
            

        
                orientation=Orientation.objects.filter(nni=nni)
                orientationnom=Orientation.objects.filter(nom=nom)
                orientationNaissance=Orientation.objects.filter(dateNaissance=dateNaissance)
                orientationLieu=Orientation.objects.filter(lieuNaissance=lieuNaissance)
                orientationSerie=Orientation.objects.filter(serie=bac)
                orientationmoyen=Orientation.objects.filter(moyenGeneral=moyen)
                etudiant = Etudiant_Public_Licence_Niveau1.objects.filter(nom=nom)
                if not etudiant.exists() and orientation.exists() and orientationnom.exists() and orientationNaissance.exists() and orientationLieu.exists() and orientationSerie.exists() and orientationmoyen.exists():
                    etudiant = Etudiant_Public_Licence_Niveau1.objects.create(
                    nom=nom,
                    nni=nni,
                    photoEtudiant=photoEtudiant,
                    sexe=sexe,
                    lieuNaissance=lieuNaissance,
                    dateNaissance=dateNaissance,
                    telephone=telephone,
                    email=email,
                    carteIdentite=carteIdentite,
                    numBac=numBac,
                    serie=bac,
                    releveNote=releveNote,
                    session=session, 
                    moyenGeneral=moyen,
                    pays=pays,
                    AnObtantionBac=annObBac,
                    filiere=filiere,
                    niveau=niveau
                            )
                    context = {
                        'numBac': numBac,
                        'nom':nom,
                        'niveau':niveau
                     }
                    return render(request, 'Inscrire/merci.html',context)
                return render(request, 'Inscrire/erreur.html')
        
            if niveau=='L2':

        
                orientation=Orientation.objects.filter(nni=nni)
                orientationnom=Orientation.objects.filter(nom=nom)
                orientationNaissance=Orientation.objects.filter(dateNaissance=dateNaissance)
                orientationLieu=Orientation.objects.filter(lieuNaissance=lieuNaissance)
                orientationSerie=Orientation.objects.filter(serie=bac)
                orientationmoyen=Orientation.objects.filter(moyenGeneral=moyen)
                etudiant = Etudiant_Public_Licence_Niveau2.objects.filter(nom=nom)
                if not etudiant.exists() and orientation.exists() and orientationnom.exists() and orientationNaissance.exists() and orientationLieu.exists() and orientationSerie.exists() and orientationmoyen.exists():
                    etudiant = Etudiant_Public_Licence_Niveau2.objects.create(
                    nom=nom,
                    nni=nni,
                    photoEtudiant=photoEtudiant,
                    sexe=sexe,
                    lieuNaissance=lieuNaissance,
                    dateNaissance=dateNaissance,
                    telephone=telephone,
                    email=email,
                    carteIdentite=carteIdentite,
                    numBac=numBac,
                    serie=bac,
                    releveNote=releveNote,
                    session=session, 
                    moyenGeneral=moyen,
                    pays=pays,
                    AnObtantionBac=annObBac,
                    filiere=filiere,
                    niveau=niveau
                            )
                    context = {
                        'numBac': numBac,
                        'nom':nom,
                        'niveau':niveau
                     }
                    return render(request, 'Inscrire/merci.html',context)
                return render(request, 'Inscrire/erreur.html')
            if niveau=='L3':

        
                orientation=Orientation.objects.filter(nni=nni)
                orientationnom=Orientation.objects.filter(nom=nom)
                orientationNaissance=Orientation.objects.filter(dateNaissance=dateNaissance)
                orientationLieu=Orientation.objects.filter(lieuNaissance=lieuNaissance)
                orientationSerie=Orientation.objects.filter(serie=bac)
                orientationmoyen=Orientation.objects.filter(moyenGeneral=moyen)
                etudiant = Etudiant_Public_Licence_Niveau3.objects.filter(nom=nom)
                if not etudiant.exists() and orientation.exists() and orientationnom.exists() and orientationNaissance.exists() and orientationLieu.exists() and orientationSerie.exists() and orientationmoyen.exists():
                    etudiant = Etudiant_Public_Licence_Niveau3.objects.create(
                    nom=nom,
                    nni=nni,
                    photoEtudiant=photoEtudiant,
                    sexe=sexe,
                    lieuNaissance=lieuNaissance,
                    dateNaissance=dateNaissance,
                    telephone=telephone,
                    email=email,
                    carteIdentite=carteIdentite,
                    numBac=numBac,
                    serie=bac,
                    releveNote=releveNote,
                    session=session, 
                    moyenGeneral=moyen,
                    pays=pays,
                    AnObtantionBac=annObBac,
                    filiere=filiere,
                    niveau=niveau
                            )
                    context = {
                        'numBac': numBac,
                        'nom':nom,
                        'niveau':niveau
                     }
                    return render(request, 'Inscrire/merci.html',context)
                return render(request, 'Inscrire/erreur.html')
            if niveau=='L1 privé':

        
                orientation=Orientation.objects.filter(nni=nni)
                orientationnom=Orientation.objects.filter(nom=nom)
                orientationNaissance=Orientation.objects.filter(dateNaissance=dateNaissance)
                orientationLieu=Orientation.objects.filter(lieuNaissance=lieuNaissance)
                orientationSerie=Orientation.objects.filter(serie=bac)
                orientationmoyen=Orientation.objects.filter(moyenGeneral=moyen)
                etudiant = Etudiant_Prive_Licence_Niveau1.objects.filter(nom=nom)
                if not etudiant.exists() and orientation.exists() and orientationnom.exists() and orientationNaissance.exists() and orientationLieu.exists() and orientationSerie.exists() and orientationmoyen.exists():
                    etudiant = Etudiant_Prive_Licence_Niveau1.objects.create(
                    nom=nom,
                    nni=nni,
                    photoEtudiant=photoEtudiant,
                    sexe=sexe,
                    lieuNaissance=lieuNaissance,
                    dateNaissance=dateNaissance,
                    telephone=telephone,
                    email=email,
                    carteIdentite=carteIdentite,
                    numBac=numBac,
                    serie=bac,
                    releveNote=releveNote,
                    session=session, 
                    moyenGeneral=moyen,
                    pays=pays,
                    AnObtantionBac=annObBac,
                    filiere=filiere,
                    niveau=niveau
                            )
                    context = {
                        'numBac': numBac,
                        'nom':nom,
                        'niveau':niveau
                     }
                    return render(request, 'Inscrire/merci.html',context)
                return render(request, 'Inscrire/erreur.html')
            if niveau=='L2 privé':

        
                orientation=Orientation.objects.filter(nni=nni)
                orientationnom=Orientation.objects.filter(nom=nom)
                orientationNaissance=Orientation.objects.filter(dateNaissance=dateNaissance)
                orientationLieu=Orientation.objects.filter(lieuNaissance=lieuNaissance)
                orientationSerie=Orientation.objects.filter(serie=bac)
                orientationmoyen=Orientation.objects.filter(moyenGeneral=moyen)
                etudiant = Etudiant_Prive_Licence_Niveau2.objects.filter(nom=nom)
                if not etudiant.exists() and orientation.exists() and orientationnom.exists() and orientationNaissance.exists() and orientationLieu.exists() and orientationSerie.exists() and orientationmoyen.exists():
                    etudiant = Etudiant_Prive_Licence_Niveau2.objects.create(
                    nom=nom,
                    nni=nni,
                    photoEtudiant=photoEtudiant,
                    sexe=sexe,
                    lieuNaissance=lieuNaissance,
                    dateNaissance=dateNaissance,
                    telephone=telephone,
                    email=email,
                    carteIdentite=carteIdentite,
                    numBac=numBac,
                    serie=bac,
                    releveNote=releveNote,
                    session=session, 
                    moyenGeneral=moyen,
                    pays=pays,
                    AnObtantionBac=annObBac,
                    filiere=filiere,
                    niveau=niveau
                            )
                    context = {
                        'numBac': numBac,
                        'nom':nom,
                        'niveau':niveau
                     }
                    return render(request, 'Inscrire/merci.html',context)
                return render(request, 'Inscrire/erreur.html')
            if niveau=='L3 privé':

        
                orientation=Orientation.objects.filter(nni=nni)
                orientationnom=Orientation.objects.filter(nom=nom)
                orientationNaissance=Orientation.objects.filter(dateNaissance=dateNaissance)
                orientationLieu=Orientation.objects.filter(lieuNaissance=lieuNaissance)
                orientationSerie=Orientation.objects.filter(serie=bac)
                orientationmoyen=Orientation.objects.filter(moyenGeneral=moyen)
                etudiant = Etudiant_Prive_Licence_Niveau3.objects.filter(nom=nom)
                if not etudiant.exists() and orientation.exists() and orientationnom.exists() and orientationNaissance.exists() and orientationLieu.exists() and orientationSerie.exists() and orientationmoyen.exists():
                    etudiant = Etudiant_Prive_Licence_Niveau3.objects.create(
                    nom=nom,
                    nni=nni,
                    photoEtudiant=photoEtudiant,
                    sexe=sexe,
                    lieuNaissance=lieuNaissance,
                    dateNaissance=dateNaissance,
                    telephone=telephone,
                    email=email,
                    carteIdentite=carteIdentite,
                    numBac=numBac,
                    serie=bac,
                    releveNote=releveNote,
                    session=session, 
                    moyenGeneral=moyen,
                    pays=pays,
                    AnObtantionBac=annObBac,
                    filiere=filiere,
                    niveau=niveau
                            )
                    context = {
                        'numBac': numBac,
                        'nom':nom,
                        'niveau':niveau
                     }
                    return render(request, 'Inscrire/merci.html',context)
                return render(request, 'Inscrire/erreur.html')
            if niveau=='M1':

        
                orientation=Orientation.objects.filter(nni=nni)
                orientationnom=Orientation.objects.filter(nom=nom)
                orientationNaissance=Orientation.objects.filter(dateNaissance=dateNaissance)
                orientationLieu=Orientation.objects.filter(lieuNaissance=lieuNaissance)
                orientationSerie=Orientation.objects.filter(serie=bac)
                orientationmoyen=Orientation.objects.filter(moyenGeneral=moyen)
                etudiant = Etudiant_Public_Master_Niveau1.objects.filter(nom=nom)
                if not etudiant.exists() and orientation.exists() and orientationnom.exists() and orientationNaissance.exists() and orientationLieu.exists() and orientationSerie.exists() and orientationmoyen.exists():
                    etudiant = Etudiant_Public_Master_Niveau1.objects.create(
                    nom=nom,
                    nni=nni,
                    photoEtudiant=photoEtudiant,
                    sexe=sexe,
                    lieuNaissance=lieuNaissance,
                    dateNaissance=dateNaissance,
                    telephone=telephone,
                    email=email,
                    carteIdentite=carteIdentite,
                    numBac=numBac,
                    serie=bac,
                    releveNote=releveNote,
                    session=session, 
                    moyenGeneral=moyen,
                    pays=pays,
                    AnObtantionBac=annObBac,
                    filiere=filiere,
                    niveau=niveau
                            )
                    context = {
                        'numBac': numBac,
                        'nom':nom,
                        'niveau':niveau
                     }
                    return render(request, 'Inscrire/merci.html',context)
                return render(request, 'Inscrire/erreur.html')
            if niveau=='M2':

        
                orientation=Orientation.objects.filter(nni=nni)
                orientationnom=Orientation.objects.filter(nom=nom)
                orientationNaissance=Orientation.objects.filter(dateNaissance=dateNaissance)
                orientationLieu=Orientation.objects.filter(lieuNaissance=lieuNaissance)
                orientationSerie=Orientation.objects.filter(serie=bac)
                orientationmoyen=Orientation.objects.filter(moyenGeneral=moyen)
                etudiant = Etudiant_Public_Master_Niveau2.objects.filter(nom=nom)
                if not etudiant.exists() and orientation.exists() and orientationnom.exists() and orientationNaissance.exists() and orientationLieu.exists() and orientationSerie.exists() and orientationmoyen.exists():
                    etudiant = Etudiant_Public_Master_Niveau2.objects.create(
                    nom=nom,
                    nni=nni,
                    photoEtudiant=photoEtudiant,
                    sexe=sexe,
                    lieuNaissance=lieuNaissance,
                    dateNaissance=dateNaissance,
                    telephone=telephone,
                    email=email,
                    carteIdentite=carteIdentite,
                    numBac=numBac,
                    serie=bac,
                    releveNote=releveNote,
                    session=session, 
                    moyenGeneral=moyen,
                    pays=pays,
                    AnObtantionBac=annObBac,
                    filiere=filiere,
                    niveau=niveau
                            )
                    context = {
                        'numBac': numBac,
                        'nom':nom,
                        'niveau':niveau
                     }
                    return render(request, 'Inscrire/merci.html',context)
                return render(request, 'Inscrire/erreur.html')
            else:      
                return render(request, 'Inscrire/erreur.html')
    except Exception as e:
        # raise e
        return render(request, 'Inscrire/erreur.html')

def licence(request):
    return render(request, 'Inscrire/licence.html')

def lppub(request):
    form= Etudiant_Licence_Public_L1Form()
    filieres=Filiere_Licence.objects.all()
    context = {
    'filieres': filieres,
    'form': form
    }
    return render(request, 'Inscrire/licencepubliclun.html',context)
def ldpub(request):
    filieres=Filiere_Licence.objects.all()
    form= Etudiant_Licence_Public_L1Form()
    context = {
    'filieres': filieres,
    'form': form
    }
    return render(request, 'Inscrire/licencepublicdeux.html',context)
def ltpub(request):
    filieres=Filiere_Licence.objects.all()
    form= Etudiant_Licence_Public_L1Form()
    context = {
    'filieres': filieres,
    'form': form
    }
    return render(request, 'Inscrire/licencepublicltrois.html',context)

def lpprb(request):
    filieres=Filiere_Licence.objects.all()
    form= Etudiant_Licence_Public_L1Form()
    context = {
    'filieres': filieres,
    'form':form
    }
    return render(request, 'Inscrire/LicencePremierNiveauPrivee.html',context)
def ldprb(request):
    filieres=Filiere_Licence.objects.all()
    form= Etudiant_Licence_Public_L1Form()
    context = {
    'filieres': filieres,
    'form':form
    }
    return render(request, 'Inscrire/LicenceDeuxiemeNiveauPrivee.html',context)



def master(request):
    return render(request, 'Inscrire/master.html')
def mppub(request):
    filieres=Filiere_Master.objects.all()
    form= Etudiant_Licence_Public_L1Form()
    context = {
    'filieres': filieres,
    'form':form
    }
    return render(request, 'Inscrire/masterpubliclun.html',context)
def Apropos(request):
    return render(request, 'Inscrire/Apropos.html')
       

def search(request):
    query = request.GET.get('query')
    if not query:
        etudiants = Etudiant_Prive_Licence_Niveau1.objects.filter(nom__icontains='AAAAAAAAAAAAAAAAAAAA')
    else:
        # title contains the query is and query is not sensitive to case.
        etudiants = Etudiant_Public_Licence_Niveau1.objects.filter(nni__icontains=query) or Etudiant_Public_Licence_Niveau2.object.filter(nni__icontains=query) or Etudiant_Public_Licence_Niveau3.object.filter(nni__icontains=query) or Etudiant_Prive_Licence_Niveau1.object.filter(nni__icontains=query) or Etudiant_Prive_Licence_Niveau2.object.filter(nni__icontains=query) or Etudiant_Prive_Licence_Niveau3.object.filter(nni__icontains=query) or Etudiant_Public_Master_Niveau1.object.filter(nni__icontains=query)or Etudiant_Public_Master_Niveau2.object.filter(nni__icontains=query)
    if not etudiants.exists():
       message=" "
    title = "Résultats pour la requête %s"%query
    context = {
        'etudiants': etudiants
        
    }
    return render(request, 'Inscrire/listingEtudiant.html', context)


def profile(request):
    return render(request, 'Inscrire/profile.html')
# def poster(request):
#     try:
#         if request.method == 'POST':
        
            
#             nom= request.POST.get('nom')
#             nni=request.POST.get('nni')
#             if not etudiant.exists() and orientation.exists() and orientationnom.exists() and orientationNaissance.exists() and orientationLieu.exists() and orientationSerie.exists() and orientationmoyen.exists():
#                     etudiant = Etudiant_Public_Licence_Niveau1.objects.create(
#                     nom=nom,
#                     nni=nni,
#     return render(request, 'Inscrire/profile.html')