# Cloud Computing Repository (GIZI)

<p align="center">
  <a>
    <img alt="Gizi GIF" title="Gizi" src="GIZI_Animation.gif">
  </a>
</p>

# Article Backend Service GIZI

Backend service ini menyediakan berbagai fungsi untuk pengelolaan artikel, termasuk membuat, membaca, memperbarui, dan menghapus artikel.

URL base service ini adalah:  
`https://article-capstone-1005631098859.asia-southeast2.run.app`

---

## **Routes**


### **1. POST `/`**
- **Deskripsi:**  
  Endpoint root yang memberikan pesan selamat datang.
- **Respon Sukses:**
  ```json
  "Hello Selamat Datang, Silahkan coba fungsionalitas aplikasi artikel anda!!"


### **2. POST `/article/create`**
- **Deskripsi:**  
  Endpoint untuk membuat artikel baru secara manual.

- **Contoh Data yang dikirim:**
  ```json
   {
    "title": "Judul Artikel",
    "author": "Penulis Artikel",
    "description": "Deskripsi Artikel",
    "category": "Kategori Artikel",
    "content": "Konten Artikel",
    "publishedAt": "Tanggal Publikasi",
    "source": { "name": "Sumber Artikel" },
    "url": "URL Artikel",
    "urlToImage": "URL Gambar Artikel"
    }

  
- **Respon Sukses:**
  ```json
  {
  "msg": "Article added successfully",
  "article": {
    "title": "Judul Artikel",
    "author": "Penulis Artikel",
    "description": "Deskripsi Artikel",
    "category": "Kategori Artikel",
    "content": "Konten Artikel",
    "publishedAt": "Tanggal Publikasi",
    "source": { "name": "Sumber Artikel" },
    "url": "URL Artikel",
    "urlToImage": "URL Gambar Artikel"
    }
  }

- **Respon Error:**
  ```json
  { "error": "Failed to add manual article" }
  

### **3. GET `/articles`**
- **Deskripsi:**  
  Endpoint untuk mengambil semua artikel dari database.
- **Respon Sukses:**
  ```json
  [
    {
      "id": "articleId1",
      "title": "Judul Artikel",
      "author": "Penulis Artikel",
      "description": "Deskripsi Artikel",
      "content": "Konten Artikel",
      "publishedAt": "Tanggal Publikasi",
      "source": { "name": "Sumber Artikel" },
      "url": "URL Artikel",
      "urlToImage": "URL Gambar Artikel"
    }
  ]
- **Respon Error:**
  ```json
  { "error": "Failed to fetch articles" }

### **4. PUT `/articles/:id`**
- **Deskripsi:**  
  Endpoint untuk memperbarui artikel berdasarkan ID.
  
- **Data yang Dikirim:**  
  Data yang ingin diperbarui dalam format JSON.
  
- **Contoh Data yang Dikirim:**  
  Data yang ingin diperbarui dalam format JSON.
  ```json
  {
  "title": "Judul Artikel Update",
  "author": "Penulis Artikel Update"
  }
- **Respon Sukses:**
  ```json
  { 
    "msg": "Article with ID <id> has been updated successfully", 
    "updates": { ...updatedFields }
  }
- **Respon Error:**
  ```json
  { "error": "Failed to update article with ID <id>" }
### **5. DELETE `/articles/:id`**
- **Deskripsi:**  
  Endpoint untuk menghapus artikel berdasarkan ID.

- **Respon Sukses:**
  ```json
  { "msg": "Article with ID <id> has been deleted successfully" }
