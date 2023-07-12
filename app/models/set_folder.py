from .db import db, environment, SCHEMA, add_prefix_for_prod


set_folders = db.Table(
    "set_folders",
    db.Model.metadata,
    db.Column(
        "setId",
        db.Integer,
        db.ForeignKey(add_prefix_for_prod("sets.id")),
        primary_key=True,
    ),
    db.Column(
        "folderId",
        db.Integer,
        db.ForeignKey(add_prefix_for_prod("folders.id")),
        primary_key=True,
    ),
)

if environment == "production":
    set_folders.schema = SCHEMA
