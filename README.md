# Project Hand Landmark Detection with MediaPipe 🖐️

Proyek ini menggunakan **[MediaPipe](https://developers.google.com/mediapipe)** untuk mendeteksi titik-titik (*[landmarks](https://ai.google.dev/edge/mediapipe/solutions/vision/gesture_recognizer?hl=id)*) pada tangan secara real-time.  
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
  <pre>
   ├── main.py
   ├── requirements.txt
   └── README.md</pre>

---
## 📦 Instalasi
1. **Clone repository**
   ```bash
   git clone https://github.com/ZULARSYL/hand_landmark.git
   cd hand-landmark
   
2. **Buat Virtual Enviroment**
   ```bash
    python -m venv hand_landmark
    source hand_landmark/bin/activate   # MacOS/Linux
    hand_landmark\Scripts\activate      # Windows
   
3. **Install Dependensi**
   ```bash
    pip install -r requirements.txt   
---
## 🛠️ Dependensi 
- Pastikan requirments.text berisi :.
  ```text
  mediapipe
  opencv-python
- Jalankan Program.
  ```bash
  python main.py
jika berhasil, kamera akan terbuka 
---
## 📸 Dokumentasi Project

