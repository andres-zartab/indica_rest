import datetime
from marshmallow import fields, Schema
from . import db


# association_table = db.Table('association', Base.metadata,
#                           Column('seeds_id', Integer, ForeignKey('seeds.id')),
#                           Column('users_id', Integer, ForeignKey('users.id'))
#                           )


class SeedModel(db.Model):
    """
    Seed Model
    """

    __tablename__ = 'seeds'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    source = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __init__(self, data):
        self.owner_id = data.get('owner_id')
        self.name = data.get('name')
        self.source = data.get('source')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        de.session.commit()

    @staticmethod
    def get_all_seeds():
        return SeedModel.query.all()

    @staticmethod
    def get_one_seed(id):
        return SeedModel.query.get(id)

    def __repr__(self):
        return '<id {}>'.format(self.id)


class SeedSchema(Schema):
    id = fields.Int(dump_only=True)
    owner_id = fields.Int(required=True)
    name = fields.Str(required=True)
    source = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
