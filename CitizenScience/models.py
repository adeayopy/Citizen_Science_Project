from CitizenScience import db

#Database setup
class Picture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    rank=db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return f"Picture('{self.name}', '{self.rank}')"

