import sqlalchemy
from .db_session import SqlAlchemyBase
from .users import User


class Department(SqlAlchemyBase):
    __tablename__ = 'Department'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)
    chief = sqlalchemy.Column(sqlalchemy.Integer)
    members = sqlalchemy.types.ARRAY(User.id, as_tuple=False, dimensions=None, zero_indexes=False)
    email = sqlalchemy.Column(sqlalchemy.String)