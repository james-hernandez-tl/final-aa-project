from flask import Blueprint, Flask, request
from flask_login import login_required, current_user
from app.models import Set,db, Folder, Set
from app.forms import folderForm

folder_routes = Blueprint("folders",__name__)

@folder_routes.route("/<int:id>")
@login_required
def getOneFolder(id):
    folder = Folder.query.get(id)
    if folder:
        return folder.to_dict(),200
    return {"errors":"folder does not exist"} , 404


@folder_routes.route("/<int:id>", methods=["DELETE"])
@login_required
def deleteFolder(id):
    folder = Folder.query.get(id)

    if not folder:
        return {"errors":"folder does not exist"} , 404

    if (current_user.id != folder.userId):
        return {"errors":"unauthorized"} , 404

    db.session.delete(folder)
    db.session.commit()
    return {"message":"succesfully deleted"} , 200


@folder_routes.route("/", methods = ["POST"])
@login_required
def createFolder():
    form = folderForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        data = form.data

        newFolder = Folder(
            name=data["name"],
            description=data["description"],
            userId=data["userId"],
        )

        db.session.add(newFolder)
        db.session.commit()

        return newFolder.to_dict(), 200
    return {"errors":form.errors}, 404


@folder_routes.route("/<int:id>", methods = ["PUT"])
@login_required
def editFolder(id):
    folder = Folder.query.get(id)
    if not folder:
        return {"errors":"Folder doesnt exist"}, 404

    if folder.userId != current_user.id :
        return {"errors":"Unauthorized"}, 404

    form = folderForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        data = form.data

        folder.name=data["name"]
        folder.description=data["description"]
        folder.userId=data["userId"]

        db.session.commit()

        return folder.to_dict(), 200
    return {"errors":form.errors}, 404


@folder_routes.route("/<int:id>/sets/<int:setId>",methods=["POST"])
@login_required
def addSetToFolder(id,setId):
    set = Set.query.get(setId)

    if not set:
        return {"errors":"set does not exist"}, 404

    folder = Folder.query.get(id)

    if not folder:
        return {"errors":"folder does not exist"}, 404

    if folder.userId != current_user.id:
        return {"errors":"Unathurized"}, 404

    if set in folder.foldersOfSets:
        return {"errors":"set is already in folder"}, 404

    folder.foldersOfSets.append(set)
    db.session.commit()

    return folder.to_dict(), 200

@folder_routes.route("/<int:id>/sets/<int:setId>",methods=["DELETE"])
@login_required
def removeSetFromFolder(id,setId):
    set = Set.query.get(setId)

    if not set:
        return {"errors":"set does not exist"} , 404

    folder = Folder.query.get(id)

    if not folder:
        return {"errors":"folder does not exist"}, 404

    if folder.userId != current_user.id:
        return {"errors":"Unathurized"}, 404


    folder.foldersOfSets.remove(set)
    db.session.commit()

    return folder.to_dict(), 200
