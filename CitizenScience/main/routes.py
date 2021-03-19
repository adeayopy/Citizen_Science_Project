import os
import re
import secrets
import random
from PIL import Image
from flask import Blueprint, render_template, url_for, request, redirect 
from CitizenScience import app, db
from CitizenScience.models import Picture
from CitizenScience.main.forms import VerifyForm


main=Blueprint('main', __name__)


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
@main.route('/', methods=['POST', 'GET']) 
@main.route('/home', methods=['POST', 'GET'])
def home(): 
    forms=VerifyForm()  
    # Use only save_picture function when loading a new set of pictures... I will fix this later
    # save_picture()

   
    if request.method=='GET':
        global select_two_images
        select_two_images=random_two()
       
    elif request.method=='POST':
        #name1=request.form.getvalue('image_file[0]')
        selected_option=request.form.get('image_file')
     
        print(selected_option)
        selected_rank=re.findall('\s\'([0-9]+)',selected_option)
        print(selected_rank)
        selected_rank=''.join(map(str,selected_rank))

        print(select_two_images)
        presented_options=re.findall('\s\'([0-9]+)',str(select_two_images))
        print(presented_options)

        if int(min(presented_options)) < int(selected_rank):
            change_to_lower=Picture.query.filter_by(rank=int(selected_rank))
            change_to_lower.rank=int(min(presented_options))

            change_to_higher=Picture.query.filter_by(rank=int(min(presented_options)))
            change_to_higher.rank=int(max(presented_options))
            db.session.commit() 
        return redirect(url_for('main.submit'))      
    
   
    return render_template('home.html', image_file=select_two_images, form=forms)

# 

@main.route('/submit')
def submit():
    return render_template('submit.html') 