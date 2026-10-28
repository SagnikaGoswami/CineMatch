
# 🎬 CineMatch

### Content-Based Movie Recommendation System

CineMatch is a movie recommendation web application built using **Python, Scikit-learn, and Streamlit**. It uses content-based filtering and cosine similarity to recommend movies based on their similarities in content and characteristics.

The application integrates the **TMDB API** to retrieve movie posters and features a modern, responsive interface developed with Streamlit and custom CSS.

## ✨ Features

- **Content-Based Recommendations:** Recommends five movies similar to a selected title.
- **Cosine Similarity:** Identifies relevant movies using a precomputed similarity matrix.
- **Movie Poster Integration:** Retrieves movie posters dynamically through the TMDB API.
- **Interactive Interface:** Provides a searchable movie selection dropdown.
- **Custom UI:** Features a dark-themed interface with responsive layouts and custom CSS.
- **Efficient Recommendations:** Uses serialized movie data and similarity scores for quick retrieval.

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Application development and recommendation logic |
| Scikit-learn | Feature vectorization and cosine similarity |
| Pandas & NumPy | Data preprocessing and manipulation |
| Streamlit | Web application interface |
| CSS | Custom UI styling |
| TMDB API | Movie poster retrieval |
| Pickle | Serialization of processed data and similarity matrix |
| Jupyter Notebook | Data preprocessing and model development |
| Git LFS | Storage of large model files |

## 🧠 Recommendation Methodology

CineMatch follows a **content-based filtering approach**, recommending movies based on similarities in their characteristics rather than user ratings or viewing history.

The recommendation pipeline involves:

1. **Data Collection:** Uses the TMDB 5000 Movie Dataset containing movie metadata and credits.
2. **Data Preprocessing:** Cleans and processes relevant movie attributes.
3. **Feature Extraction:** Converts movie-related information into numerical representations.
4. **Similarity Computation:** Calculates pairwise cosine similarity between movie vectors.
5. **Recommendation Generation:** Identifies the five most similar movies to the selected title.
6. **Poster Retrieval:** Fetches movie posters through the TMDB API and displays the results.

### Cosine Similarity

Cosine similarity measures the similarity between two vectors based on the cosine of the angle between them.

$$
\text{similarity}(A,B) =
\frac{A \cdot B}{\|A\|\|B\|}
$$

Higher similarity scores indicate greater similarity between the corresponding movie representations.

## 📁 Project Structure

```text
CineMatch/
├── app.py
├── style.css
├── movies.pkl
├── similarity.pkl
├── requirements.txt
├── .gitignore
├── .gitattributes
├── README.md
│
├── notebooks/
│   └── movie-recommender-system.ipynb
│
└── datasets/
    ├── tmdb_5000_movies.csv
    └── tmdb_5000_credits.csv
```

**Note:** The `similarity.pkl` file is managed using Git LFS because it exceeds GitHub's standard file size limit.

## 📊 Dataset

This project uses the [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata), which contains metadata for approximately 5,000 movies.

The dataset includes:

- Movie titles and descriptions
- Genres and keywords
- Cast and crew information
- Movie identifiers and additional metadata

These attributes are used to construct movie representations for similarity-based recommendations.

## 🚀 Installation and Setup

### Prerequisites

- Python 3.10 or later, with compatible dependencies
- Git and Git LFS
- TMDB API key

### 1. Clone the Repository

```bash
git lfs install
git clone https://github.com/SagnikaGoswami/CineMatch.git
cd CineMatch
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project's root directory and add your TMDB API key:

```env
TMDB_API_KEY=your_tmdb_api_key
```

You can obtain an API key from [The Movie Database](https://www.themoviedb.org/settings/api).

**Security:** The `.env` file is excluded from version control to prevent accidental exposure of API credentials.

### 5. Run the Application

```bash
streamlit run app.py
```

The application will launch locally in your browser.

## ☁️ Deployment

CineMatch is designed to be deployed using **Streamlit Community Cloud**.

Deployment requires connecting the GitHub repository, selecting `app.py` as the application entry point, and configuring the TMDB API key through Streamlit's Secrets management.

### Live Application

**[Live Demo](https://cinematch-ai-movie-finder.streamlit.app/)**

## 🔮 Future Improvements

- Genre-based filtering and advanced search
- Movie ratings and additional metadata
- User watchlists and favorites
- Hybrid recommendation approaches
- Recommendation quality evaluation
- Improved mobile user experience

## 🙏 Acknowledgements

- [TMDB](https://www.themoviedb.org/) — Movie metadata and poster API
- [Kaggle](https://www.kaggle.com/) — TMDB 5000 Movie Dataset
- [Scikit-learn](https://scikit-learn.org/) — Machine learning utilities
- [Streamlit](https://streamlit.io/) — Web application framework

## 👩‍💻 Author

**Sagnika Goswami**

[GitHub](https://github.com/SagnikaGoswami)

---

⭐ If you found this project useful, consider giving it a star.
