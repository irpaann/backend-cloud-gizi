from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import vertexai
from vertexai.generative_models import GenerativeModel

import os
from google.auth.transport.requests import Request
from google.oauth2 import service_account

# Firebase Admin SDK
import firebase_admin
from firebase_admin import credentials, firestore

# Tentukan path ke file kredensial
cred_path = "path/to/credetials.json"
# Tentukan ID proyek
os.environ["GOOGLE_CLOUD_PROJECT"] = "your-project-id"

# Inisialisasi autentikasi dan verifikasi kredensial
credentials = service_account.Credentials.from_service_account_file(cred_path)

# Verifikasi kredensial
if credentials and credentials.valid:
    print("Kredensial valid dan siap digunakan.")
else:
    print("Kredensial tidak valid atau belum dikonfigurasi.")

# Inisialisasi Firebase Admin SDK
if not firebase_admin._apps:
    cred = credentials
    firebase_admin.initialize_app(cred)

# Inisialisasi Firestore
db = firestore.client()

# Inisialisasi aplikasi FastAPI
app = FastAPI()

# Inisialisasi Vertex AI
vertexai.init(project="1005631098859", location="us-central1")
model = GenerativeModel(
    "projects/your-project-id/locations/your-region/endpoints/your-endpoint-id"
)

# Model Pydantic untuk validasi input
class ChatRequest(BaseModel):
    prompt: str  # Memastikan bahwa prompt adalah string

@app.post("/chatbot/")
async def chatbot(request: ChatRequest):
    try:
        # Mencetak log untuk memastikan data diterima
        print(f"Received prompt: {request.prompt}")
        
        # Memulai chat dengan model
        chat = model.start_chat()
        
        # Mengirim pesan tanpa parameter 'temperature'
        response = chat.send_message(request.prompt)
        
        # Menyimpan riwayat chat ke Firestore
        chat_history = {
            "user_prompt": request.prompt,
            "bot_response": response.text,
            "timestamp": firestore.SERVER_TIMESTAMP,  # Menyimpan waktu otomatis dari server Firestore
        }
        
        # Simpan ke koleksi Firestore
        db.collection("chat_history").add(chat_history)
        print("Chat history saved to Firestore.")

        # Mengembalikan response dari model
        return {"response": response.text}
    
    except Exception as e:
        # Jika ada error, mengembalikan pesan error 500
        print(f"Error occurred: {str(e)}")  # Log error di server untuk debugging
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
