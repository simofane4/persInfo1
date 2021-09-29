from django import forms

class ContactForm(forms.Form):
    nom = forms.CharField( label="nom",max_length=50)
    prenom = forms.CharField( label="prenom ",max_length=50)
    matricule = forms.CharField( label="mle",max_length=50)
    adresse =  forms.CharField(label="adresse",max_length=50)
    email = forms.CharField( label="email",max_length=50)
