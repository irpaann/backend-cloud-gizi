# Article Backend Service

Backend service ini menyediakan berbagai fungsi untuk pengelolaan artikel, termasuk membuat, membaca, memperbarui, dan menghapus artikel. Selain itu, Anda dapat mengambil berita dari NewsAPI dan menyimpannya ke database.

URL base service ini adalah:  
`https://article-capstone-1005631098859.asia-southeast2.run.app`

---

## **Routes**

### **1. GET `/`**
- **Deskripsi:**  
  Endpoint root yang memberikan pesan selamat datang.
- **Respon Sukses:**
  ```json
  "Hello Selamat Datang, Silahkan coba fungsionalitas aplikasi artikel anda!!"
