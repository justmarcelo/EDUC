EDUC - Plateforme d'orientation scolaire
 pour le Congo
 EDUC est une application web qui permet aux étudiants de s'inscrire, de déposer des
 vœux pour des formations et de suivre leurs candidatures, à l'image de Parcoursup,
 mais adaptée au contexte du Congo.
 Fonctionnalités principales
 Inscription et connexion d'utilisateur 
Dépôt de vœux pour des formations 
Suivi de l'état de ses candidatures 
Interface simple et responsive 
Pour tester le projet sur Windows ou Mac
     1.  
Installer Python (version 3.8 ou plus)
 Si Python n'est pas installé, télécharge-le sur python.org 
     2.  
Ouvrir un terminal ou PowerShell dans le dossier du projet 
     3.  
Créer un environnement virtuel
 Windows : python -m venv venv
 Mac/Linux : python3 -m venv venv 
     4.  
Activer l'environnement virtuel
 Windows : venv\Scripts\activate
 Mac/Linux : source venv/bin/activate 
     5.  
Installer les dépendances
 pip install -r requirements.txt 
     6.  
Initialiser la base de données
 python manage.py migrate 
     7.  
(Optionnel) Créer un superutilisateur pour l'administration
 python manage.py createsuperuser 
     8.  
Lancer le serveur de développement
 python manage.py runserver 
     9.  
Ouvrir le site dans le navigateur
 Aller sur http://127.0.0.1:8000/ 
Accès à l'administration
 Si tu as créé un superutilisateur, tu peux accéder à l'administration via
 http://127.0.0.1:8000/admin
 Remarques importantes
 Ne pas supprimer le dossier venv/, mais ne pas l'envoyer sur GitHub. 
Le fichier db.sqlite3 contient la base de données locale (pour les tests). 
Si tu veux réinitialiser la base, supprime db.sqlite3 puis relance python
 manage.py migrate. 
