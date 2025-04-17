
from flask import Flask, jsonify,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"

@app.route('/')
def index():
    return 'Hello!'

@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    output = []

    for drink in drinks:
        drink_data = {
            'id':drink.id,
            'name': drink.name,
            'description': drink.description
        }
        output.append(drink_data)

    return jsonify(drinks=output)

@app.route('/drinks/<int:id>')
def get_drink(id):
    k= Drink.query.all()
    print(k)
    drink = Drink.query.get_or_404(id)
    return jsonify(name=drink.name, description=drink.description)

@app.route('/drinks',methods=['POST'])
def add_drink():

  drink = Drink(name = request.json['name'],description = request.json['description'])
  db.session.add(drink)
  db.session.commit()
  return jsonify(id=drink.id)

@app.route('/drinks/<int:id>',methods=['DELETE'])
def delete_drink(id):
  drink = Drink.query.get(id)
  if drink is None:
    return jsonify(error="not found")
  
  db.session.delete(drink)
  db.session.commit()
  return jsonify(message="removed")


'''
To create tables we say 
db.create_all()

to create and add data
import the following class and do execute the following ones:-
from application import Drink
drink = Drink(name = 'Cocacola', description = 'It is very sweet with soda brown in color')
db.session.add(drink)
db.session.commit()

To display the drinks 
Drink.query.all()

And to exit the interpreter - exit()
'''
if __name__ == '__main__':
    app.run(debug=True)
