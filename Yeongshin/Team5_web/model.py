from Team5_web import db

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.LargeBinary, nullable=False)
    caption = db.Column(db.Text, nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    #
    # def __repr__(self):
    #     return f'Image(id={self.id}, caption="{self.caption[:20]}")'