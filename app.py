#PRUEBA 2


# A very simple Flask Hello World app for you to get started with...
from dataclasses import dataclass
import datetime
from sqlalchemy import select, and_, or_, ForeignKey, UniqueConstraint
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func
from flask import Flask, jsonify,  request, render_template,session,redirect
from flask_sqlalchemy import SQLAlchemy
import json
from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Micontra123@localhost:5432/postgres'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:password@localhost:5432/proyecto'

app.config['SQLALCHEMY<@_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@dataclass
class PERSONA(db.Model):
    __tablename__ = 'PERSONA'
    id: int
    correo:str
    username: str
    password: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    correo = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f'<PERSONA {self.username}>'
    
    def check_password(self, password):
        return self.password == password



@app.route('/')
def hello_world():
    return 'HOLA BOLA'

from flask_cors import CORS 
CORS(app)

@app.route('/personas',methods=['GET', 'POST'])
def route_personas():
    if request.method=='GET':
        personas = PERSONA.query.all()
        return jsonify(personas)
    
    elif request.method == 'POST':
        data = request.get_json()
        persona = PERSONA(username=data["username"], correo=data["correo"], password=data["password"])
        db.session.add(persona)
        db.session.commit()
        return jsonify(persona)
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    #app.run(debug=True, port=5000, host='192.168.18.14')
    app.run()