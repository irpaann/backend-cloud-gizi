# API Chatbot dengan FastAPI, Firebase, dan Vertex AI

Proyek ini adalah API chatbot yang dibangun menggunakan FastAPI dengan integrasi Firebase Firestore untuk menyimpan riwayat chat dan Vertex AI untuk menghasilkan respons chatbot. API ini memungkinkan pengguna untuk berinteraksi dengan chatbot dan melihat riwayat percakapan mereka.

---

## Fitur

- *API Chatbot*: Mengirimkan prompt pengguna ke Vertex AI untuk menghasilkan respons.
- *Integrasi Firestore*: Menyimpan riwayat percakapan di Firestore, diorganisasikan berdasarkan ID pengguna.
- *Pengambilan Riwayat*: Mengambil riwayat percakapan untuk pengguna tertentu.
- *Skalabilitas dan Keamanan*: Dibangun dengan FastAPI dan Firebase untuk memastikan performa dan integritas data.

---

## Prasyarat

- Python 3.9 atau lebih tinggi
- Proyek Google Cloud dengan Vertex AI dan Firestore diaktifkan
- File kredensial Firebase Admin SDK (credentials.json)
- FastAPI dan pustaka Python yang diperlukan sudah diinstal

---

## Instalasi

1. *Kloning Repository*
   bash
   git clone https://github.com/your-repo-name/chatbot-api.git
   cd chatbot-api
   

2. *Buat Virtual Environment*
   bash
   python -m venv venv
   source venv/bin/activate  # Di Windows, gunakan `venv\Scripts\activate`
   

3. *Instal Dependensi*
   bash
   pip install -r requirements.txt
   

4. *Konfigurasi Kredensial Firebase*
   - Tambahkan file kredensial Firebase Admin SDK Anda ke direktori proyek.
   - Perbarui cred_path dalam kode ke jalur file credentials.json Anda.

5. *Setel Variabel Lingkungan*
   bash
   export GOOGLE_CLOUD_PROJECT="your-project-id"
   

6. *Inisialisasi Firestore dan Vertex AI*
   Pastikan Firestore dan Vertex AI telah dikonfigurasi dengan benar di proyek Google Cloud Anda.

---

## Menjalankan API

1. *Jalankan Server FastAPI*
   bash
   uvicorn main:app --reload
   
   API akan tersedia di http://127.0.0.1:8000.

