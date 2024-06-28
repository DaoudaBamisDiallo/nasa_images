# liste des fonctions du programe
import configs as cf

API=cf.api_bamis
# fonction de l'imge du jour
def showing_day_image(API_KEY):
                
    with cf.requests.Session() as session:
            try:
               # lien de la page
                url="https://apod.nasa.gov/apod/astropix.html"
                # chemin d'enregistrement de l'image
                path="images/"
                # requete d'obtention des information du site
                response = session.get(url, params={'api_key':API_KEY})
                print(response.raise_for_status())
                
                # analyse du contenue de la requete
                soup = cf.BeautifulSoup(response.text,'html.parser')
                # recherche du lien de l'image
                link_img_day=soup.select_one('img').get('src')
                
                # creation du lien du telechargement de l'image
                path_img=cf.urljoin(url,link_img_day)
                
                # telechargement de li'image
                fileimage= session.get(path_img, params={'api_key':API_KEY})
                
                # creation du nom de l'image en le nom qui se trouve dans l'url
                paths=path+link_img_day.split('/')[2]
                
                # ouvertur et transformation en byte de l'image
                image = cf.Image.open(cf.BytesIO(fileimage.content))
                # enregistrement de l'image
                image.save(paths)
                # affichage de l'image
                cf.io.imshow(paths)
                cf.io.show()
                cf.plt.title('Image du jour de la nasa')
                print('succeful save image')
            except cf.requests.exceptions.HTTPError as errh:
                print ('HTTP error',errh)
       
#showing_day_image(API)


 # fonction de recherche de l'image en un date donnée
 # fonction d'affiche image en une date donnée
def search_image_date(API,date_day):
    with cf.requests.Session() as session:
            try:
                url= "https://api.nasa.gov/planetary/apod"
        
                #parametres de la requette
                
                params = {
                    'api_key':API ,
                    'date': date_day 
                    }
                url_image = session.get(url, params=params).json().get('url')
              
                name_image=url_image.split('/')[-1]
                
                file_image = session.get(url_image, params=params)
                image = cf.Image.open(cf.BytesIO(file_image.content))
            
                paths="images/"+name_image
                image.save(paths)
                #img=cf.io.imread(paths)
                cf.io.imshow(paths)
                cf.io.show()
                cf.plt.title(f"Image du {date_day}")
                
                print('succeful save image')
            except cf.requests.exceptions.HTTPError as errh:
                print ('HTTP error',errh)

#search_image_date(API,"2024-04-10")   

# recherche des astroide de la nasa
def get_all_astroides(API_KEY,start_date,end_date):
             
    with cf.requests.Session() as session:   
        url="https://api.nasa.gov/neo/rest/v1/feed"
        parameters= {
            'api_key': API_KEY,
            'start_date': start_date,  
            'end_date': end_date
            }
        response = session.get(url, params=parameters)
        astroides=response.json()
        
        all_astroides={"id_astroides":[],
                       "name":[],
                       "magnitude_absolue":[],
                       "diametre_min":[],
                       "vitesse_relatives(km/s)":[]
                      }
        for dates in astroides.get('near_earth_objects').keys():
            n_astroid=0
            for astroide in astroides.get('near_earth_objects')[dates]:
                n_astroid +=1
                all_astroides.get("id_astroides").append(astroide.get('id'))
                all_astroides.get("name").append(astroide.get('name'))
                all_astroides.get("magnitude_absolue").append(astroide.get('absolute_magnitude_h'))
                all_astroides.get("diametre_min").append(astroide.get('estimated_diameter').get('kilometers').get('estimated_diameter_min'))
                all_astroides.get("vitesse_relatives(km/s)").append(astroide.get('close_approach_data')[0].get('relative_velocity').get('kilometers_per_second'))
                print("N°: ",n_astroid)
                print(f" id : {astroide.get('id')} \n nom : {astroide.get('name')} \n magnitude absolue:  {astroide.get('absolute_magnitude_h')}")
                print('diameter_min :',astroide.get('estimated_diameter').get('kilometers').get('estimated_diameter_min'),'Km')
                print('Vitesse relatives :',astroide.get('close_approach_data')[0].get('relative_velocity').get('kilometers_per_second'),'Km/s')
                print('**'*50) 
                data=cf.pd.DataFrame(all_astroides)
                data.to_csv('astroides_dataset.csv')
                
        return data
#get_all_astroides(API,'2024-06-20','2024-06-25')


def get_data_astroides():
     data=cf.pd.read_csv('astroides_dataset.csv')
     print(data)
#get_data_astroides()