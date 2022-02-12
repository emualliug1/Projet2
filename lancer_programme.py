# -*- coding:Utf8 -*-
#############################################
# Programme Python type
# auteur: G.T,Nt,2022
#############################################

#############################################
# Importation de fonction externes          :
import time
from tqdm import tqdm
from constante import*
#############################################
def lancer_programme(scraper,repertoire):
    "lancement du programme scraper"

    TEMPS_LANCEMENT_PROGRAMME_DEBUT = time.time()

    for url0 in tqdm(scraper.recuperer_urls_categories(),desc='Chargement'):

        scraper.changer_url(url0)
        repertoire.creer_repertoire()
        repertoire.creer_fichier_csv(scraper.recuperer_categorie_livre())
        scraper.recuperer_nombre_livres_max(url0)
        scraper.changer_page(url0)

        for url1 in scraper.recuperer_urls_livres():
            scraper.changer_url(url1)
            repertoire.enregistrer_imgages_livres(scraper.recuperer_urls_images())
            repertoire.ecrire_information_livre(scraper, repertoire,url1)

        if int(scraper.livres_max) > MAX_LIVRES_PAR_URLS:

            for url2 in (scraper.iteration_url):
                scraper.changer_url(url2)

                for url3 in scraper.recuperer_urls_livres():
                    scraper.changer_url(url3)
                    repertoire.enregistrer_imgages_livres(scraper.recuperer_urls_images())
                    repertoire.ecrire_information_livre(scraper, repertoire,url3)
    print('--- %s seconds ---' % (round(time.time()) - round(TEMPS_LANCEMENT_PROGRAMME_DEBUT)))





