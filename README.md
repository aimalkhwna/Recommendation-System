# 🎬 Movie Recommendation System

A **Content-Based Movie Recommendation System** built using **Python**, **Pandas**, **NumPy**, and **Scikit-learn**. The system recommends movies similar to a selected movie by analyzing metadata such as genres, keywords, cast, crew, and movie overview.

---

## 📌 Features

* Recommends the **Top 5 similar movies**
* Uses **Content-Based Filtering**
* Text preprocessing using **NLTK**
* Vectorization using **CountVectorizer**
* Similarity computation using **Cosine Similarity**
* Fast recommendation generation using a precomputed similarity matrix

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* Jupyter Notebook

---

## 📂 Dataset

This project uses **The Movie Database (TMDB) 5000 Movies Dataset**.

Files used:

* `tmdb_5000_movies.csv`
* `tmdb_5000_credits.csv`

Dataset Source:
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

---

## ⚙️ Project Workflow

1. Load movie and credits datasets.
2. Merge datasets using movie title.
3. Select relevant features:

   * Genres
   * Keywords
   * Cast
   * Crew (Director)
   * Overview
4. Handle missing values.
5. Convert JSON-like columns into lists.
6. Remove spaces from multi-word names.
7. Combine all textual information into a single **tags** column.
8. Perform text preprocessing:

   * Lowercase conversion
   * Tokenization
   * Stemming using PorterStemmer
9. Convert text into numerical vectors using **CountVectorizer**.
10. Calculate **Cosine Similarity** between all movie vectors.
11. Recommend the most similar movies.

---

## 🧠 Recommendation Logic

```python
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    for i in movie_list:
        print(movies.iloc[i[0]].title)
```

---

## 📊 Machine Learning Concepts Used

* Natural Language Processing (NLP)
* Feature Engineering
* Count Vectorization
* Cosine Similarity
* Content-Based Recommendation Systems

---

## 📁 Project Structure

```
Movie-Recommendation-System/
│
├── Movie Recommendation System.ipynb
├── movies.pkl
├── similarity.pkl
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── requirements.txt
├── README.md
└── images/
    └── demo.png
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Movie-Recommendation-System.git
```

Move into the project directory:

```bash
cd Movie-Recommendation-System
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Jupyter Notebook:

```bash
jupyter notebook
```

---

## 💡 Example

Input:

```
Avatar
```

Output:

```
Guardians of the Galaxy
Aliens
John Carter
Titan A.E.
Battle: Los Angeles
```

*(Recommendations may vary depending on preprocessing and vectorization settings.)*

---

## 🔮 Future Improvements

* Build an interactive web application using Streamlit.
* Display movie posters using the TMDB API.
* Add movie search with autocomplete.
* Recommend movies based on genres, actors, or directors.
* Implement hybrid recommendation techniques combining content-based and collaborative filtering.
* Deploy the application on Streamlit Cloud, Render, or Hugging Face Spaces.

---

## 👨‍💻 Author

**Aimal Khan**

* Computer Science Student
* Machine Learning & Deep Learning Enthusiast
* Interested in AI, Computer Vision, and Recommendation Systems

---

## ⭐ If you found this project useful

Please consider giving this repository a **⭐ Star** on GitHub if it helped you learn about recommendation systems or inspired your own projects.

