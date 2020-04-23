from manage import db
from pony.orm import Required


class Bug(db.Entity):
    life = Required(int, default=0)
    energy = Required(int, default=100)
