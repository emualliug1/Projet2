# -*- coding:Utf8 -*-
#############################################
# Programme Python type
# auteur: G.T,Nt,2022
#############################################

#############################################
# Importation de fonction externes          :
import time
from tqdm import tqdm
#############################################
def lancer_programme(scraper,repertoire):
    start_time = time.time()
    for url0 in tqdm(scraper.recuperer_urls_categories(),desc="Chargement"):

        scraper.changer_url(url0)
        repertoire.creer_repertoire()
        repertoire.creer_fichier_csv(scraper.recuperer_categorie_livre())
        scraper.recuperer_nombre_livres_max(url0)
        scraper.changer_page(url0)

        for url1 in scraper.recuperer_urls_livres():
            scraper.changer_url(url1)
            repertoire.enregistrer_imgages_livres(scraper.recuperer_urls_images())
            repertoire.ecrire_information_livre(scraper,repertoire)

        if int(scraper.livres_max) > 20:

            for page in (scraper.iteration_url):
                scraper.changer_url(page)

                for url2 in scraper.recuperer_urls_livres():
                    scraper.changer_url(url2)
                    repertoire.enregistrer_imgages_livres(scraper.recuperer_urls_images())
                    repertoire.ecrire_information_livre(scraper,repertoire)


    print("--- %s seconds ---" % (round(time.time()) - round(start_time)))


