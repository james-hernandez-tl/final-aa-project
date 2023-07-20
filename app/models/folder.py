from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy import UniqueConstraint
from .set_folder import set_folders


class Folder(db.Model):
    __tablename__ = "folders"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    description = db.Column(db.String(100),nullable = False)
    userId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable = False)

    user = db.relationship("User",back_populates = "folder")

    foldersOfSets = db.relationship(
        "Set",
        secondary=set_folders,
        back_populates="setsInFolder"
    )

    UniqueConstraint("name","userId", name="idx_Folder_name_userId")

    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "description":self.description,
            "userId":self.userId,
            "Sets":[aset.to_dict_less() for aset in self.foldersOfSets],
            "NumSets":len(self.foldersOfSets)
        }

    def to_dict_less(self):
        return {
            "id":self.id,
            "name":self.name,
            "description":self.description,
            "userId":self.userId,
            "NumSets":len(self.foldersOfSets)
        }
