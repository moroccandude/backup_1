from sqlalchemy import create_engine, Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship,declarative_base
import pandas as pd


#  Base class, SQLAlchemy can automatically map your class to a database table. 
Base = declarative_base()

# Define the Ville class for the "ville" table
class Ville(Base):
    __tablename__ = 'ville'
    
    id_ville = Column(Integer, primary_key=True, autoincrement=True)
    name_ville = Column(Text, nullable=False)
    
    # Relationship to Annonce
    annonces = relationship("Annonce", back_populates="ville")

# Define the Annonce class for the "annonce" table
class Annonce(Base):
    __tablename__ = 'annonce'
    
    id_annonce = Column(Integer, primary_key=True, autoincrement=True)
    titre = Column(String(50), nullable=True)
    prix = Column(Float, nullable=True)
    chambres = Column(Integer, nullable=True)
    douches = Column(Integer, nullable=True)
    surface = Column(Float, nullable=True)
    link = Column(Text, nullable=True)
    
    id_ville = Column(Integer, ForeignKey('ville.id_ville'))
    
  
    ville = relationship("Ville", back_populates="annonces")
    annonce_equipements = relationship("AnnonceEquipement", back_populates="annonce")

class Equipement(Base):
    __tablename__ = 'equipement'
    
    id_equipement = Column(Integer, primary_key=True, autoincrement=True)
    name_equipement = Column(Text, nullable=True)
    
    
    annonce_equipements = relationship("AnnonceEquipement", back_populates="equipement")

class AnnonceEquipement(Base):
    __tablename__ = 'annonce_equipements'
    
    id_annonce = Column(Integer, ForeignKey('annonce.id_annonce'), primary_key=True)
    id_equipement = Column(Integer, ForeignKey('equipement.id_equipement'), primary_key=True)
    
    
    annonce = relationship("Annonce", back_populates="annonce_equipements")
    equipement = relationship("Equipement", back_populates="annonce_equipements")


