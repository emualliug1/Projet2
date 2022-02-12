Programme de scraping du site:
https://books.toscrape.com

Une application pour récupérer les données suivantes au moment de l'exécution:
 - URL de la page produit
 - code produit universel (upc)
 - Titre
 - prix TTC
 - prix hors taxe
 - numéro disponible
 - Description du produit
 - note du livre
 - image du livre


Pour Commencer:

Assurez-vous que python3 est installé sur votre machine: 

`python -V`

Vérifiez que vous disposez du module venv: 

`python -m venv --help`


Si Python n'est pas installé sur votre machine :

https://www.python.org/downloads/
 

une fois Python installé:

1.ouvrir une invite de commande et utiliser la commande: 

`cd` pour aller dans le repertoire ou vous voulez copier le projet.
vous pouvez aussi creer un nouveau repertoire avec la commande: `mkdir`

2.une fois dans le bon repertoire il vous suffit de taper:
`git clone ***url du projet github***`

3.Créer un environnement virtuel avec `venv`:
`python -m venv ***nom de l'environnement***` : pour créer l'environnement virtuel - exemple : `py -m venv env`

4.Activez l'environnement virtuel:
`***nom de l'environnement***/Scripts/activate.bat` - ex: `env/Scripts/activate.bat`

5.Installez les packages avec pip: `pip install -r requirements.txt`

6.Lancez le programme avec : `python3 main.py`


a la fin du chargement:

- un repertoire P2 contient 50 fichiers csv avec le nom de la catégorie de livre sur chaque fichier contenant les données de chaque livre sous cette catégorie.

- un repertoire images qui contient les 1000 images des livres.