- **Respon Error:**
  ```json
  { "error": "Failed to delete article with ID <id>" }


# API Chatbot dengan FastAPI, Firebase, dan Vertex AI

Proyek ini adalah API chatbot yang dibangun menggunakan **FastAPI** dengan integrasi **Firebase Firestore** untuk menyimpan riwayat chat dan **Vertex AI** untuk menghasilkan respons chatbot. API ini memungkinkan pengguna untuk berinteraksi dengan chatbot dan melihat riwayat percakapan mereka.

---

## Fitur

- **API Chatbot**: Mengirimkan prompt pengguna ke Vertex AI untuk menghasilkan respons.
- **Integrasi Firestore**: Menyimpan riwayat percakapan di Firestore, diorganisasikan berdasarkan ID pengguna.
- **Pengambilan Riwayat**: Mengambil riwayat percakapan untuk pengguna tertentu.
- **Skalabilitas dan Keamanan**: Dibangun dengan FastAPI dan Firebase untuk memastikan performa dan integritas data.

---

## Prasyarat

- Python 3.9 atau lebih tinggi
- Proyek Google Cloud dengan **Vertex AI** dan **Firestore** diaktifkan
- File kredensial **Firebase Admin SDK** (`credentials.json`)
- FastAPI dan pustaka Python yang diperlukan sudah diinstal

---

## Instalasi

1. **Kloning Repository**
   ```bash
   git clone https://github.com/irpaann/backend-cloud-gizi.git
   cd backend-cloud-gizi/Fitur chatbot

2. *Buat Virtual Environment*
   ```bash
   python -m venv venv
   source venv/bin/activate  # Di Windows, gunakan `venv\Scripts\activate`

3. *Instal Dependensi*
   ```bash
   pip install -r requirements.txt

4. *Konfigurasi Kredensial Firebase*
   - Tambahkan file kredensial Firebase Admin SDK Anda ke direktori proyek.
   - Perbarui cred_path dalam kode ke jalur file credentials.json Anda.

5. *Setel Variabel Lingkungan*
   ```bash
   export GOOGLE_CLOUD_PROJECT="your-project-id"

6. *Inisialisasi Firestore dan Vertex AI*
   Pastikan Firestore dan Vertex AI telah dikonfigurasi dengan benar di proyek Google Cloud Anda.

---

## Menjalankan API

1. *Jalankan Server FastAPI*
   ```bash
   uvicorn main:app --reload ## API akan tersedia di http://127.0.0.1:8000.

2. *Uji Endpoint*

   - `POST /chatbot/`
     ```bash
     curl -X POST "http://127.0.0.1:8000/chatbot/" \
     -H "Content-Type: application/json" \
     -d '{"user_id": "user123", "prompt": "Halo!"}'

   - `GET /chatbot/history/`
     ```bash
     curl -X GET "http://127.0.0.1:8000/chatbot/history/?user_id=user123"

---

## Endpoint API

### POST /chatbot/
- *Deskripsi*: Mengirimkan prompt pengguna ke chatbot dan mengembalikan respons.
- `*Request Body*`:
  ```bash
  {
      "user_id": "string",
      "prompt": "string"
  }
  
- *Respons*:
  ```bash
  {
      "response": "string"
  }


### GET /chatbot/history/
- *Deskripsi*: Mengambil riwayat percakapan untuk pengguna tertentu.
- *Parameter Query*:
     ```bash
  user_id: ## ID pengguna yang riwayat percakapannya ingin diambil.
- *Respons*:
   ```bash  
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
   ```bash
   pip install pytest

2. *Buat Pengujian*
   Tambahkan file test_main.py di direktori proyek:
   ```bash
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
   ```bash
   pytest


### Pengujian Manual

- Gunakan alat seperti Postman atau cURL untuk menguji endpoint API secara manual.

---

## Deployment

- Gunakan layanan seperti Google Cloud Run, AWS Lambda, atau VM tradisional untuk mendistribusikan aplikasi FastAPI.
- Pastikan konfigurasi variabel lingkungan dan kredensial dilakukan dengan aman.

---

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT. Lihat file [LICENSE](Fiturr chatbot/LICENSE) untuk detailnya.

---

## Kontribusi

Kontribusi sangat diterima! Silakan fork repository ini dan buat pull request untuk ditinjau.

---

## Kontak

Untuk pertanyaan atau dukungan, silakan hubungi c206b4ky200@bangkit.academy. 