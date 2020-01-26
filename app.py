from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from features import question_manager
import mimetypes
import os
from urllib.parse import urlparse
import requests
from twilio.twiml.messaging_response import MessagingResponse
#
app = Flask(__name__)
# GOOD_BOY_URL = "https://images.unsplash.com/photo-1518717758536-85ae29035b6d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"
#
# ENV = 'dev'
#
# if ENV == 'dev':
#     app.debug = True
#     POSTGRES = {
#         'user': 'postgres',
#         'pw': 'schilo',
#         'db': 'regdb',
#         'host': 'localhost',
#         'port': '5432',
#     }
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:schilo@localhost:5432/regdb'
# else:
#     app.debug = False
#     app.config['SQLALCHEMY_DATABASE_URI'] = ''
#
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)
#
#
# # class Feedback(db.Model):
# #     __tablename__ = 'feedback'
# #     id = db.Column(db.Integer, primary_key=True)
# #     customer = db.Column(db.String(200), unique=True)
# #     dealer = db.Column(db.String(200))
# #     rating = db.Column(db.Integer)
# #     comments = db.Column(db.Text())
#
# #     def __init__(self, customer, dealer, rating, comments):
# #         self.customer = customer
# #         self.dealer = dealer
# #         self.rating = rating
# #         self.comments = comments
#
# #
# # class User(db.Model):
# #     __tablename__ = 'membres'
# #     id = db.Column(db.Integer, primary_key=True)
# #
# #     nom = db.Column(db.String(80), nullable=False)
# #     prenom = db.Column(db.String(80), nullable=False)
# #     sexe = db.Column(db.String(80),  nullable=False)
# #     date_aniversaire = db.Column(db.DateTime(),  nullable=False)
# #     quartier = db.Column(db.String(80), nullable=False)
# #     telephone = db.Column(db.String(20), nullable=False)
# #     email = db.Column(db.String(120), nullable=False)
# #     statut_matrimomial = db.Column(db.String(120))
# #     nom_du_conjoint =db.Column(db.String(120))
# #     profession = db.Column(db.String(80))
# #     service = db.Column(db.String(80))
# #     filiere = db.Column(db.String(80))
# #     formations = db.Column(db.String(80))
# #     competences =  db.Column(db.String(80))
# #     date_conversion = db.Column(db.DateTime())
# #     date_bapteme = db.Column(db.DateTime())
# #     date_chapelle = db.Column(db.DateTime())
# #     numero_carte_membre = db.Column(db.String(15))
# #     annee_adhesion_jeunesse = db.Column(db.DateTime())
# #
# #     cellule = db.Column(db.String(80))
# #     activites_chapelle = db.Column(db.String(80))
#       nom_image = db.Column(db.String(80))
#       data_image = db.Column(db.LargeBinary)

# #
# #
# #     def __init__(self, nom, prenom , sexe, date_aniversaire, quartier, telephone, email,statut_matrimomial,
# #                  nom_du_conjoint, profession, service, filiere, formations, competences,  date_conversion, date_bapteme, date_chapelle, numero_carte_membre, annee_adhesion_jeunesse, cellule,activites_chapelle, image_name,image_data):
# #         self.nom = nom
# #         self.prenom = prenom
# #         self.date_aniversaire = date_aniversaire
# #         self.quartier = quartier
# #         self.telephone = telephone
# #         self.email = email
# #         self.statut_matrimomial = statut_matrimomial
# #         self.nom_du_conjoint = nom_du_conjoint
# #         self.profession = profession
# #         self.service = service
# #         self.filiere = filiere
# #         self.formations = formations
# #         self.competences = competences
# #         self.date_conversion = date_conversion
# #         self.date_bapteme = date_bapteme
# #         self.date_chapelle = date_chapelle
# #         self.numero_carte_membre = numero_carte_membre
# #         self.annee_adhesion_jeunesse = annee_adhesion_jeunesse
# #         self.cellule = cellule
# #         self.activites_chapelle = activites_chapelle
#             self.image_name = nom_image
#             self.image_data = data_image
#
#
# @app.route('/')
# def index():
#     return "hello world"
#
#
# #
# # @app.route("/whatsapp", methods=["GET", "POST"])
# # def reply_whatsapp():
# #
# #     num_media = int(request.values.get("NumMedia"))
# #     media_files = []
# #     for idx in range(num_media):
# #         media_url = request.values.get(f'MediaUrl{idx}')
# #         mime_type = request.values.get(f'MediaContentType{idx}')
# #         media_files.append((media_url, mime_type))
# #
# #         req = requests.get(media_url)
# #         file_extension = mimetypes.guess_extension(mime_type)
# #         media_sid = os.path.basename(urlparse(media_url).path)
# #
# #         with open(f"app_data/{media_sid}{file_extension}", 'wb') as f:
# #             f.write(req.content)
# #
# #     response = MessagingResponse()
# #     if not num_media:
# #         msg = response.message("Send us an image!")
# #     else:
# #         msg = response.message("Thanks for the image(s).")
# #     msg.media(GOOD_BOY_URL)
# #     return str(response)

