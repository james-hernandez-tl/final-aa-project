from flask import Blueprint, jsonify, Flask, request
from flask_login import login_required, current_user
from app.models import Card,db,Set
from app.forms import cardForm

card_routes = Blueprint('cards', __name__)

@card_routes.route("/",methods = ["POST"])
@login_required
def createCard():

    for card in request.json["cards"]:

        form = cardForm(question = card["question"],answer = card["answer"], setId = card["setId"])
        form['csrf_token'].data = request.cookies['csrf_token']

        if form.validate_on_submit():
            data = form.data

            setId = data["setId"]

            newCard = Card(
                question = data["question"],
                answer = data["answer"],
                setId = data["setId"]
            )

            db.session.add(newCard)
        else:

            return {"errors":form.errors,"card":form.data}, 404
    db.session.commit()
    set = Set.query.get(setId)
    return set.to_dict(), 200


@card_routes.route("/",methods = ["DELETE"])
@login_required
def deleteCard():

    for cardId in request.json["cards"]:
        deletedCard = Card.query.get(cardId)

        if not deletedCard:
            return {"errors":{"error":"card does not exist","card":cardId}}, 404
        setId = deletedCard.setId

        db.session.delete(deletedCard)
    db.session.commit()

    set = Set.query.get(setId)
    return set.to_dict(), 200


@card_routes.route("/",methods = ["Put"])
@login_required
def editCards():
    for card in request.json["cards"]:
        form = cardForm(question = card["question"], answer = card["answer"],setId= card["setId"])
        form['csrf_token'].data = request.cookies['csrf_token']

        if form.validate_on_submit():
            data = form.data
            oldCard = Card.query.get(card["id"])
            setId = card["setId"]

            oldCard.question = data["question"]
            oldCard.answer = data["answer"]

        else:
            return {"errors":form.errors,"card":form.data}, 404
    db.session.commit()
    set = Set.query.get(setId)
    return set.to_dict(), 200
