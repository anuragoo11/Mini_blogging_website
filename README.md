# Mini Blogging Website 🗒

A simple blogging application built with Flask. Users can create, view, update, and delete blogs. This project demonstrates fundamental web development concepts, database handling, and templating using Flask and Jinja2.

---

## Features ✨
- 🖋️ Create blogs with a title, content, and author name.  
- 📜 View a list of all blogs.  
- ✏️ Update and ❌ delete existing blogs.  
- 📂 Automatically creates the database when the app runs.  

---

## Project Structure 📂
```
mini_blogging_website  
|  
|-- env/                   # Virtual environment (not included in the repository)  
|-- instance/  
|   |-- blog.db            # Database file (automatically generated)  
|-- templates/             # HTML templates for the app  
|   |-- base.html  
|   |-- home.html  
|   |-- update.html  
|   |-- view.html  
|-- app.py                 # Main Flask application  
|-- requirements.txt       # Python dependencies  
```

---

## Prerequisites ⚙️
- 🐍 Python 3.8 or above  
- 📦 pip (Python package manager)  

---

## Setup Instructions 🛠️

### 1. Clone the Repository 📥
```bash
git clone https://github.com/anuragoo11/Mini_blogging_website
cd mini_blogging_website
```

### 2. Create a Virtual Environment 🌐
```bash
python -m venv env
```

### 3. Activate the Virtual Environment ⚡
- On Windows:
  ```bash
  .\env\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source env/bin/activate
  ```

### 4. Install Dependencies 📋
```bash
pip install -r requirements.txt
```

### 5. Run the Application 🚀
```bash
python app.py
```

The application will be accessible at `http://127.0.0.1:5000/`.

---

## Usage 💻
- Open your browser and navigate to `http://127.0.0.1:5000/`.  
- 🖐️ Create a new blog by filling out the form on the home page.  
- 🔄 View, update, or delete blogs using the provided buttons.  

---

## Notes 📝
- The `blog.db` file will be automatically created in the `instance/` directory when the app runs for the first time.  
- Ensure you activate the virtual environment every time before running the app.  

---

## Dependencies 📦
The application uses the following libraries, which are listed in `requirements.txt`:  
- Flask  
- Flask-SQLAlchemy  
- Jinja2  

---

## Screenshots 📸
### Home Page  
![image](https://github.com/user-attachments/assets/b2360487-fa71-4858-aea9-3da174f469c6)
![image](https://github.com/user-attachments/assets/247c7318-fd3c-45ab-80b4-7ff55e90024e)

---

## License 🛡️
This project is licensed under the MIT License. Feel free to use and modify it as needed!  

---

## Contact 📧
For any questions or suggestions, feel free to contact the project owner. 😊
