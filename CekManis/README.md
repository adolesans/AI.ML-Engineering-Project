# 🍯 CekManis - Diabetes Risk Prediction & Education Platform

<div align="center">
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen" alt="Status">
  <img src="https://img.shields.io/badge/Python-3.8+-blue" alt="Python">
  <img src="https://img.shields.io/badge/Flask-2.0+-red" alt="Flask">
  <img src="https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange" alt="ML">
  <img src="https://img.shields.io/badge/Deployment-Railway-purple" alt="Deployment">
</div>

## 📋 Deskripsi Proyek

**CekManis** adalah platform web terintegrasi yang menggabungkan teknologi machine learning dengan edukasi kesehatan komprehensif untuk membantu masyarakat dalam deteksi dini dan pencegahan diabetes melitus.

### 🎯 Tujuan Utama
- **Prediksi Risiko**: Menggunakan model AI untuk memprediksi risiko diabetes berdasarkan faktor medis
- **Edukasi Kesehatan**: Menyediakan informasi lengkap tentang gejala, penanganan, dan pencegahan diabetes
- **Aksesibilitas**: Memberikan akses mudah terhadap layanan kesehatan digital
- **Pemberdayaan Masyarakat**: Meningkatkan kesadaran dan mendorong perubahan perilaku sehat
- **Prediksi BMI**: Menggunakan prehitungan matematis untuk memprediksi BMI pada seseorang beserta kategori BMI nya

## 🌟 Fitur Utama

### 🔮 Prediksi Risiko Diabetes
- Model machine learning yang akurat untuk prediksi risiko
- Input parameter medis: glukosa, BMI, usia, tekanan darah, dll.

### 📚 Edukasi Kesehatan Komprehensif
- Informasi lengkap tentang diabetes melitus
- Panduan gejala dan tanda-tanda awal

### 💻 Antarmuka User-Friendly
- Desain responsif untuk semua perangkat
- Navigasi yang intuitif dan mudah digunakan

## 🚀 Demo

**🌐 Live Demo**: [https://cekmanis-production.up.railway.app/](https://cekmanis-production.up.railway.app/)

## 🛠️ Teknologi yang Digunakan

- **Backend**: Python Flask
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap
- **Deployment**: Railway

## 📊 Dataset

Proyek ini menggunakan dataset **Pima Indians Diabetes Database** dari UCI Machine Learning Repository.

**📁 Link Dataset**: [Kaggle - Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

### Fitur Dataset:
- Pregnancies: Jumlah kehamilan
- Glucose: Konsentrasi glukosa plasma
- BloodPressure: Tekanan darah diastolik
- SkinThickness: Ketebalan lipatan kulit trisep
- Insulin: Insulin serum 2 jam
- BMI: Indeks massa tubuh
- DiabetesPedigreeFunction: Fungsi silsilah diabetes
- Age: Usia
- Outcome: Variabel target (0 = non-diabetes, 1 = diabetes)

## 🏃‍♂️ Cara Menjalankan Proyek Secara Lokal

### Prasyarat
- Python 3.8 atau lebih baru
- pip (Python package manager)
- Git (optional)

### Langkah Instalasi

1. **Clone Repository**
   ```bash
   git clone https://github.com/Ryan-Rachmad-Hidayat/CekManis.git
   cd CekManis
   ```

2. **Buat Virtual Environment** (Recommended)
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan Aplikasi**
   ```bash
   python app.py
   ```

### Struktur Proyek
```
CekManis/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── diabetes_model.pkl     # Machine learning models
├── templates/            # HTML templates
│   ├── index.html
│   ├── about.html
│   └── services.html
│   └── services1.html
│   └── services2.html
│   └── blog.html
│   └── blog_details1.html
│   └── blog_details2.html
│   └── blog_details3.html
│   └── blog_details4.html
│   └── blog_details5.html
│   └── blog_details6.html
├── static/              # CSS, JS, dll
│   ├── css/
│   ├── js/
│   └── images/
│   └── scss/
│   └── fonts/
└── README.md
```

<div align="center">
  <p><strong>Dibuat dengan ❤️ untuk kesehatan masyarakat Indonesia</strong></p>
  <p><em>"Deteksi Dini, Hidup Lebih Sehat"</em></p>
</div>
