from django.urls import path
from apis.views import DetailEtudiant_Prive_Licence_Niveau1, DetailEtudiant_Prive_Licence_Niveau2, DetailEtudiant_Prive_Licence_Niveau3, DetailEtudiant_Prive_Master_Niveau1, DetailEtudiant_Prive_Master_Niveau2, DetailEtudiant_Public_Licence_Niveau1, DetailEtudiant_Public_Licence_Niveau2, DetailEtudiant_Public_Licence_Niveau3, DetailEtudiant_Public_Master_Niveau1, DetailEtudiant_Public_Master_Niveau2, DetailFilier_Licence, ListEtudiant_Prive_Licence_Niveau1, ListEtudiant_Prive_Licence_Niveau2, ListEtudiant_Prive_Licence_Niveau3, ListEtudiant_Prive_Master_Niveau1, ListEtudiant_Prive_Master_Niveau2, ListEtudiant_Public_Licence_Niveau1, ListEtudiant_Public_Licence_Niveau2, ListEtudiant_Public_Licence_Niveau3, ListEtudiant_Public_Master_Niveau1, ListEtudiant_Public_Master_Niveau2, ListFilier_Licence

app_name='apis'
urlpatterns=[
    path('filierlicence',ListFilier_Licence.as_view(), name='listfilierlicence'),
    path('filierlicence/<int:pk>/',DetailFilier_Licence.as_view()),
    path('listlunpublic',ListEtudiant_Public_Licence_Niveau1.as_view(), name='ListEtudiant_Public_Licence_Niveau1'),
    path('listlunpublic/<int:pk>/',DetailEtudiant_Public_Licence_Niveau1.as_view()),
    path('listldpublic',ListEtudiant_Public_Licence_Niveau2.as_view(), name='ListEtudiant_Public_Licence_Niveau2'),
    path('listldpublic/<int:pk>/',DetailEtudiant_Public_Licence_Niveau2.as_view()),
    path('listltpublic',ListEtudiant_Public_Licence_Niveau3.as_view(), name='ListEtudiant_Public_Licence_Niveau3'),
    path('listltpublic/<int:pk>/',DetailEtudiant_Public_Licence_Niveau3.as_view()),
    path('listlunprive',ListEtudiant_Prive_Licence_Niveau1.as_view(), name='ListEtudiant_Prive_Licence_Niveau1'),
    path('listlunprive/<int:pk>/',DetailEtudiant_Prive_Licence_Niveau1.as_view()),
    path('listldprive',ListEtudiant_Prive_Licence_Niveau2.as_view(), name='ListEtudiant_Prive_Licence_Niveau2'),
    path('listldprive/<int:pk>/',DetailEtudiant_Prive_Licence_Niveau2.as_view()),
    path('listltprive',ListEtudiant_Prive_Licence_Niveau3.as_view(), name='ListEtudiant_Prive_Licence_Niveau3'),
    path('listltprive/<int:pk>/',DetailEtudiant_Prive_Licence_Niveau3.as_view()),
    path('listmunpublic',ListEtudiant_Public_Master_Niveau1.as_view(), name='ListEtudiant_Public_Master_Niveau1'),
    path('listmunpublic/<int:pk>/',DetailEtudiant_Public_Master_Niveau1.as_view()),
    path('listmdpublic',ListEtudiant_Public_Master_Niveau2.as_view(), name='ListEtudiant_Public_Master_Niveau2'),
    path('listmdpublic/<int:pk>/',DetailEtudiant_Public_Master_Niveau2.as_view()),
    path('listmunprive',ListEtudiant_Prive_Master_Niveau1.as_view(), name='ListEtudiant_Prive_Master_Niveau1'),
    path('listmunprive/<int:pk>/',DetailEtudiant_Prive_Master_Niveau1.as_view()),
    path('listmdprive',ListEtudiant_Prive_Master_Niveau2.as_view(), name='ListEtudiant_Prive_Master_Niveau2'),
    path('listmdprive/<int:pk>/',DetailEtudiant_Prive_Master_Niveau2.as_view()),
]       