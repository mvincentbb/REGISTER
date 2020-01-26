from twilio.twiml.messaging_response import MessagingResponse


def question_manager(msg_send):
    tab = []
    return tab


def add_data(data, db):
    db.session.add(data)
    db.session.commit()
    return "Votre formulaire a ete pris en compte"


type_message = {1: "Nom",
                2: "Prenoms",
                3: {"Sexe": {1: "Masculin", 2: "Feminin"}},
                4: "Date anniversaire",
                5: "Quartier",
                6: "Telephone",
                7: "Email",
                8: {"Statut Matrimonial": {1: "Celibataire", 2: "Veuve", 3: "Marié(e)"}},
                9: "Nom du conjoint si marie",
                10: "Service/Filiere",
                11: "Formations / Competences",
                12: "Date de Conversion",
                13: "Date de Bapteme",
                14: "Annee d'entree a la chapelle",
                15: "Annee d'ahesion a la jeunesse",
                16: {"Celulle": {1: "Va a Bethel", 2: "Mont des Oliviers", 3: "Ebenezer", 4:"Maranatha"}},
                17: "Activite"
                }

user_dict = {}


# @app.route("/sms")
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message

    # msg = request.form.get('Body')
    from_ = request.form.get('From')
    if from_ not in user_dict.keys():
        user_dict[from_] = {}
        compteur_formulaire = len(user_dict[from_])
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


import mimetypes
import os
from urllib.parse import urlparse

from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)


GOOD_BOY_URL = "https://images.unsplash.com/photo-1518717758536-85ae29035b6d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"



#
#
# @app.route("/whatsapp", methods=["GET", "POST"])
# def reply_whatsapp():
#
#     num_media = int(request.values.get("NumMedia"))
#     media_files = []
#     for idx in range(num_media):
#         media_url = request.values.get(f'MediaUrl{idx}')
#         mime_type = request.values.get(f'MediaContentType{idx}')
#         media_files.append((media_url, mime_type))
#
#         req = requests.get(media_url)
#         file_extension = mimetypes.guess_extension(mime_type)
#         media_sid = os.path.basename(urlparse(media_url).path)
#
#         with open(f"app_data/{media_sid}{file_extension}", 'wb') as f:
#             f.write(req.content)
#
#     response = MessagingResponse()
#     if not num_media:
#         msg = response.message("Send us an image!")
#     else:
#         msg = response.message("Thanks for the image(s).")
#     msg.media(GOOD_BOY_URL)
#     return str(response)
#

if __name__ == "__main__":
    app.run()
