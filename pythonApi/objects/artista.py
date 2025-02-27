import json
import pyodbc
import db.sql as sql
from ytmusicapi import YTMusic
import os

# Python no soporta por defecto rutas relativas, con la librería OS se puede conseguir el efecto
directorioActual = os.path.dirname(__file__)
rutaArtistas = os.path.join(directorioActual, '../data/artistas.json')

ytmusic = YTMusic('headers_auth.json')

class Artista(object):
    id = ""
    nombre = ""
    imagen_url = ""
    descripcion = ""
    generos = ""
    relevancia = ""

    # The class "constructor" - It's actually an initializer 
    def __init__(self, id, nombre, imagen_url, descripcion, generos, relevancia):
        self.id = id
        self.nombre = nombre
        self.imagen_url = imagen_url
        self.descripcion = descripcion
        self.generos = generos
        self.relevancia = relevancia



def crear_artistas():
    # Opening JSON file
    jsonController = open(rutaArtistas)
    
    # returns JSON object as
    # a dictionary
    data = json.load(jsonController)
    print(len(data))
    #YTMUSIC READ INFO
    for info in data:
        artista_id = info["id"]
        artistaDict = ytmusic.get_artist(artista_id)
        url = artistaDict["thumbnails"][len(artistaDict["thumbnails"])-1]["url"]
        artist = Artista(artista_id, info["nombre"], url, artistaDict["description"], info["generos"], info["relevancia"])
        sql.insertar_artista(artist)
    jsonController.close()