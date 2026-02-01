from flask import Flask, render_template,redirect,request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column()

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def user_create():
    if request.method == "POST":
        user = User(
            username=request.form["name"],
            email=request.form["email"],
        )
        db.session.add(user)
        db.session.commit()

    return render_template("index.html")

if __name__ == '__main__':
  app.run(debug=True)