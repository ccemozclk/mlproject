# 🎯 MLProject - Student Performance Predictor

This project is an end-to-end machine learning pipeline that predicts student performance using demographic and academic data. It is deployed on **AWS Elastic Beanstalk** using a fully automated CI/CD workflow via **CodePipeline + CodeBuild**.

---

## 🚀 Deployment URL
You can test the project live here:  
🔗 [http://mlproject-env.eba-2ifjf9pm.us-east-1.elasticbeanstalk.com/](http://mlproject-env.eba-2ifjf9pm.us-east-1.elasticbeanstalk.com/)

---

## 🔧 Tech Stack
- Python 3.11
- Flask + Gunicorn
- Scikit-learn, XGBoost, CatBoost
- AWS Elastic Beanstalk
- AWS CodePipeline & CodeBuild
- GitHub (main branch trigger)

---

## 📁 Project Structure
'''
mlproject/
├── app.py
├── templates/
│ ├── index.html
│ └── home.html
├── src/
│ └── ...
├── artifacts/
│ └── model.pkl
├── requirements.txt
├── Procfile
├── .ebextensions/
│ └── python.config
└── README.md
'''

---

## 🧪 Prediction Flow

1. Go to `/predictdata`
2. Fill the form
3. Click Submit
4. See prediction on-screen instantly

---

## 🙋‍♂️ Author
Cem Özçelik  
_Data Scientist | AI Enthusiast | Industrial Engineer
