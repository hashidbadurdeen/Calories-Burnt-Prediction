# 🔥 Calorie Prediction Web Application

A full-stack machine learning web application that predicts **calories burned** based on user input using a trained ML model. The app features user login, feedback submission, and an interactive prediction interface built with Flask and MySQL.

---

## 🚀 Features

- User registration and login system  
- Calories burned prediction using a machine learning model  
- Interactive web interface built with HTML, CSS, and Flask  
- Feedback collection system  
- MySQL database integration  
- Trained model built using Python and scikit-learn  

---

## 🛠️ Technologies Used

### 👨‍💻 Languages & Libraries

| Category         | Tools/Technologies                             |
|------------------|------------------------------------------------|
| **Frontend**     | HTML, CSS, JavaScript                          |
| **Backend**      | Python, Flask                                  |
| **Database**     | MySQL                                          |
| **Data Science** | Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn |
| **Deployment**   | Pickle (model serialization)                   |

---

## 📊 Machine Learning Model

The model was developed in a Jupyter Notebook (`Final_Dissertation_Project_Calories_Prediction.ipynb`) and trained on a dataset including:

- Gender  
- Age  
- Height  
- Weight  
- Exercise Duration  
- Heart Rate  
- Body Temperature  
- Exercise Type  

The trained model is saved as `Calories.pkl` and integrated into the Flask app to make real-time predictions.

---

## 📁 Folder Structure

```
├── app.py                          # Flask backend logic
├── templates/                      # HTML pages (login, home, prediction, etc.)
├── static/                         # CSS, JS files
├── Calories.pkl                    # Trained ML model
├── Final_Dissertation_Project_Calories_Prediction.ipynb  # Model training notebook
├── README.md                       # Project documentation
```

---

## 🧠 How It Works

1. User registers or logs in.
2. User inputs parameters (age, gender, exercise type, etc.).
3. The data is passed to a trained model.
4. Model returns the predicted number of calories burned.
5. Result is displayed on the frontend.

---

## ⚙️ Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start MySQL Server & Create Database:**
   - Create a database named `calories`
   - Create tables for `user` and `feedback` as per the `app.py` logic

4. **Run the Flask App:**
   ```bash
   python app.py
   ```

---

## 📝 Feedback

Feedback can be submitted through the `/contact` page and is stored in the MySQL database for review.

---

## 🛡️ Security Note

- Avoid hardcoding credentials in production.
- Use environment variables for DB credentials and secret keys.

---

## 📬 Contact

If you have questions or suggestions, feel free to open an issue or reach out!


