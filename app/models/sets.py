from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy import UniqueConstraint

class Set(db.model):
    __tablename__ = "sets"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    desciption = db.Column(db.String(100),nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)

    user = db.relationship("User",backreferences = "set")
    UniqueConstraint("name","userId", name="idx_name_userId")
