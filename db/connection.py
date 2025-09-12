import os 
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

#connects to the database (imports credentials)
def get_connection():
    conn = mysql.connector.connect(  
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password= os.getenv("DB_PASS"),
    database=os.getenv("DB_NAME")
)