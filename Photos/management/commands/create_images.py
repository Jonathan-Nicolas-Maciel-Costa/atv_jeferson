from django.core.management.base import BaseCommand
from django.utils.text import slugify
from faker import Faker
from ...models import Photo
import psycopg2
import requests

fake = Faker('en_US')

conn = psycopg2.connect(
    dbname="photograths",
    user="postgres",
    password="root",
    host="localhost",
    port=""
)
photo = conn.cursor()

qtd_images = 200000

class Command(BaseCommand):
    help = "create photos"
    
    def handle(self, *args, **kwargs):
        
        #gera as imagens 
        
        for _ in range(qtd_images):
            photo.execute("insert into \"Photos_photo\" (title, discription, photo, send_date, last_modified) values ('{}','{}','{}','{}','{}')".format(fake.name(), "photo taken in " + fake.address(), fake.image_url(width=600,placeholder_url="https://placewaifu.com/image/720"), fake.date_object(), fake.date_object()))
            
            teste = Photo.objects.create( title=fake.name(), 
                                          discription="photo taken in " + fake.address(), 
                                          photo=fake.image_url(width=600,placeholder_url="https://placewaifu.com/image/720"), 
                                          send_date=fake.date_object(), 
                                          last_modified=fake.date_object())
          
            
        
        print('ta certo meu nobre')

