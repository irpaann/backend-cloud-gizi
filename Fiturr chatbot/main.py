from fastapi import FastAPI, HTTPException, Query
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
cred_path = "your/path/credentials.json"
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
vertexai.init(project="your-project-id", location="your-location")
model = GenerativeModel(
    "projects/your-project-id/locations/your-location/endpoints/your-ednpoint-models"
)

# Model Pydantic untuk validasi input
class ChatRequest(BaseModel):
    user_id: str  # Tambahkan user_id untuk memisahkan data berdasarkan pengguna
    prompt: str   # Memastikan bahwa prompt adalah string

@app.post("/chatbot/")
async def chatbot(request: ChatRequest):
    try:
        # Mencetak log untuk memastikan data diterima
        print(f"Received prompt: {request.prompt} from user: {request.user_id}")
        
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
        
        # Simpan riwayat chat ke subkoleksi berdasarkan user_id
        db.collection("your-firestore-collections").document(request.user_id).collection("messages").add(chat_history)
        print(f"Chat history saved to Firestore for user {request.user_id}.")

        # Mengembalikan response dari model
        return {"response": response.text}
    
    except Exception as e:
        # Jika ada error, mengembalikan pesan error 500
        print(f"Error occurred: {str(e)}")  # Log error di server untuk debugging
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.get("/chatbot/history/")
async def get_chat_history(user_id: str = Query(..., description="User ID for filtering chat history")):
    """
    Mengambil riwayat chat berdasarkan user_id.
    """
    try:
        # Query riwayat chat berdasarkan user_id
        messages_ref = db.collection("chat_history").document(user_id).collection("messages")
        messages = messages_ref.order_by("timestamp", direction=firestore.Query.ASCENDING).stream()

        # Menyusun riwayat chat ke dalam list
        chat_history = [
            {
                "user_prompt": message.get("user_prompt"),
                "bot_response": message.get("bot_response"),
                "timestamp": message.get("timestamp"),
            }
            for message in messages
        ]

        # Mengembalikan riwayat chat
        if not chat_history:
            return {"message": "No chat history found for the given user_id."}
        return {"user_id": user_id, "chat_history": chat_history}
    
    except Exception as e:
        # Jika ada error, mengembalikan pesan error 500
        print(f"Error occurred while fetching chat history: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
