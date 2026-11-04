from dotenv import load_dotenv
import os
load_dotenv()
print(f"Mot de passe : {os.getenv('API_KEY')}")