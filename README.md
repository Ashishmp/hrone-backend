HROne Backend Task
This is a FastAPI-based backend application built for the HROne Backend Intern Hiring Task. It provides APIs for managing products and orders, including user-specific order listings and product filtering.


🚀 Tech Stack
- Framework: FastAPI
- Database: MongoDB (MongoDB Atlas)
- Deployment: Railway 
- Environment: Python 3.10+ (using venv)

  
🛠️ Setup Instructions

1. Clone the Repository

git clone https://github.com/Ashishmp/hrone-backend.git

cd hrone-backend

2. Activate the Virtual Environment

On Windows:
cd venv\Scripts
./activate


3. Install Dependencies 

pip install -r requirements.txt

4. Create a .env File

In the root directory:
MONGODB_URI=<your_mongodb_connection_uri> // add your own I have added mine

DATABASE_NAME=<your_database_name> // add your own I have added mine

5. Run the Server

uvicorn app.main:app --reload

App URL: http://127.0.0.1:8000  // need to modify port to host on railway.
Docs: http://127.0.0.1:8000/docs 
