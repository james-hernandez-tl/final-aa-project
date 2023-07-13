from flask import Blueprint, jsonify, Flask, request
from flask_login import login_required, current_user
from app.models import Card,db
from app.forms import cardForm

card_routes = Blueprint('cards', __name__)

@card_routes.route("/",methods = ["POST"])
@login_required
def createCard(setId):

    for card in request.json:
        form = cardForm(question = card["question"], answer = card["answer"],setId= card["setId"])
        form['csrf_token'].data = request.cookies['csrf_token']

        if form.validate_on_submit():
            data = form.data

            newCard = Card(
                question = data["question"],
                answer = data["answer"],
                setId = data["setId"]
            )

            db.session.add(newCard)
        else:
            return {"errors":form.errors,"card":form.data}, 404
    db.session.commit()
    return {"message","succesful"}, 200


@card_routes.routes("/<int:cardId>",methods = ["DELETE"])
@login_required
def deleteCard(cardId):
    card = Card.query.get(cardId)

    if not card:
        return {"errors":"Card does not exist"}

    db.session.delete(card)
    db.session.commit()
    return {"message":"succesful"}, 200


@card_routes.routes("/",methods = ["Delete"])
@login_required
def editCards():
    for card in request.json:
        form = cardForm(question = card["question"], answer = card["answer"],setId= card["setId"])
        form['csrf_token'].data = request.cookies['csrf_token']

        if form.validate_on_submit():
            data = form.data

            card.question = data["question"]
            card.answer = data["answer"]

        else:
            return {"errors":form.errors,"card":form.data}, 404
    db.session.commit()
    return {"message","succesful"}, 200
