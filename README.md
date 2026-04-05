# PINNE Backend (FastAPI)

Probabilistic Intelligent Network for Emergency (PINNE) — Backend System  
Built using FastAPI, MongoDB, and a modular service architecture.

---

## 🚀 Project Setup

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd <your-project-folder>
```

---

### 🐍 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
```

#### Windows:
```bash
venv\Scripts\activate
```

#### Mac/Linux:
```bash
source venv/bin/activate
```

---

### 📦 3️⃣ Install Dependencies

Make sure you have a `requirements.txt` file:

```
fastapi
uvicorn
python-dotenv
pymongo
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

### ⚙️ 4️⃣ Environment Configuration

Create a `.env` file in the root directory and add:

```
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/
```

Replace `<username>` and `<password>` with your MongoDB credentials.

Also add your .env to the .gitignore file so it would be pushed to the main branch

---

### ▶️ 5️⃣ Run the Server

```bash
uvicorn main:app --reload
```

Server will run at:

http://127.0.0.1:8000

---

## 📬 API Testing

### Swagger Docs (Recommended)

http://127.0.0.1:8000/docs

---

### Endpoint

POST /api/emergencies/assess (Do this using Postman API)

---

### Sample Request

```json
{
  "patient_id": "P001",
  "raw_symptoms": "I have chest pain and breathing difficulty",
  "location": {
    "latitude": 8.52,
    "longitude": 76.93
  }
}
```

---

## 🧠 Current Features

- FastAPI backend
- Modular service architecture
- Basic symptom extraction
- Dynamic emergency assessment pipeline
- MongoDB integration
- Severity classification
- Mock emergency response (hospital + dispatch)

---

## ⚠️ Notes

- MongoDB Atlas or local MongoDB must be running
- Ensure `.env` file is correctly configured
- Symptoms should match expected format (e.g., `chest_pain` internally)

---

## 🚧 Upcoming Enhancements

- Bayesian probability scoring
- Symptom ontology expansion
- SciSpacy-based NLP
- Patient registration system
- Real-time ambulance dispatch integration
