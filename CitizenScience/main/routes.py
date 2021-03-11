import os
import secrets
from PIL import Image
from flask import Blueprint, render_template, url_for 
from CitizenScience import app, db
from CitizenScience.models import Picture


main=Blueprint('main', __name__)

#This route reduces the size of picture files, copy them into another folder and display on webpage 
@main.route('/home')
def home():   
    # Accessing one of the pictures 
    picture='S1_f1_nw.jpg'
    count=1
    # Picture on filesystem
    image_folder=os.path.join(app.root_path,'static/weed_rank_images/',picture)
    #New folder to save reduced file
    picture_path=os.path.join(app.root_path,'static/new_weed_images/', picture)
    output_size=(500,500)
    i=Image.open(image_folder)
    i.thumbnail(output_size, Image.ANTIALIAS)
    i.save(picture_path)
    store=Picture(name=picture, rank=count)
    #Storing picture information in database
    db.session.add(store)
    db.session.commit()
    
    #Getting information from database
    image_file=Picture.query.first()
    
    return render_template('home.html', image_file=image_file)


