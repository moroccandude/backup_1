from sqlalchemy import create_engine, Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import sessionmaker
import pandas as pd
from model import Ville,Annonce,Equipement,AnnonceEquipement,Base
import os
from dotenv import load_dotenv

load_dotenv()
# import csv file(Data)
df = pd.read_csv('project_database/data/aa_output.csv', on_bad_lines='skip', sep=';').reset_index()
def connectTo_db():
   USER=os.getenv('USER')
   DB_NAME=os.getenv('POSTGRES_DB')
   PORT=os.getenv('PORT')
   HOST=os.getenv('HOST')
   DATABASE_URL = f"postgresql://postgres:{os.getenv('PASSWORD')}@{HOST}:{PORT}/{DB_NAME}"
   engine = create_engine(DATABASE_URL)
   return engine

def creation_table(engine):
#cree des tableaux qui exist au model.py
   Base.metadata.create_all(engine)

def insertation_des_tables(engine,df=df):
 # Configure the session to interact with the database
 Session = sessionmaker(bind=engine)
 session = Session()

 for index, row in df.iterrows():
    new_ville = Ville(name_ville=row['localisation'])
    session.add(new_ville)
    session.commit() 

    new_annonce = Annonce(
        titre=row['titre'],
        prix=row['prix'],
        chambres=row['chambres'],
        douches=row['douches'],
        surface=row['surface'],
        link=row['URL'],
        id_ville=new_ville.id_ville 
    )
    session.add(new_annonce)
    session.commit()  

    for equip_name in [
        "Chauffage central", "Lave-vaisselle", "Meuble", "Ascenseur", 
        "Double vitrage", "Isolation phonique", "Dressing", "Cave", "Grenier", "Four", 
        "Micro-ondes", "Hotte aspirante", "Plaque de cuisson", "Refrigerateur", "Congelateur", 
        "Box internet", "Systeme domotique", "Pre-installation pour climatisation reversible", 
        "Faux-plafond", "Revetement de sol industriel", "eclairage professionnel"
    ]:
        new_equipement = Equipement(name_equipement=equip_name)
        session.add(new_equipement)
        session.commit()  # save
        # Add association in AnnonceEquipement
        annonce_equipement = AnnonceEquipement(
            id_annonce=new_annonce.id_annonce,
            id_equipement=new_equipement.id_equipement
        )
        session.add(annonce_equipement)
        session.commit()
  
    session.close()

