import os
import secrets
import random
from PIL import Image
from flask import Blueprint, render_template, url_for 
from CitizenScience import app, db
from CitizenScience.models import Picture


main=Blueprint('main', __name__)

import os
from PIL import Image


#Use function once....I will get a way to sync

# def save_picture():
#     # Accessing one of the pictures 
#     image_folder=os.path.join(app.root_path, "static/weed_rank_images/")
#     count=0
#     for picture in os.listdir(image_folder):
#         count+=1
#         # Picture on filesystem       
#         #New folder to save reduced file
#         new_picture_path=os.path.join(app.root_path,'static/new_weed_images/')
#         output_size=(500,500)
#         i=Image.open(image_folder+'\\'+picture)
#         i.thumbnail(output_size, Image.ANTIALIAS)
#         i.save(new_picture_path+'\\'+picture)
#         store_pictures=Picture(name=picture, rank=count)
#         #Storing picture information in database
#         db.session.add(store_pictures)
#         db.session.commit()

# Function to randomise and return 2 distinct pictures
def random_two():
    img=[]
    for picture in range(2):
        picture_q=random.choice(Picture.query.all())
        img.append(picture_q)
    if img[0]==img[1]:
        random_two()
    return img


#This route reduces the size of picture files, copy them into another folder and display on webpage
@main.route('/') 
@main.route('/home')
def home():   
    # Use only save_picture function when loading a new set of pictures... I will fix this later
    # save_picture()
    select_two_image=random_two()
    return render_template('home.html', image_file=select_two_image)
