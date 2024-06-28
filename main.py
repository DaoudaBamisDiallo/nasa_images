# programme principale du projet
#-------------------importation du fichier utils-----------
import utils as ut
API_KEY=ut.API
# recherche des astroides de la nasa
print("-------------Bienvenu voici l'image du jour--------------\n")
ut.showing_day_image(ut.API)
choix=1
while choix > 0:
    choix=int(input('-------------Menu--------------\n 1: Image du jour \n 2: Rechercher une image \n 3: Info astroides \n 4 : Données astroides \n 0 : Quitter \n'))

    try:
        # image du jour
        if choix==1:
            
            ut.showing_day_image(API_KEY)
        # recherche image en une date
        elif choix==2:
            dates_image=input('Donner une date (aaa-mm-jj)')
            ut.search_image_date(API_KEY,dates_image) 
        #Information des astroides a une intervalle de dates debut et fin

        elif choix==3:
            # saisie des dates
            start_date=input('Donner une date de debut (aaa-mm-jj)') 
            end_date=input('Donner une date de fin (aaa-mm-jj)')
            
            df=ut.get_all_astroides(API_KEY,start_date,end_date)
            # dataframe des astroides
        elif choix==4:
            ut.get_data_astroides() 
        else:
            print('Choix invalide')
    except ut.cf.requests.exceptions.HTTPError as errh:
            print ('HTTP error',errh)

