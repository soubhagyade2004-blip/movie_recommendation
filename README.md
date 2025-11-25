# 🎬 Movie Recommendation System

A simple and interactive **Streamlit web application** that recommends similar movies using machine learning and displays posters using the **TMDB API**.

---

## 🚀 Features
- Recommends **Top 5 similar movies**
- Fetches **high-quality posters** via TMDB
- Uses **cosine similarity** for movie comparison
- Fast and interactive UI made with **Streamlit**
- Loads preprocessed `.pkl` files for instant results

---

## 📁 Project Structure
```
├── app.py                # Main Streamlit app
├── movie_dict.pkl        # Movie data dictionary
├── similarity.pkl        # Cosine similarity matrix
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

---

## 🛠️ Tech Stack
- Python  
- Streamlit  
- Pandas  
- Requests  
- Pickle  
- TMDB API  

---

## 🧠 How It Works
1. User selects a movie  
2. App identifies the movie index  
3. Retrieves similarity scores  
4. Selects top 5 similar movies  
5. Fetches posters using TMDB API  
6. Displays the result beautifully in Streamlit  

---

## ▶️ Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2️⃣ Create and activate virtual environment

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit application
```bash
streamlit run app.py
```

---

## 🔑 TMDB API Key Setup
Sign up to get an API key → https://www.themoviedb.org/

Replace inside `app.py`:
```python
TMDB_KEY = "YOUR_API_KEY"
```

---

## 📝 Example Requirements
```
streamlit
pandas
requests
urllib3
```

---

## 📸 Screenshots  
<img width="1915" height="868" alt="image" src="https://github.com/user-attachments/assets/5d5e24ab-b3eb-4be3-ba39-805508cdb25e" />


---

## 🧩 Credits
- Dataset: **TMDB 5000 Movies Dataset**
- API Provider: **The Movie Database (TMDB)**

---

## ⭐ Support
If you like this project, please ⭐ star the repository!

