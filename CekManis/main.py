import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model diabetes
model = pickle.load(open('diabetes_model.pkl', 'rb'))

# Halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# Halaman about
@app.route('/informasi-diabetes')
def about():
    return render_template('about.html')

# Halaman blog utama
@app.route('/blog')
def blog():
    return render_template('blog.html')

# Blog detail (1–6)
@app.route('/kenali-lebih-dalam-terkait-diabetes')
def blog_details1():
    return render_template('blog_details1.html')

@app.route('/apa-saja-sih-tipe-diabetes')
def blog_details2():
    return render_template('blog_details2.html')

@app.route('/waspadai-gejala-diabetes')
def blog_details3():
    return render_template('blog_details3.html')

@app.route('/cegah-diabetes-mulai-sekarang')
def blog_details4():
    return render_template('blog_details4.html')

@app.route('/bahaya-komplikasi-diabetes')
def blog_details5():
    return render_template('blog_details5.html')

@app.route('/hidup-normal-dengan-diabetes')
def blog_details6():
    return render_template('blog_details6.html')

# Halaman services utama
@app.route('/cek-kesehatan')
def services():
    return render_template('services.html')

# Service 1 = BMI
@app.route('/cek-bmi')
def services1():
    return render_template('services1.html')

# Service 2 = Diabetes
@app.route('/cek-diabetes')
def services2():
    return render_template('services2.html')

# Form cek diabetes (GET: tampilkan form, POST: prediksi hasil)
@app.route('/hasil-prediksi', methods=['POST'])
def predict_diabetes():
    data = [
        float(request.form['Pregnancies']),
        float(request.form['Glucose']),
        float(request.form['BloodPressure']),
        float(request.form['SkinThickness']),
        float(request.form['Insulin']),
        float(request.form['BMI']),
        float(request.form['DiabetesPedigreeFunction']),
        float(request.form['Age']),
    ]

    input_data = np.array(data).reshape(1, -1)
    prediction = model.predict(input_data)

    result = 'POSITIF Diabetes 😟' if prediction[0] > 0.5 else 'NEGATIF Diabetes 😄'
    return render_template('services2.html', prediction=result)

# Jalankan server Flask
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)