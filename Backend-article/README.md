# Article Backend Service

Backend service ini menyediakan berbagai fungsi untuk pengelolaan artikel, termasuk membuat, membaca, memperbarui, dan menghapus artikel. Selain itu, Anda dapat mengambil berita dari NewsAPI dan menyimpannya ke database.

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
