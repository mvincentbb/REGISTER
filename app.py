from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from features import question_manager

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    POSTGRES = {
        'user': 'postgres',
        'pw': 'schilo',
        'db': 'regdb',
        'host': 'localhost',
        'port': '5432',
    }
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:schilo@localhost:5432/regdb'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# class Feedback(db.Model):
#     __tablename__ = 'feedback'
#     id = db.Column(db.Integer, primary_key=True)
#     customer = db.Column(db.String(200), unique=True)
#     dealer = db.Column(db.String(200))
#     rating = db.Column(db.Integer)
#     comments = db.Column(db.Text())

#     def __init__(self, customer, dealer, rating, comments):
#         self.customer = customer
#         self.dealer = dealer
#         self.rating = rating
#         self.comments = comments


class User(db.Model):
    __tablename__ = 'membres'
    id = db.Column(db.Integer, primary_key=True)

    nom = db.Column(db.String(80), nullable=False)
    prenom = db.Column(db.String(80), nullable=False)
    sexe = db.Column(db.String(80),  nullable=False)
    date_aniversaire = db.Column(db.DateTime(),  nullable=False)
    quartier = db.Column(db.String(80), nullable=False)
    telephone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    statut_matrimomial = db.Column(db.String(120))
    nom_du_conjoint =db.Column(db.String(120))
    profession = db.Column(db.String(80))
    service = db.Column(db.String(80))
    filiere = db.Column(db.String(80))
    formations = db.Column(db.String(80))
    competences =  db.Column(db.String(80))
    date_conversion = db.Column(db.DateTime())
    date_bapteme = db.Column(db.DateTime())
    date_chapelle = db.Column(db.DateTime())
    numero_carte_membre = db.Column(db.String(15))
    annee_adhesion_jeunesse = db.Column(db.DateTime())

    cellule = db.Column(db.String(80))
    activites_chapelle = db.Column(db.String(80))


    def __init__(self, nom, prenom , sexe, date_aniversaire, quartier, telephone, email,statut_matrimomial,
                 nom_du_conjoint, profession, service, filiere, formations, competences,  date_conversion, date_bapteme, date_chapelle, numero_carte_membre, annee_adhesion_jeunesse, cellule,activites_chapelle):
        self.nom = nom
        self.prenom = prenom
        self.date_aniversaire = date_aniversaire
        self.quartier = quartier
        self.telephone = telephone
        self.email = email
        self.statut_matrimomial = statut_matrimomial
        self.nom_du_conjoint = nom_du_conjoint
        self.profession = profession
        self.service = service
        self.filiere = filiere
        self.formations = formations
        self.competences = competences
        self.date_conversion = date_conversion
        self.date_bapteme = date_bapteme
        self.date_chapelle = date_chapelle
        self.numero_carte_membre = numero_carte_membre
        self.annee_adhesion_jeunesse = annee_adhesion_jeunesse
        self.cellule = cellule
        self.activites_chapelle = activites_chapelle


@app.route('/')
def index():
    # return render_template('index.html')
    utilisateurs = User()


    

    

# @app.route('/submit', methods=['POST'])
# def submit():
#     if request.method == 'POST':
#         customer = request.form['customer']
#         dealer = request.form['dealer']
#         rating = request.form['rating']
#         comments = request.form['comments']
#         # print(customer, dealer, rating, comments)
#         if customer == '' or dealer == '':
#             return render_template('index.html', message='Please enter required fields')
#         if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
#             data = Feedback(customer, dealer, rating, comments)
#             db.session.add(data)
#             db.session.commit()
#             send_mail(customer, dealer, rating, comments)
#             return render_template('success.html')
#         return render_template('index.html', message='You have already submitted feedback')


if __name__ == '__main__':
    app.run()