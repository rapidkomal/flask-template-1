"""
Database module, including the SQLAlchemy database object
and DB-related utilities.
"""

from extensions import db

import datetime

# Alias common SQLAlchemy names
Column = db.Column
relationship = db.relationship


class BaseModel(db.Model):
    """
    Base model class that includes created_at, updated_at
    plus adds a 'primary key' column named ``id``.
    """
    __abstract__ = True

    id = Column(db.Integer, primary_key=True)
    created_at = Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(db.DateTime, default=datetime.datetime.utcnow,
                        onupdate=datetime.datetime.utcnow)
