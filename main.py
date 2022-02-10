# -*- coding:Utf8 -*-
#############################################
# Programme Python type
# auteur: G.T,Nt,2022
#############################################

#############################################
# Importation de fonction externes          :
from fonctionp2 import*
from classp2 import*
##############################################
## Programme principal :                    ##
##############################################
smaitre = Scraper("https://books.toscrape.com/") #initialisation du scraper avec l'adresse du site
r1 = Information()                               #initialisation de la class informmation
lancer_programme(smaitre,r1)                     #lancement du scraping avec enregistrement des donnees + photos




