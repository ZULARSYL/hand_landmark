# ✋ Hand Landmark Detection with MediaPipe

Proyek ini menggunakan **[MediaPipe](https://developers.google.com/mediapipe)** untuk mendeteksi titik-titik (*landmarks*) pada tangan secara real-time.  
Cocok digunakan untuk pengembangan **gesture recognition**, **kontrol interaktif**, atau **aplikasi berbasis AI/Computer Vision** lainnya.

## 🚀 Fitur
- Deteksi tangan secara real-time dari kamera.
- Mendapatkan koordinat landmark tangan (21 titik).
- Bisa digunakan untuk mengenali gesture custom.
- Ringan dan cepat dijalankan di CPU.

## 📂 Struktur Proyek
Hand-Landmark/
│-- main.py # Script utama untuk menjalankan deteksi tangan
│-- requirements.txt # Daftar dependensi Python
└── README.md # Dokumentasi proyek

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

🛠 Dependensi
Pastikan requirements.txt berisi:

txt
Copy
Edit
mediapipe
opencv-python
Install manual jika perlu:

bash
Copy
Edit
pip install mediapipe opencv-python
▶️ Menjalankan Proyek
Jalankan script utama:

bash
Copy
Edit
python main.py
Jika berhasil, kamera akan terbuka dan titik-titik landmark tangan akan muncul di layar.

📸 Contoh Hasil

📚 Referensi
MediaPipe Hands Documentation

OpenCV Documentation
