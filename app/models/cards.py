from .db import db, SCHEMA, add_prefix_for_prod, environment


class Card(db.Model):
    __tablename__ = "cards"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer,primary_key = True)
    question = db.Column(db.String(225),nullable=False)
    answer = db.Column(db.String(225), nullable = False)
    setId = db.Column(db.Integer,db.ForeignKey(add_prefix_for_prod("sets.id")), nullable = False)

    cardsInSet = db.relationship("Set", back_populates = "setOfCards")

    def to_dict(self):
        return {
            "id":self.id,
            "question":self.question,
            "answer":self.answer,
            "setId":self.setId
        }
