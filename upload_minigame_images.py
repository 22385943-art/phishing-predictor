import os
from pymongo import MongoClient
from gridfs import GridFS
from urllib.parse import quote_plus
from dotenv import load_dotenv


load_dotenv()
user = os.getenv("MONGO_USERNAME")
pw = os.getenv("PASSWORD")

username = quote_plus(user)
password = quote_plus(pw)

uri = f"mongodb+srv://{username}:{password}@cluster0.naqjxci.mongodb.net/?appName=Cluster0"
client = MongoClient(uri)
db = client["DB_Phishing"]
fs = GridFS(db)

IMAGE_FOLDER = "images" 
#Dependiendo del nombre de tu imagen detecta si es phishing o no para este caso. EJEMPLO: phishing1.png (phishing = True).
# nophishing1.png (phishing = False)

for filename in os.listdir(IMAGE_FOLDER):
    filepath = os.path.join(IMAGE_FOLDER, filename)

    if not os.path.isfile(filepath):
        continue

    is_phishing = filename.lower().startswith("phishing")

    with open(filepath, "rb") as f:
        file_id = fs.put(
            f,
            filename=filename,
            contentType="image/png" if filename.endswith(".png") else "image/jpeg"
        )

    db["minigame"].insert_one({
        "_id": file_id,
        "is_phishing": is_phishing
    })

    print(f"Subida: {filename} | phishing={is_phishing}")

print("Las imágenes se han subido correctamente.")
