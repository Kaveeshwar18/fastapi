:::writing{variant=“standard” id=“48291”}

FastAPI Basic Project

📌 Description

This is a simple FastAPI project that demonstrates basic API development with input validation and logic processing.

🚀 Features
	•	Create and analyze posts
	•	Word count calculation
	•	Categorize content (Short / Medium / Long)
	•	REST API structure

🛠️ Tech Stack
	•	Python
	•	FastAPI
	•	Uvicorn
	•	Pydantic
  
▶️ How to Run

1. Install dependencies
pip install -r requirements.txt

2. Run the server
uvicorn main:app --reload

3. Open in browser
	•	API: http://127.0.0.1:8000
	•	Docs: http://127.0.0.1:8000/docs

📡 API Endpoints

Home
	•	GET /
	•	Returns API status

Analyze Post
	•	POST /analyze-post
	•	Input:
  {
  "title": "Example",
  "content": "This is a sample post"
}

Get Posts
	•	GET /posts
	•	Returns all posts
  
fastapi-basic/
│
├── main.py
├── model.py
├── service.py
├── requirements.txt
└── README.md
📖 Explanation
	•	main.py → Handles API routes
	•	model.py → Validates input data
	•	service.py → Contains logic and processing

👨‍💻 Author

Kaveeshwar
:::
