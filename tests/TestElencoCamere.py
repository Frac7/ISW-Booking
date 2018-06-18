# Test di Accettazione per la Uesr Story Elenco Camera
from django.test import TestCase
from GestioneHotel.models import *
import unittest

class TestElencoCamere(TestCase):
    def setUp(self):
        #-------------------(IL VECCHIO CODICE, PRESENTE PRIMA CHE CI SCRIVA IO)--------------------
        # Creazione albergatore (nome, cognome, email, password
        # albergatore=Albergatore("Nome","Cognome","email","password")
        # hotel=Hotel("Hilton",albergaore)

        # listacamere = []
        #  servizi={"FB":"Frigo-bar","AC":"Aria Condizionata"}
        # camera1=Camera(hotel,1,servizi)
        # listacamere.append(self,camera)

        # servizi={"SK":"SKY","CF":"Cassaforte"}
        # camera2=Camera(hotel,2,servizi)
        # listacamere.append(self,camera)

        # assert listacamere[0]==camera1
        # assert listacamere[1] == camera2

        #--------------------(VA BENE?)--------------------------------------------------------------
        email = "user@email.com"
        password = "password"
        albergatore = Albergatore(nome="Pippo", cognome="Albergatore", email=email, password=password)
        albergatore.save()

        # Creazione indirizzi per gli hotel
        indirizzo1 = Indirizzo(via='Via Trieste', numero='14')
        indirizzo1.save()

        # Creazione degli Hotel e poi aggiunta alla lista
        hotel1 = Hotel(nome='Gold Hotel', descrizione='L\'Hotel piu\' adatto per la vostra permanenza e riposo.',
                           citta='Cagliari', indirizzo=indirizzo1, proprietario=albergatore)
        hotel1.save()

        # Creazione lista delle camere legate all'hotel dichiarato sopra
        listaCamere = []

        # Creazione servizi per i servizi disponibili
        servizio = Servizio(nome="TV", descrizioneServizio="televisione")
        servizio.save()

        # Creazione delle camere che verranno mostrate nella lista delle camere di un dato Hotel
        camera1 = Camera(numero=1, postiLetto=4, hotel=hotel1)
        camera1.save()
        listaCamere.append(camera1)
        camera2 = Camera(numero=2, postiLetto=3, hotel=hotel1)
        camera2.save()
        listaCamere.append(camera2)

        self.assertEqual(listaCamere[0], camera1, "Camera 1 e' presente nella lista")
        self.assertEqual(listaCamere[1], camera2, "Camera 2 e' presente nella lista")

    def testListaCamere(self):
        self.assertEqual(len(Camera.objects.all()), 2)

if __name__ == "__main__":
        unittest.main()