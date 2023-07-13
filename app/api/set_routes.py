from flask import Blueprint, jsonify, Flask, request
from flask_login import login_required, current_user
from app.models import Set,db
from app.forms import setForm


set_routes = Blueprint('sets', __name__)


@set_routes.route("/")
def getAllSets():
    search = request.args.to_dict().get("search")
    if search:
        allSets = Set.query.filter(Set.name.like(f"{search}%")).all()
    else:
        allSets = Set.query.order_by(Set.rating)

    dictSets = [aset.to_dict() for aset in allSets]
    recommend = sorted(dictSets,key = lambda x: x["Rating"], reverse=True)[:10]
    obj = {"allSets":dictSets,"recommended":recommend}
    return obj , 200


@set_routes.route("/",methods=["POST"])
@login_required
def create_a_set():
    form = setForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        data = form.data

        newSet = Set(
            name=data["name"],
            description=data["description"],
            draft=data["draft"],
            userId=data["userId"],
        )

        db.session.add(newSet)
        db.session.commit()
        return newSet.to_dict(), 200
    return {"errors":form.errors}, 404


@set_routes.route("/<int:setId>")
def getOneSet(setId):
    set = Set.query.get(setId)
    if set:
        return set.to_dict(), 200
    return {"errors":"set does not exist"}, 404


@set_routes.route("/<int:setId>",methods = ["PUT"])
@login_required
def editSet(setId):
    set = Set.query.get(setId)

    if not set:
        return {"errors":"set does not exist"}

    form = setForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        data = form.data

        set.name=data["name"],
        set.description=data["description"],
        set.draft=data["draft"],
        set.userId=data["userId"],

        db.session.commit()
        return set.to_dict(), 200
    return {"errors":form.errors}, 404


@set_routes.route("/<int:setId>",methods = ["DELETE"])
def deleteSet(setId):
    Set.query.filter(Set.id == setId).delete()
    db.session.commit()

    return {"message":"succesfully deleted"}
