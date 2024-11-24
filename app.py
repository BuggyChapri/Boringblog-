from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Blog_post.db"
db = SQLAlchemy(app)

class Blog_post(db.Model):
    srno = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    blog_img = db.Column(db.String(50), nullable = False)
    blog_title = db.Column(db.String(50), nullable = False)
    blog_content = db.Column(db.String(500), nullable = False)

    def __repr__(self):
        return f"<Blog_post(title='{self.blog_title}', content='{self.blog_content}')>"

class Login_data(db.Model):
    srno = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(50), nullable=  False)
    password = db.Column(db.String(30), nullable = False)

@app.route("/")
def index():
    allData = Blog_post.query.all()
    return render_template("index.html", allData = allData)

@app.route("/delete/<int:srno>")
def delete(srno):
    allData = Blog_post.query.filter_by(srno = srno).first()
    db.session.delete(allData)
    db.session.commit() 
    return redirect("/")

@app.route("/show/<int:srno>")
def show(srno):
    allData = Blog_post.query.filter_by(srno=srno).first()
    return render_template("show.html", allData=allData)


@app.route("/create_blog", methods=["GET", "POST"])
def create_blog():
    if request.method == "POST":
        blog_img = request.form.get("src") 
        title = request.form.get("Title")
        content = request.form.get("content")
        blog_post = Blog_post(blog_title=title, blog_content=content, blog_img=blog_img)
        db.session.add(blog_post)
        db.session.commit()
    allData = Blog_post.query.all()
    return render_template("create_blog.html")


@app.route("/contact", methods = ["GET","POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        login = Login_data(name = name, email = email, password = password)
        db.session.add(login)
        db.session.commit() 
    return render_template("contact.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug = True)