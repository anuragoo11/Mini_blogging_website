from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///blog.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Blog model
class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Blog({self.title}, by {self.author})"

# Create the database (run this only once)
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        # Create and add a new blog
        blog = Blog(title=title, content=content, author=author)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('home'))
    
    # Retrieve all blogs
    blogs = Blog.query.order_by(Blog.timestamp.desc()).all()
    return render_template('home.html', blogs=blogs)

@app.route('/view/<int:id>')
def view_blog(id):
    blog = Blog.query.get_or_404(id)
    return render_template('view.html', blog=blog)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_blog(id):
    blog = Blog.query.get_or_404(id)
    if request.method == 'POST':
        blog.title = request.form['title']
        blog.content = request.form['content']
        blog.author = request.form['author']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('update.html', blog=blog)

@app.route('/delete/<int:id>')
def delete_blog(id):
    blog = Blog.query.get_or_404(id)
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)