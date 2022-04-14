from app.common.database import Column, db, BaseModel


class Project(BaseModel):
    __tablename__ = 'projects'

    name = Column(db.String)
