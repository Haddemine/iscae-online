from unicodedata import name
from django.urls import path
from .views import  ltpub, mppub,openfile,arrchive, profile, stat,Apropos,detail, listing, inscrirel2, licence, listingEtudiant, listl1pri, listl1pu, listl2pri, listl2pu,master,lpprb,ldprb,ldpub,lppub, search
app_name='Inscrire'

urlpatterns =[
    path('inscrire', listing,  name='listing'),
    path('listingEtudiant', listingEtudiant,  name='listingEtudiant'),
    path('stat',stat, name='stat'),

    path('listl1pu', listl1pu,  name='listl1pu'),
    path('listl2pu', listl2pu,  name='listl2pu'),
    path('listl1pri', listl1pri,  name='listl1pri'),
    path('listl2pri', listl2pri,  name='listl2pri'),

    path('arrchive',arrchive, name='arrchive'),
    path('openfile',openfile, name='openfile'),

    path('inscrirel2', inscrirel2, name='inscrire'),
    path('detail', detail, name='detail'),
    path('licence', licence, name='licence'),
    path('master', master, name='master'),
    path('lppub', lppub, name='lppub'),
    path('ldpub', ldpub, name='ldpub'),
    path('ltpub', ltpub, name='ltpub'),
    path('lpprb', lpprb, name='lpprb'),
    path('ldprb', ldprb, name='ldprb'),

    path('profile',profile,name='profile'),

    path('mppub',mppub, name='mppub'),
    path('search', search, name='search'),

    path('Apropos',Apropos,name='Apropos')


]
