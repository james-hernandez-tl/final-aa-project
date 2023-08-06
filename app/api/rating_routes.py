from flask import Blueprint, jsonify, Flask, request
from flask_login import login_required, current_user
from app.models import Set,db, Rating
from app.forms import setForm, ratingForm

rating_routes = Blueprint("ratings", __name__)

@rating_routes.route("/",methods = ["POST"])
@login_required
def create_rating():

    form = ratingForm()

    form['csrf_token'].data = request.cookies['csrf_token']


    if form.validate_on_submit():
        data = form.data

        newRating = Rating(
            userId = data["userId"],
            setId = data["setId"],
            rating = data["rating"]
        )

        db.session.add(newRating)
        db.session.commit()

        set = Set.query.get(data["setId"])
        return set.to_dict()

    return {"errors":form.errors}, 401


@rating_routes.route("/", methods = ["PUT"])
@login_required
def edit_rating():

    rating = Rating.query.get(request.json["id"])

    if not rating:
        return {'errors':"rating does not exist"}

    form = ratingForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():

        data = form.data

        rating.userId = data["userId"]
        rating.setId = data["setId"]
        rating.rating = data["rating"]

        db.session.commit()
        set = Set.query.get(data["setId"])
        return set.to_dict()

    return {"errors":form.errors}, 401
