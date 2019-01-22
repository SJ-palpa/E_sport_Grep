from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'blog/accueil.html')


def connexion(request):
    return render(request, 'blog/connexion.html')

def informationUtilisateur(request):
    return render(request, 'blog/utilisateur/informationUtilisateur.html')


def informationAdminEvenement(request):
    return render(request, 'blog/adminEvenement/informationAdminEvenement.html')


def listeEvenement(request):
    return render(request, 'blog/adminEvenement/listeEvenement.html')


def creationEvenement(request):
    return render(request, 'blog/adminEvenement/creationEvenement.html')


def creationAdminEvenement(request):
    return render(request, 'blog/adminSESF/creationAdminEvenement.html')


def listeJoueur(request):
    return render(request, 'blog/adminSESF/listeJoueur.html')


def importerFichier(request):
    return render(request, 'blog/adminEvenement/evenement/importerFichier.html')


def modifierEvenement(request):
    return render(request, 'blog/adminEvenement/evenement/modifierEvenement.html')


def modificationUtilisateur(request):
    return render(request, 'blog/utilisateur/modificationUtilisateur.html')


def modificationAdminEvenement(request):
    return render(request, 'blog/adminEvenement/modificationAdminEvenement.html')


def modificationUtilisateurAdminSesf(request):
    return render(request, 'blog/adminSESF/gestionUtilisateur/modificationUtilisateur.html')

def logCarte(request):
    return render(request, 'blog/adminSESF/logCarte.html')



