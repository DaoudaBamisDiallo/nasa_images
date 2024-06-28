# liste des librairie et package a installer
#-----------packages a installer-----------------------
'''
pip install python-dotenv
pip install pandas
pip install matplotlib
pip install pillow
pip install requests
pip install beautifulsoup4
(pip installe urllib ou urljoin)  pip install pycopy-urllib.parse
pip install scikit-image

'''
#--------------librairies------------

from dotenv import load_dotenv

import os 
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from skimage import transform,io,data
from skimage.io import imsave
import matplotlib.pyplot as plt
from PIL import Image,ImageTk
from io import BytesIO
import imageio
load_dotenv()
api_bamis=os.getenv('API_BAMIS')
#print(api_bamis)
