from flask import Blueprint, jsonify, Flask, request
from flask_login import login_required, current_user
from app.models import Card,db,Set
from app.forms import cardForm

card_routes = Blueprint('cards', __name__)

@card_routes.route("/",methods = ["POST"])
@login_required
def createCard():
    print("[request.json]",request.json)
    for card in request.json["cards"]:
        print("[card]",card)
        form = cardForm(question = card["question"],answer = card["answer"], setId = card["setId"])
        # form["question"] = card["question"]
        # form["answer"] = card["answer"]
        # form["setId"] = card["setId"]
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
            print("[card errors]",form.errors)
            return {"errors":form.errors,"card":form.data}, 404
    db.session.commit()
    set = Set.query.get(setId)
    return set.to_dict(), 200


@card_routes.route("/<int:cardId>",methods = ["DELETE"])
@login_required
def deleteCard(cardId):
    card = Card.query.get(cardId)

    if not card:
        return {"errors":"Card does not exist"}

    db.session.delete(card)
    db.session.commit()
    return {"message":"succesful"}, 200


@card_routes.route("/",methods = ["Delete"])
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