2. *Uji Endpoint*

   - *POST /chatbot/*
     bash
     curl -X POST "http://127.0.0.1:8000/chatbot/" \
     -H "Content-Type: application/json" \
     -d '{"user_id": "user123", "prompt": "Halo!"}'
     

   - *GET /chatbot/history/*
     bash
     curl -X GET "http://127.0.0.1:8000/chatbot/history/?user_id=user123"
     

---

## Endpoint API

### POST /chatbot/
- *Deskripsi*: Mengirimkan prompt pengguna ke chatbot dan mengembalikan respons.
- *Request Body*:
  json
  {
      "user_id": "string",
      "prompt": "string"
  }
  
- *Respons*:
  json
  {
      "response": "string"
  }
  

### GET /chatbot/history/
- *Deskripsi*: Mengambil riwayat percakapan untuk pengguna tertentu.
- *Parameter Query*:
  - user_id: ID pengguna yang riwayat percakapannya ingin diambil.
- *Respons*:
  json
  {
      "user_id": "string",
      "chat_history": [
          {
              "user_prompt": "string",
              "bot_response": "string",
              "timestamp": "timestamp"
          }
      ]
  }
  

---

## Pengujian

### Pengujian Unit

1. **Instal pytest**
   bash
   pip install pytest
   

2. *Buat Pengujian*
   Tambahkan file test_main.py di direktori proyek:
   python
   from fastapi.testclient import TestClient
   from main import app

   client = TestClient(app)

   def test_chatbot():
       response = client.post("/chatbot/", json={"user_id": "testuser", "prompt": "Halo!"})
       assert response.status_code == 200
       assert "response" in response.json()

   def test_chat_history():
       response = client.get("/chatbot/history/?user_id=testuser")
       assert response.status_code == 200
       assert "chat_history" in response.json()
   

3. *Jalankan Pengujian*
   bash
   pytest
   

### Pengujian Manual

- Gunakan alat seperti Postman atau cURL untuk menguji endpoint API secara manual.

---

## Deployment

- Gunakan layanan seperti Google Cloud Run, AWS Lambda, atau VM tradisional untuk mendistribusikan aplikasi FastAPI.
- Pastikan konfigurasi variabel lingkungan dan kredensial dilakukan dengan aman.

---

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT. Lihat file [LICENSE](LICENSE) untuk detailnya.

---

## Kontribusi

Kontribusi sangat diterima! Silakan fork repository ini dan buat pull request untuk ditinjau.

---

## Kontak

Untuk pertanyaan atau dukungan, silakan hubungi your-email@example.com.# API Chatbot dengan FastAPI, Firebase, dan Vertex AI

Proyek ini adalah API chatbot yang dibangun menggunakan FastAPI dengan integrasi Firebase Firestore untuk menyimpan riwayat chat dan Vertex AI untuk menghasilkan respons chatbot. API ini memungkinkan pengguna untuk berinteraksi dengan chatbot dan melihat riwayat percakapan mereka.

---

## Fitur

- *API Chatbot*: Mengirimkan prompt pengguna ke Vertex AI untuk menghasilkan respons.
- *Integrasi Firestore*: Menyimpan riwayat percakapan di Firestore, diorganisasikan berdasarkan ID pengguna.
- *Pengambilan Riwayat*: Mengambil riwayat percakapan untuk pengguna tertentu.
- *Skalabilitas dan Keamanan*: Dibangun dengan FastAPI dan Firebase untuk memastikan performa dan integritas data.

---

## Prasyarat

- Python 3.9 atau lebih tinggi
- Proyek Google Cloud dengan Vertex AI dan Firestore diaktifkan
- File kredensial Firebase Admin SDK (credentials.json)
- FastAPI dan pustaka Python yang diperlukan sudah diinstal

---

## Instalasi

1. *Kloning Repository*
   bash
   git clone https://github.com/your-repo-name/chatbot-api.git
   cd chatbot-api
   

2. *Buat Virtual Environment*
   bash
   python -m venv venv
   source venv/bin/activate  # Di Windows, gunakan `venv\Scripts\activate`
   

3. *Instal Dependensi*
   bash
   pip install -r requirements.txt
   

4. *Konfigurasi Kredensial Firebase*
   - Tambahkan file kredensial Firebase Admin SDK Anda ke direktori proyek.
   - Perbarui cred_path dalam kode ke jalur file credentials.json Anda.

5. *Setel Variabel Lingkungan*
   bash
   export GOOGLE_CLOUD_PROJECT="your-project-id"
   

6. *Inisialisasi Firestore dan Vertex AI*
   Pastikan Firestore dan Vertex AI telah dikonfigurasi dengan benar di proyek Google Cloud Anda.

---

## Menjalankan API

1. *Jalankan Server FastAPI*
   bash
   uvicorn main:app --reload
   
   API akan tersedia di http://127.0.0.1:8000.

2. *Uji Endpoint*

   - *POST /chatbot/*
     bash
     curl -X POST "http://127.0.0.1:8000/chatbot/" \
     -H "Content-Type: application/json" \
     -d '{"user_id": "user123", "prompt": "Halo!"}'
     

   - *GET /chatbot/history/*
     bash
     curl -X GET "http://127.0.0.1:8000/chatbot/history/?user_id=user123"
     

---

## Endpoint API

### POST /chatbot/
- *Deskripsi*: Mengirimkan prompt pengguna ke chatbot dan mengembalikan respons.
- *Request Body*:
  json
  {
      "user_id": "string",
      "prompt": "string"
  }
  
- *Respons*:
  json
  {
      "response": "string"
  }
  

### GET /chatbot/history/
- *Deskripsi*: Mengambil riwayat percakapan untuk pengguna tertentu.
- *Parameter Query*:
  - user_id: ID pengguna yang riwayat percakapannya ingin diambil.
- *Respons*:
  json
  {
      "user_id": "string",
      "chat_history": [
          {
              "user_prompt": "string",
              "bot_response": "string",
              "timestamp": "timestamp"
          }
      ]
  }
  

---

## Pengujian

### Pengujian Unit

1. **Instal pytest**
   bash
   pip install pytest
   

2. *Buat Pengujian*
   Tambahkan file test_main.py di direktori proyek:
   python
   from fastapi.testclient import TestClient
   from main import app

   client = TestClient(app)

   def test_chatbot():
       response = client.post("/chatbot/", json={"user_id": "testuser", "prompt": "Halo!"})
       assert response.status_code == 200
       assert "response" in response.json()

   def test_chat_history():
       response = client.get("/chatbot/history/?user_id=testuser")
       assert response.status_code == 200
       assert "chat_history" in response.json()
   

3. *Jalankan Pengujian*
   bash
   pytest
   

### Pengujian Manual

- Gunakan alat seperti Postman atau cURL untuk menguji endpoint API secara manual.

---

## Deployment

- Gunakan layanan seperti Google Cloud Run, AWS Lambda, atau VM tradisional untuk mendistribusikan aplikasi FastAPI.
- Pastikan konfigurasi variabel lingkungan dan kredensial dilakukan dengan aman.

---

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT. Lihat file [LICENSE](LICENSE) untuk detailnya.

---

## Kontribusi

Kontribusi sangat diterima! Silakan fork repository ini dan buat pull request untuk ditinjau.

---

## Kontak

Untuk pertanyaan atau dukungan, silakan hubungi your-email@example.com.
