from django.db import models
from datetime import date,datetime

class Albergatore(models.Model):
    nome = models.CharField(max_length=50,default='')
    cognome = models.CharField(max_length=50,default='')
    email = models.EmailField(max_length=50,default='')
    password = models.CharField(max_length=32,default='')
class Indirizzo(models.Model):
    via = models.CharField(max_length=50,default='')
    numero = models.CharField(max_length=5,default='')

class Servizio(models.Model):
    nome = models.CharField(max_length=15,default='')
    descrizioneServizio = models.TextField(default='')

class Hotel(models.Model):
    nome = models.CharField(max_length=50,default='')
    descrizione = models.TextField(default='')
    citta = models.CharField(max_length=50,default='')
    indirizzo = models.ForeignKey(Indirizzo)
    proprietario = models.ForeignKey(Albergatore)

class Camera(models.Model):
    numero = models.CharField(max_length=15,default='')
    postiLetto = models.IntegerField(default=1)
    servizi = models.ForeignKey(Servizio)
    hotel = models.ForeignKey(Hotel)

class Prenotazione(models.Model):

    camera=models.ForeignKey(Camera)
    utente=models.CharField(max_length=50,default='')
    checkin=models.DateField(default=datetime.now())
    checkout=models.DateField(default=datetime.now())