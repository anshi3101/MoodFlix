# MoodFlix

An AI-powered Movie Recommendation System that provides personalized movie suggestions based on **Content Similarity**, **User Mood**, **Companion Preference**, and **Preferred Language**.

MoodFlix combines multiple recommendation strategies into a single intelligent pipeline to deliver recommendations that better match the user's current context instead of relying only on traditional similarity-based methods.

---

## Features

- Content-Based Movie Recommendation
- Mood-Aware Recommendation Engine
- Companion-Based Filtering
- Multi-Language Recommendation Support
- TMDB Movie Metadata Integration
- Official Trailer Support
- Wishlist Management
- Recently Viewed Movies
- Analytics Dashboard
- Responsive User Interface
- Modern Glassmorphism Design
- Fast Recommendation Pipeline
- Interactive Movie Detail Cards

---

## Recommendation Pipeline

```text
               User Input
                    │
                    ▼
      Content Similarity Engine
                    │
                    ▼
          Language Filtering
                    │
                    ▼
            Mood Filtering
                    │
                    ▼
        Companion Preference
                    │
                    ▼
           Ranking & Scoring
                    │
                    ▼
      Personalized Movie Results
```

---

## System Architecture

```text
                         User
                           │
                           ▼
                  Streamlit Frontend
                           │
                           ▼
               Recommendation Pipeline
                           │
      ┌────────────────────┼────────────────────┐
      │                    │                    │
      ▼                    ▼                    ▼
Content Engine       Mood Engine      Companion Engine
      │                    │                    │
      └──────────────┬─────┴────────────────────┘
                     ▼
             Language Engine
                     │
                     ▼
          Final Ranking & Scoring
                     │
                     ▼
            Personalized Results
                     │
                     ▼
              TMDB API Metadata
```

---

## Tech Stack

### Frontend

- Streamlit
- HTML
- CSS

### Backend

- Python

### Machine Learning

- Content-Based Recommendation
- Cosine Similarity
- NLP-Based Movie Tags
- Multi-Level Recommendation Pipeline

### Dataset

- TMDB 5000 Movies Dataset

### APIs

- TMDB API

### Libraries

- Pandas
- NumPy
- Scikit-learn
- Requests
- Pickle
- Gdown

---

## Project Structure

```text
MoodFlix/
│
├── app.py
├── content_based.py
├── pipeline_engine.py
├── movie_card.py
├── tmdb_service.py
│
├── mood_engine.py
├── companion_engine.py
├── language_engine.py
├── genre_profiles.py
│
├── dashboard.py
├── sidebar.py
├── wishlist.py
├── recent.py
│
├── styles/
│   └── style.css
│
├── movie_dict.pkl
├── similarity.pkl
├── tmdb_5000_movies.csv
│
└── README.md
```

---

## Recommendation Strategy

### 1. Content Similarity

The system first identifies movies that are semantically similar to the selected movie using cosine similarity.

### 2. Language Preference

Movies are prioritized according to the user's preferred language.

### 3. Mood Filtering

Recommendations are re-ranked based on the user's selected mood.

Supported moods include:

- Happy
- Sad
- Romantic
- Excited
- Relaxed
- Emotional
- Inspirational
- Thriller
- Family
- Adventure

### 4. Companion Filtering

Recommendations are further refined based on whom the user is watching with.

Available options include:

- Alone
- Friends
- Family
- Partner
- Kids

### 5. Final Ranking

The system combines similarity, mood score, companion score, and language score to generate the final recommendation list.

---

## Dashboard Features

- Total Movies
- Genre Distribution
- Language Distribution
- Average Runtime
- Average Rating
- Wishlist Statistics

---

## User Features

- Personalized Recommendations
- Movie Posters
- Runtime Information
- Ratings
- Genres
- Language Details
- Official Trailer
- Movie Overview
- Wishlist
- Recently Viewed Movies

---

## Installation

### Clone Repository

```bash
git clone https://github.com/anshi3101/MoodFlix
```

### Move into Project

```bash
cd MoodFlix
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## Dataset

This project uses the TMDB 5000 Movie Dataset.

Additional movie metadata including posters, trailers, cast, runtime, ratings, and overview are fetched dynamically using the TMDB API.

---

## Future Improvements

- Collaborative Filtering
- Hybrid Recommendation Engine
- User Authentication
- Personalized User Profiles
- Watch History Analytics
- AI Chat Assistant
- Recommendation Explainability
- Voice-Based Search
- Sentiment-Based Recommendation
- Streaming Platform Availability
- Multi-Modal Recommendation System

---

## Performance

- Fast Recommendation Pipeline
- Cached Movie Metadata
- Optimized Similarity Search
- Responsive UI
- Efficient API Calls

---

## Learning Outcomes

This project demonstrates practical implementation of:

- Recommendation Systems
- Content-Based Filtering
- Recommendation Pipelines
- Cosine Similarity
- Data Processing
- API Integration
- Streamlit Application Development
- Responsive UI Design
- Software Architecture
- User Experience Design

---

## License

This project is developed for educational and portfolio purposes.

---

## Author

**Anshi Srivastava**

AI & Machine Learning Developer

GitHub: https://github.com/anshi3101

LinkedIn: https://www.linkedin.com/in/anshi-srivastava31