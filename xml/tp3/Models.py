
from peewee import *

## article|inproceedings|proceedings|book|incollection|phdthesis|mastersthesis|www|person|data

db = SqliteDatabase("mydb.db")

class BaseModel(Model):

    class Meta:
        database = db

class Phdthesis(BaseModel):
    """
        author  title pages year volume number
        month  url  ee  publisher
        note  isbn  series  school
    """

    author = CharField(null=True)
    title = CharField(null=True)
    pages = CharField(null=True)
    year = DateField(null=True)
    volume = CharField(null=True)
    number = CharField(null=True)
    mouth = CharField(null=True)
    url = CharField(null=True)
    ee = CharField(null=True)
    publisher = CharField(null=True)
    note = CharField(null=True)
    isbn = CharField(null=True)
    series = CharField(null=True)
    school = CharField(null=True)




## ===================== A concerver tout en bas
db.connect()
db.create_tables([Phdthesis], safe = True)
db.close()