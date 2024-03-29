from django import forms
from django.forms import Field

from GestioneHotel.models import *

from django.contrib.auth.forms import UserCreationForm


# Collegato alla view signup
class SignUpForm(UserCreationForm):
    username = forms.EmailField(label="Email", max_length=254, help_text='Obbligatorio. inserire un indirizzo email valido.')
    nome = forms.CharField(max_length=50, help_text='Obbligatorio.')
    cognome = forms.CharField(max_length=50, help_text='Obbligatorio.')

    class Meta:
        model = Albergatore
        fields = ('username', 'nome', 'cognome', 'password1', 'password2', )


#Collegato alla view aggiungiCamera
class AggiungiCameraForm(forms.Form):
    #Campo numero camera
    numero = forms.CharField(label="Numero",max_length=15,required=True,widget=forms.TextInput(attrs={'id': 'campoCamera'}))
    #Posti camera: da 1 a 6
    elencoPosti = [(i, i) for i in range(1, 7)]
    postiLetto = forms.ChoiceField(label="Posti Letto", choices=elencoPosti, widget=forms.Select(attrs={'id' : 'postiCamera'}))

    #Generazione dinamica servizi disponibili in base a quelli presenti nel db
    def __init__(self, *args, **kwargs):
        super(AggiungiCameraForm, self).__init__(*args, **kwargs)
        for servizio in Servizio.objects.all():
            self.fields[servizio.nome] = forms.BooleanField(required=False,label=servizio.nome + ", " + servizio.descrizioneServizio,widget=forms.CheckboxInput(attrs={'id': 'servizioCamera'}))
#Form login
class LoginForm(forms.Form):
    #Campo email
    email = forms.EmailField(label="Email",required=True, widget=forms.TextInput(attrs={'id' : 'accediLogin'}))
    #Campo passowrd
    password = forms.CharField(label="Password",required=True,widget=forms.PasswordInput(attrs={'id' : 'accediPassword'}))

class AggiungiHotelForm(forms.Form):
     nome = forms.CharField(label="Nome", max_length=30, required=True,
                               widget=forms.TextInput(attrs={'id': 'nomeHotel'}))
     descrizione = forms.CharField(label='Descrizione', max_length=100, required=True,
                                      widget=forms.TextInput(attrs={'id': 'descrizioneHotel'}))
     citta = forms.CharField(label='Citta', max_length=30, required=True,
                                widget=forms.TextInput(attrs={'id': 'cittaHotel'}))
     via = forms.CharField(label='Via', max_length=50, required=True,
                              widget=forms.TextInput(attrs={'id': 'viaHotel'}))
     numeroCivico = forms.CharField(label='NumeroCivico', max_length=10, required=True,
                                       widget=forms.TextInput(attrs={'id': 'numeroHotel'}))

class FormRicerca(forms.Form):

    #recupero l'elenco delle citta dagli hotel
    elencoCitta = [(hotel.citta, hotel.citta) for hotel in Hotel.objects.order_by('citta')]
    if len(elencoCitta)>0:
        # elimino i duplicati dalla lista
        elencoCitta = list(set(elencoCitta))
        #ordino la lista
        elencoCitta.sort()
        # html select della citta dell'elenco delle citta disponibili
        citta=forms.ChoiceField(label="Destinazione", widget=forms.Select(attrs={'id':'ricercaCitta'}), choices=elencoCitta, required=False)
    else:
        citta = forms.CharField(widget=forms.TextInput(attrs={'id':'ricercaCitta'}))
    # input data arrivo
    dataArrivo = forms.DateField(label="Arrivo",widget=forms.SelectDateWidget(attrs={'id':'ricercaDataIn'}))
    #input data partenza
    dataPartenza = forms.DateField(label="Partenza",widget=forms.SelectDateWidget(attrs={'id':'ricercaDataOut'}))
    elencoPosti=[(i,i) for i in range(1, 7)]
    posti = forms.ChoiceField(label="Posti",choices=elencoPosti, widget=forms.Select(attrs={'id':'ricercaPostiLetto'}))

class FormPrenota(forms.Form):
    # input dell'indirizzo Email dell'utente che effettua la prenotazione
    prenotaUtente = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'id':'prenotaUtente'}))
    prenotaCheckin = forms.CharField(widget=forms.HiddenInput(attrs={'id':'prenotaDataIn'}))
    prenotaCheckout = forms.CharField(widget=forms.HiddenInput(attrs={'id':'prenotaDataOut'}))
    prenotaIdCamera = forms.CharField(widget=forms.HiddenInput(attrs={'id':'prenotaIdCamera'}))
