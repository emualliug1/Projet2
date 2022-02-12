# -*- coding:Utf8 -*-
#############################################
# Programme Python type
# auteur: G.T,Nt,2022
#############################################

#############################################
# Importation de fonction externes          :
from lancer_programme import*
from class_information import*
from constante import*
##############################################
## Programme principal :                    ##
##############################################
smaitre = Scraper(URL_MAITRE) #initialisation du scraper avec l'adresse du site
r1 = Information()                               #initialisation de la class informmation
lancer_programme(smaitre,r1)                     #lancement du scraping avec enregistrement des donnees + photos




