from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy import UniqueConstraint
from .set_folder import set_folders


class Folder(db.model):
    __tablename__ = "folders"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(15), nullable = False)
    description = db.Column(db.String(100),nullable = False)
    userId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable = False)

    user = db.relationship("User",back_populates = "folder", cascade="all, delete")

    UniqueConstraint("name","userId", name="idx_Folder_name_userId")
