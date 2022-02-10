# -*- coding:Utf8 -*-
#############################################
# Programme Python type
# auteur: G.T,Nt,2022
#############################################

#############################################
# Importation de fonction externes          :
import os.path
import time
import requests
from bs4 import BeautifulSoup
from math import ceil
from pathlib import Path
import csv
import os
#############################################

class Scraper(object):

    def __init__(self, url):
        self.url = url
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")

    def recuperer_urls_categories(self):
        "recuperation des urls des categories"
        self.urls_categories=[]
        for i in self.soup.find_all('a', href=True):
            self.urls_categories.append("https://books.toscrape.com/" + i['href'])
        return self.urls_categories[3:-41]

    def recuperer_urls_livres(self):
        "recuperation des urls des livres"
        self.urls_livres=[]
        chercher_balise_h3_html = self.soup("h3", text=True)  # soup("a") == soup.find_all("a")
        for i in chercher_balise_h3_html:
            chercher_url_livre = i.find("a")
            url_livre = chercher_url_livre["href"]
            self.urls_livres.append(
                "http://books.toscrape.com/catalogue/" + url_livre[9:])  # j'utilise le slicing pour supprimer les /./
        return self.urls_livres

    def recuperer_nombre_livres_max(self, new_url):
        "recuperation du nombre maximun de livre d'une categorie"
        self.url = new_url
        chercher_balise_strong_html= self.soup.find_all("strong")
        self.livres_max=chercher_balise_strong_html[1].text
        return self.livres_max

    def recuperer_titre_livre(self):
        "recuperation du titre du livre"
        self.titre_livre = self.soup.h1.get_text()
        return self.titre_livre

    def recuperer_categorie_livre(self):
        "recuperation de la categorie du livre"
        self.categorie_livre = self.soup.h1.get_text()
        return self.categorie_livre

    def recuperer_informations_livre(self):
        "recuperation des informations du livre"
        self.informations_livre=[]
        chercher_balise_td_html = (self.soup('td', text=True))
        for i in chercher_balise_td_html:
            self.informations_livre.append(i.get_text())
        return self.informations_livre

    def recuperer_description_livre(self):
        "recuperation de la description du livre"
        self.description_livre = self.soup("p")
        return self.description_livre[3].text

    def recuperer_note_livre(self):
        "recuperation de la note du livre"
        chercher_class_col_html = self.soup(class_="col-sm-6 product_main")
        liste_note_livre = ["none", "star-rating One", "star-rating Two",
                           "star-rating Three", "star-rating Four",
                           "star-rating Five"]
        for i in liste_note_livre:
            for j in chercher_class_col_html:
                chercher_note = (j.find(class_=i))
                if chercher_note:
                    self.note_livre = liste_note_livre.index(i)
                    return str(self.note_livre)

    def recuperer_urls_images(self):
        "recuperer les images des livres"
        self.images_urls = []
        for i in self.soup("img"):
            url_image = (i["src"])
            self.images_urls.append("http://books.toscrape.com" + url_image[5:])
        return self.images_urls[0]

    def changer_url(self, nouvelle_url):
        "changement d'url"
        self.url = nouvelle_url
        self.page = requests.get(nouvelle_url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")

    def changer_page(self, nouvelle_url):
        "calcul et creation des nouvelles url quand une categorie à plus de 20 livres"
        self.url = nouvelle_url
        self.iteration_url = []
        i = 2
        max_page = ceil(int(self.livres_max) / 20)
        while i <= max_page:
            h = nouvelle_url
            self.iteration_url.append(h[:-10] + "page-" + str(i) + ".html")
            i += 1
        return self.iteration_url


class Information(object):

    def __init__(self):
        self.path = os.getcwd()
        self.creer_sous_repertoire_p2 = "P2"
        self.creer_sous_repertoire_img = "Images"

    def creer_repertoire(self):
        "creation des repertoire pour les sauvegardes des informations"
        self.repertoire = os.path.join(self.path,self.creer_sous_repertoire_p2,
                                       self.creer_sous_repertoire_img)
        try:
            Path(self.repertoire).mkdir(parents=True, exist_ok=True)
        except FileExistsError:
            pass

    def enregistrer_imgages_livres(self, new_url):
        "enregistrement des images des livres"
        self.url = new_url
        self.page = requests.get(new_url)
        nom_image = new_url.split("/")[-1]
        self.sauvegarde_image = os.path.join(self.repertoire,nom_image)
        with open(self.sauvegarde_image, 'wb') as f:
            f.write(self.page.content)
        time.sleep(0.25)

    def creer_fichier_csv(self,nom_fichier):
        "creation d'un fichier csv"
        nom_fichier_csv=nom_fichier+".csv"
        self.fichier = os.path.join(self.creer_sous_repertoire_p2,nom_fichier_csv)
        with open(self.fichier, "a", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(("Titre", "Image", "Description", "Note",
                             "UPC", "Price (excl. tax)", "Price (incl. tax)",
                              "Availability"))

    def ecrire_information_livre(self, scraper,repertoire):
        "ecrire les information des livres dans le fichier correspondant à la bonne categorie"
        with open(self.fichier, "a", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow((scraper.recuperer_titre_livre(),
                             repertoire.sauvegarde_image,
                             scraper.recuperer_description_livre(),
                             scraper.recuperer_note_livre(),
                             scraper.recuperer_informations_livre()[0],
                             scraper.informations_livre[2],
                             scraper.informations_livre[3],
                             scraper.informations_livre[5]))
