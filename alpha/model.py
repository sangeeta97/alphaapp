from alpha import db



class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer(), primary_key=True)
    name= db.Column(db.String(length=50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    param_model = db.Column(db.String(length=60), nullable=False)
    param_db = db.Column(db.String(length=60), nullable=False)
    inputfile = db.Column(db.String(length=100), nullable=False)
    outputfile= db.Column(db.String(length=100), nullable=False)
    uniquestr = db.Column(db.String(length=100), nullable=False, unique= True)
    state = db.Column(db.String(length=100), nullable=False)




    def __init__(self, name, email, param_model, param_db, inputfile, outputfile, uniquestr, state):
        self.name = name
        self.email = email
        self.param_model = param_model
        self.param_db = param_db
        self.inputfile = inputfile
        self.outputfile = outputfile
        self.uniquestr = uniquestr
        self.state = state
