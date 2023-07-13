from .db import db,SCHEMA, add_prefix_for_prod, environment

class Rating(db.Model):
    __tablename__ = "ratings"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key = True)
    userId = db.Column(db.Integer,db.ForeignKey(add_prefix_for_prod("users.id")) ,nullable = False)
    setId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("sets.id")) ,nullable = False)
    rating = db.Column(db.Integer)

    users = db.relationship("User", foreign_keys = [userId], back_populates = "usersRatings")
    set = db.relationship("Set", foreign_keys = [setId], back_populates = "setRating")

    def to_dict(self):
        return {
            "id":self.id,
            "userId":self.userId,
            "setId":self.setId,
            "rating":self.rating
        }
