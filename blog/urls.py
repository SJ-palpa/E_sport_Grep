from django.urls import path
from django.contrib import admin

from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accueil', views.home, name="accueil"),
    path('connexion', views.connexion, name="connexion"),
    path('informationUtilisateur', views.informationUtilisateur, name="informationUtilisateur"),
    path('informationAdminEvenement', views.informationAdminEvenement, name="informationAdminEvenement"),
    path('listeEvenement', views.listeEvenement, name="listeEvenement"),
    path('creationEvenement', views.creationEvenement, name="creationEvenement"),
    path('creationAdminEvenement', views.creationAdminEvenement, name="creationAdminEvenement"),
    path('listeJoueur', views.listeJoueur, name="listeJoueur"),
    path('importerFichier', views.importerFichier, name="importerFichier"),
    path('modifierEvenement', views.modifierEvenement, name="modifierEvenement"),
    path('modificationUtilisateur', views.modificationUtilisateur, name="modificationUtilisateur"),
    path('modificationAdminEvenement', views.modificationAdminEvenement, name="modificationAdminEvenement"),
    path('modificationUtilisateurAdminSesf', views.modificationUtilisateurAdminSesf, name="modificationUtilisateurAdminSesf"),
    path('logCarte', views.logCarte, name="logCarte"),
]