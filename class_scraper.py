# -*- coding:Utf8 -*-
#############################################
# Programme Python type
# auteur: G.T,Nt,2022
#############################################

#############################################
# Importation de fonction externes          :
import requests
from bs4 import BeautifulSoup
from math import ceil
from constante import*
#############################################

class Scraper(object):

    def __init__(self, url):
        self.url = url
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")

    def recuperer_urls_categories(self):
        "recuperation des urls des categories"
        self.urls_categories=[]
        for i in self.soup.find_all("a", href=True):
            self.urls_categories.append(URL_MAITRE + i['href'])
        return self.urls_categories[URLS_CATEGORIE_DEBUT:URLS_CATEGORIE_FIN]

    def recuperer_urls_livres(self):
        "recuperation des urls des livres"
        self.urls_livres=[]
        chercher_balise_h3_html = self.soup("h3", text=True)  # soup("a") == soup.find_all("a")
        for i in chercher_balise_h3_html:
            chercher_url_livre = i.find("a")
            url_livre = chercher_url_livre["href"]
            self.urls_livres.append(
                URL_LIVRE + url_livre[URLS_LIVRE_DEBUT:])  # j'utilise le slicing pour supprimer les /./
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
        return self.description_livre[DESCRIPTION_LIVRE].text

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
            self.images_urls.append("http://books.toscrape.com" + url_image[URL_IMAGE_DEBUT:])
        return self.images_urls[URL_IMAGE_FIN]

    def changer_url(self, nouvelle_url):
        "changement d'url"
        self.url = nouvelle_url
        self.page = requests.get(nouvelle_url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")

    def changer_page(self, nouvelle_url):
        "calcul et creation des nouvelles url quand une categorie à plus de 20 livres"
        self.url = nouvelle_url
        self.iteration_url = []
        debut_iteration = DEBUT_ITERATION
        max_page = ceil(int(self.livres_max) / MAX_LIVRES_PAR_URLS)
        while debut_iteration <= max_page:
            h = nouvelle_url
            self.iteration_url.append(h[:-10] + "page-" + str(debut_iteration) + ".html")
            debut_iteration += 1
        return self.iteration_url


