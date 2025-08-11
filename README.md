# ✋ Hand Landmark Detection with MediaPipe

Proyek ini menggunakan **[MediaPipe](https://developers.google.com/mediapipe)** untuk mendeteksi titik-titik (*landmarks*) pada tangan secara real-time.  
Cocok digunakan untuk pengembangan **gesture recognition**, **kontrol interaktif**, atau **aplikasi berbasis AI/Computer Vision** lainnya.
---
## 🚀 Fitur
- Deteksi tangan secara real-time dari kamera.
- Mendapatkan koordinat landmark tangan (21 titik).
- Bisa digunakan untuk mengenali gesture custom.
- Ringan dan cepat dijalankan di CPU.
---
## 📂 Struktur Proyek
- **`Hand-Landmark/`**
<pre> ```plaintext Hand-Landmark/ ├── src/ │ ├── main.py │ ├── requirements.txt └── README.md ``` </pre>
project-name/
├── src/
│   ├── main.py
│   ├── gesture_recognition.py
│   └── utils.py
├── images/
│   └── example.png
├── requirements.txt
└── README.md

---
## 📦 Instalasi
1. **Clone repository**
   ```bash
   git clone https://github.com/ZULARSYL/hand_landmark.git
   cd hand-landmark
2. **Buat Virtual Enviroment**
    python -m venv hand_landmark
    source hand_landmark/bin/activate   # MacOS/Linux
    hand_landmark\Scripts\activate      # Windows 
3. pip install -r requirements.txt

---
## 🛠️ Dependensi
Pastikan requirements.txt berisi:
mediapipe
opencv-python

Install manual(opsional)

pip install mediapipe opencv-python
▶️ Menjalankan Proyek

Jalankan script utama:
python main.py
Jika berhasil, kamera akan terbuka dan titik-titik landmark tangan akan muncul di layar.


---
## 📸 Dokumentasi Project

