### Mini Blogging Website 📝

A simple blogging website built using Flask where users can create, update, view, and delete blogs. This project demonstrates the use of Flask, SQLAlchemy, and Jinja2 for web development.

## Features ✨

- Create new blog posts.
- View a list of all blog posts.
- Update existing blog posts.
- Delete blog posts.
- Uses a SQLite database to store blog data.

## Project Structure 📁
```
mini_blogging_website
|
|__ __pycache__        # Compiled Python files (not uploaded)
|__ env                # Virtual environment (not uploaded)
|__ instance
|      |__ blog.db     # SQLite database (not uploaded; auto-generated)
|__ templates
|      |__ base.html   # Base template for consistent styling
|      |__ home.html   # Homepage for displaying all blogs
|      |__ view.html   # Page to view individual blogs
|      |__ update.html # Page to update blogs
|__ app.py             # Main Flask application
|__ requirements.txt   # List of dependencies
|__ README.md          # Project documentation (this file)
```

## Setup Instructions 🛠️

Follow these steps to run the project on your local machine:

### 1. Clone the Repository
```bash
git clone <repository_url>
cd mini_blogging_website
```

### 2. Set Up a Virtual Environment
Create a virtual environment to isolate dependencies:
```bash
python -m venv env
```
Activate the virtual environment:
- On Windows:
  ```bash
  .\env\Scripts\activate.ps1
  ```
- On macOS/Linux:
  ```bash
  source env/bin/activate
  ```

### 3. Install Dependencies
Install all required Python packages:
```bash
pip install -r requirements.txt
```

### 4. Initialize the Database
Run the following command to create the SQLite database:
```bash
python -c "from app import db; db.create_all()"
```

### 5. Run the Application
Start the Flask development server:
```bash
python app.py
```
Access the website at `http://127.0.0.1:5000/` in your browser.

## Dependencies 📦

These dependencies are listed in `requirements.txt`:

- Flask==2.3.2
- Flask-SQLAlchemy==3.0.5
- Jinja2==3.1.2

To install them, use:
```bash
pip install -r requirements.txt
```

## Notes 📝

- The `blog.db` file is not uploaded as it is generated automatically when you initialize the database. Ensure you run the command in Step 4 to create it.
- Avoid uploading the `env` and `__pycache__` folders to your repository.

## Contributing 🤝

Feel free to fork this repository and contribute by submitting pull requests. Let's make this project better together!

## License 📜

This project is open-source and available under the [MIT License](LICENSE).

---

Happy coding! 😊
