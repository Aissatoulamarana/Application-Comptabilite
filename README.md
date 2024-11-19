# Application-Comptabilite
Ce projet est une application comptable développée avec Django REST Framework pour aider à gérer les opérations financières et les comptes de manière efficace. Ce guide vous aidera à cloner, installer et exécuter le projet sur votre machine locale.

Avant de commencer, assurez-vous d'avoir Python installé sur votre système 

Installation
1. Cloner le projet
Clonez ce dépôt Git sur votre machine locale : git clone https://github.com/Aissatoulamarana/Application-Comptabilite.git

2. Accéder au répertoire du projet
Déplacez-vous à la racine du projet : cd Application-Comptabilite

3. Créer un environnement virtuel
Créez un environnement virtuel pour isoler les dépendances : py -m venv venv

4. Activer l'environnement virtuel
Activez l'environnement virtuel :

Sur Windows : .\venv\Scripts\activate
Sur macOS/Linux : source venv/bin/activate

5. Installer les dépendances
Installez les bibliothèques nécessaires depuis le fichier requirements.txt : pip install -r requirements.txt

6. Exécution du Projet
    1. Assurez-vous que l'environnement virtuel est activé.
    2. Appliquez les migrations pour configurer la base de données:
        python manage.py migrate
    3. Lancez le serveur de développement : python manage.py runserver
    4. Accédez à l'application via votre navigateur à l'adresse : http://127.0.0.1:8000/


Structure du Projet
Voici un aperçu de l'organisation du projet :

Backend/ : Contient les fichiers backend de l'application.
venv/ : Répertoire de l'environnement virtuel (généré après l'installation).
requirements.txt : Liste des dépendances nécessaires.
manage.py : Point d'entrée principal de l'application Django.