DOWNLOAD_DIRECTORY = 'app_data'





@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
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

            resp.message("Thanks for the image!")

        else:
            resp.message("votre fichier doit avoir l'extension .jpeg, .png ou .jpg . merci")

    else:
        resp.message("Try sending a picture message.")

    return str(resp)

    # # if request.values['NumMedia'] != '0':
    # if 1==1:
    #     print("image detect")
    #
    #     # Use the message SID as a filename.
    #     filename = request.values['MessageSid'] + '.jpeg'
    #     with open('{}/{}'.format(DOWNLOAD_DIRECTORY, filename), 'wb') as f:
    #         image_url = request.values['MediaUrl0']
    #         f.write(requests.get(image_url).content)
    #
    #     resp.message("Thanks for the image!")
    # else:
    #     print("image not detect")
    #     resp.message("Try sending a picture message.")
    #
    # return str(resp)

# if __name__ == "__main__":
#     app.run(debug=True)
#
#
#
#
#
# # @app.route('/submit', methods=['POST'])
# # def submit():
# #     if request.method == 'POST':
# #         customer = request.form['customer']
# #         dealer = request.form['dealer']
# #         rating = request.form['rating']
# #         comments = request.form['comments']
# #         # print(customer, dealer, rating, comments)
# #         if customer == '' or dealer == '':
# #             return render_template('index.html', message='Please enter required fields')
# #         if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
# #             data = Feedback(customer, dealer, rating, comments)
# #             db.session.add(data)
# #             db.session.commit()
# #             send_mail(customer, dealer, rating, comments)
# #             return render_template('success.html')
# #         return render_template('index.html', message='You have already submitted feedback')
#
#
# if __name__ == '__main__':
#     app.run()



#
# import mimetypes
# import os
# from urllib.parse import urlparse
#
# from flask import Flask, request
# import requests
# from twilio.twiml.messaging_response import MessagingResponse
#
#
# app = Flask(__name__)
#
#
# GOOD_BOY_URL = "https://images.unsplash.com/photo-1518717758536-85ae29035b6d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"
#
#
# @app.route("/sms", methods=["GET", "POST"])
# def reply_whatsapp():
#
#     print((request.values.get("NumMedia")))
#     num_media = request.values['NumMedia']
#     # num_media = int(request.values.get("NumMedia"))
#     # media_files = []
#     # for idx in range(num_media):
#     #     media_url = request.values.get(f'MediaUrl{idx}')
#     #     mime_type = request.values.get(f'MediaContentType{idx}')
#     #     media_files.append((media_url, mime_type))
#     #
#     #     req = requests.get(media_url)
#     #     file_extension = mimetypes.guess_extension(mime_type)
#     #     media_sid = os.path.basename(urlparse(media_url).path)
#     #
#     #     with open(f"app_data/{media_sid}{file_extension}", 'wb') as f:
#     #         f.write(req.content)
#
#
#     media_url = request.values.get(f'MediaUrl0')
#     mime_type = request.values.get(f'MediaContentType0')
#     # media_files.append((media_url, mime_type))
#
#     req = requests.get(media_url)
#     file_extension = mimetypes.guess_extension(mime_type)
#     media_sid = os.path.basename(urlparse(media_url).path)
#
#     with open(f"app_data/{media_sid}{file_extension}", 'wb') as f:
#         f.write(req.content)
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

    app.run(debug=True)