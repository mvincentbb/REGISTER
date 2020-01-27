from twilio.twiml.messaging_response import MessagingResponse
import requests
from flask import Flask, render_template, request

import mimetypes
import os
from urllib.parse import urlparse

from twilio.twiml.messaging_response import MessagingResponse


def question_manager(msg_send):
    tab = []
    return tab


def add_data(data, db):
    db.session.add(data)
    db.session.commit()
    return "Votre formulaire a ete pris en compte"

def simpleTextInput(resp,compteur,dict, user_dict,from_):
    """
    insertion de message simple
    """

    resp.message(dict[compteur])
    user_dict[from_][compteur]= request.form.get('Message')



def multipleChoiceInput():
    """
    selection parmi une liste multiple de choix
    """


def imageInput(DOWNLOAD_DIRECTORY,compteur):
    """
    insertion d'Image
    """
    """Respond to incoming with a simple text message."""

    resp = MessagingResponse()

    if request.values['NumMedia'] != '0':

        # Use the message SID as a filename.
        mime_type = request.values.get(f'MediaContentType0')
        print("mine_type = ",mime_type)

        print("minetypes = ", mimetypes)
        file_extension = mimetypes.guess_extension(mime_type,True)
        print(file_extension)

        if (file_extension in['.jpeg','.png','.jpg','.jpe']):
            filename = request.values['MessageSid'] + '.jpeg'
            with open('{}/{}'.format(DOWNLOAD_DIRECTORY, filename), 'wb') as f:
                image_url = request.values['MediaUrl0']
                f.write(requests.get(image_url).content)


            user_dict[compteur]=(filename, f.read())

            resp.message("Thanks for the image!")

        else:
            resp.message("votre fichier doit avoir l'extension .jpeg, .png ou .jpg . merci")

    else:
        resp.message("Try sending a picture message.")

    return str(resp)


type_message = {1: "Nom",
                2: "Prenoms",
                3: {"Sexe": {1: "Masculin", 2: "Féminin"}},
                4: "Date anniversaire",
                5: "Quartier",
                6: "Telephone",
                7: "Email",
                8: {"Quel est votre Statut Matrimonial : saisir le numero correspondant "
                    "*1*  👉🏼 Celibataire"
                    "*2* 👉🏼 Veuve"
                    "*3* 👉🏼 Mariee"},
                9: "Nom du conjoint si marie",
                10: "Service/Filiere",
                11: "Formations / Competences",
                12: "Date de Conversion",
                13: "Date de Bapteme",
                14: "Annee d'entree a la chapelle",
                15: "Annee d'ahesion a la jeunesse",
                16: {"Celulle": {1: "Va a Bethel", 2: "Mont des Oliviers", 3: "Ebenezer", 4:"Maranatha"}},
                17: "Activite",
                18: "Inserer votre image"
                }

user_dict = {}
list_of_simpleInput = [1,2,5,6,9,10,11,17]
list_of_dateInput=[4,12,13,14,15]
list_of_multipleChoiceInput=[3,8,16]

# @app.route("/sms")
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message

    # msg = request.form.get('Body')
    from_ = request.form.get('From')
    if from_ not in user_dict.keys():
        user_dict[from_] = {}
    compteur_formulaire = len(user_dict[from_])+ 1
    to = from_

    # Create reply
    resp = MessagingResponse()

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=type_message[compteur_formulaire],
        to=to
    )
    print("####", message.sid)

    resp.message("")

    return str(resp)




