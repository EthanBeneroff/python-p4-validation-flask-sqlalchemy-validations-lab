from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'
    
    @validates('name')
    def validate_name(self, key, name_value):
        if not name_value:
            raise ValueError('Name cannot be null')
        names = db.session.query(Author.name).all()
        if name_value in names:
            raise ValueError('Name must be unique')
        return name_value

    @validates('phone_number')
    def validate_phone_number(self, key, number):
        if len(number) != 10:
            raise ValueError("Phone number must be 10 digits")
        return number

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
    
    @validates('content')
    def validate_content(self, key, text):
        if (len(text) <250):
            raise ValueError('Content must be at least 250 characters')
        return text
    
    @validates('summary')
    def validate_summary(self, key, summary_value):
        if (len(summary_value) > 250):
            raise ValueError('Summary must be less than 250 characters')
        return summary_value
    
    @validates('category')
    def validate_category(self, key, cat):
        if not (cat == "Fiction" or cat == "Non-Fiction"):
            raise ValueError("Category must be Fiction or Non-Fiction")
        return cat
    
    @validates('title')
    def validate_title(self,key,title):
        clickbaits = ("Won't Believe", "Secret", "Top", "Guess")
        if "Won't Believe" or "Secret" or "Top" or "Guess" not in title:
            raise ValueError("Title must be clickbait")
        return title

