from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from Inscrire.models import Arrchive, Departement, Etudiant, Etudiant_Prive_Licence_Niveau1, Etudiant_Prive_Licence_Niveau2, Etudiant_Prive_Licence_Niveau3, Etudiant_Prive_Master_Niveau1, Etudiant_Prive_Master_Niveau2, Etudiant_Public_Licence_Niveau1, Etudiant_Public_Licence_Niveau2, Etudiant_Public_Licence_Niveau3, Etudiant_Public_Master_Niveau1, Etudiant_Public_Master_Niveau2, Filiere_Licence, Filiere_Master, Orientation

# Register your models here.
admin.site.register(Departement)
admin.site.register(Arrchive)

@admin.register(Filiere_Licence)
class Filiere_LicenceAdmin(admin.ModelAdmin):
    search_fields = ['nom']

@admin.register(Filiere_Master)
class Filiere_MasterAdmin(admin.ModelAdmin):
    search_fields = ['nom']

@admin.register(Orientation)
class userdat(ImportExportModelAdmin):
    pass

@admin.register(Etudiant_Prive_Licence_Niveau1)
class Etudiant_Prive_Licence_Niveau1Admin(admin.ModelAdmin):
    search_fields = ['nom']
    
    
@admin.register(Etudiant_Prive_Licence_Niveau2)
class Etudiant_Prive_Licence_Niveau2Admin(admin.ModelAdmin):
    search_fields = ['nom']
@admin.register(Etudiant_Prive_Licence_Niveau3)
class Etudiant_Prive_Licence_Niveau3Admin(admin.ModelAdmin):
    search_fields = ['nom']

@admin.register(Etudiant_Public_Licence_Niveau1)
class Etudiant_Public_Licence_Niveau1Admin(admin.ModelAdmin):
    search_fields = ['nom']

@admin.register(Etudiant_Public_Licence_Niveau2)
class Etudiant_Public_Licence_Niveau2Admin(admin.ModelAdmin):
    search_fields = ['nom']
@admin.register(Etudiant_Public_Licence_Niveau3)
class Etudiant_Public_Licence_Niveau3Admin(admin.ModelAdmin):
    search_fields = ['nom']

@admin.register(Etudiant_Public_Master_Niveau1)
class Etudiant_Public_Master_Niveau1Admin(admin.ModelAdmin):
    search_fields = ['nom']
@admin.register(Etudiant_Public_Master_Niveau2)
class Etudiant_Public_Master_Niveau2Admin(admin.ModelAdmin):
    search_fields = ['nom']
    
@admin.register(Etudiant_Prive_Master_Niveau1)
class Etudiant_Prive_Master_Niveau1Admin(admin.ModelAdmin):
    search_fields = ['nom']
@admin.register(Etudiant_Prive_Master_Niveau2)
class Etudiant_Prive_Master_Niveau2Admin(admin.ModelAdmin):
    search_fields = ['nom']

    
admin.site.site_header = "ISCAE"
admin.site.site_title = "Partie admin"
admin.site.index_title = "Gestion d'insctiption"
