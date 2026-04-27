FASTAPI Basic Project

Description

This is a simple FastAPI project created to understand how APIs work.
It includes basic input validation, simple logic, and a clean structure.

Features
	•	Create and analyze posts
	•	Count number of words
	•	Categorize posts (Short / Medium / Long)
	•	Simple REST API

Tech Stack
	•	Python
	•	FastAPI
	•	Uvicorn
	•	Pydantic

How to Run
	1.	Install required packages:

pip install -r requirements.txt

	2.	Run the server:

uvicorn main:app --reload

	3.	Open in browser:

	•	API: http://127.0.0.1:8000
	•	Docs: http://127.0.0.1:8000/docs

API Endpoints
	•	GET /
Returns API status
	•	POST /analyze-post
Input example:

{
  "title": "Example",
  "content": "This is a sample post"
}

	•	GET /posts
Returns all posts

Project Structure

fastapi-basic/
│
├── main.py
├── model.py
├── service.py
├── requirements.txt
└── README.md

Explanation
	•	main.py → Handles API routes
	•	model.py → Defines input structure
	•	service.py → Contains logic
