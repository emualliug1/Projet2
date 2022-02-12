# -*- coding:Utf8 -*-
#############################################
# Programme Python type
# auteur: G.T,Nt,2022
#############################################

#############################################
# Importation de fonction externes          :
from pathlib import Path
import csv
import os
import os.path
from class_scraper import*
from constante import*
#############################################

class Information(object):

    def __init__(self):
        self.path = os.getcwd()
        self.creer_sous_repertoire_p2 = 'P2'
        self.creer_sous_repertoire_img = 'Images'

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
        nom_image = new_url.split('/')[-1]
        self.sauvegarde_image = os.path.join(self.repertoire,nom_image)
        with open(self.sauvegarde_image, 'wb') as f:
            f.write(self.page.content)
        time.sleep(0.25)

    def creer_fichier_csv(self,nom_fichier):
        "creation d'un fichier csv"
        nom_fichier_csv = nom_fichier+'.csv'
        self.fichier = os.path.join(self.creer_sous_repertoire_p2,nom_fichier_csv)
        with open(self.fichier, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(('product_page_url', 'universal_ product_code (upc)', 'title', 'price_including_tax',
                             'price_excluding_tax', 'number_available', 'product_description',
                              'review_rating','image_url'))

    def ecrire_information_livre(self, scraper,repertoire,url):
        "ecrire les information des livres dans le fichier correspondant à la bonne categorie"
        with open(self.fichier, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow((url,
                             scraper.recuperer_informations_livre()[UPC],
                             scraper.recuperer_titre_livre(),
                             scraper.informations_livre[PRICE_INCL_TAX],
                             scraper.informations_livre[PRICE_EXCL_TAX],
                             scraper.informations_livre[AVAILABILITY],
                             scraper.recuperer_description_livre(),
                             scraper.recuperer_note_livre(),
                             repertoire.sauvegarde_image))

















