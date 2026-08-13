# 🎬 Movie Recommender System

A smart web application that recommends 5 similar movies based on user input. Built with machine learning algorithms to help users discover movies faster without spending hours searching.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [How It Works](#how-it-works)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Algorithm Details](#algorithm-details)
- [Data Source](#data-source)
- [Contributing](#contributing)

## 🎯 Overview

The Movie Recommender System is designed to solve the problem of choice paralysis when searching for movies to watch. By leveraging machine learning and the TMDB (The Movie Database) API, it analyzes movie metadata and recommends 5 similar films based on user input.

**Problem It Solves:**
- Reduces time spent searching for similar movies
- Provides personalized recommendations based on similarity metrics
- Displays movie posters and details for quick visual reference

## ✨ Features

- **Smart Recommendations**: Get 5 similar movies with a single search
- **Visual Display**: Movie posters and titles for easy browsing
- **Real Movie Data**: Uses TMDB database with extensive movie information
- **Fast Processing**: Efficient similarity calculations using cosine similarity
- **User-Friendly Interface**: Simple web-based interface for easy interaction

## 🔍 How It Works

1. **User Input**: Enter the name of a movie you like
2. **Data Processing**: The system extracts movie metadata from TMDB database
3. **Vector Generation**: Movie features are converted into numerical vectors using CountVectorizer
4. **Similarity Calculation**: Cosine Similarity compares the input movie with all other movies
5. **Results**: Top 5 most similar movies are displayed with posters and details

### Algorithm Flow

```
User Input → TMDB Database Lookup → Feature Extraction → 
Vector Generation → Cosine Similarity Calculation → 
Sort by Similarity Score → Display Top 5 Results
```

## 🛠 Technologies Used

| Technology | Purpose |
|-----------|---------|
| **Python** | Core programming language |
| **Flask/Streamlit** | Web framework for UI |
| **TMDB API** | Movie database and metadata |
| **scikit-learn** | Machine learning library |
| **CountVectorizer** | Text feature extraction |
| **Cosine Similarity** | Similarity metric calculation |
| **Pandas/NumPy** | Data manipulation and processing |

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- TMDB API Key (get one from [themoviedb.org](https://www.themoviedb.org/settings/api))

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/ren555542L/MovieRecommenderSystem.git
   cd MovieRecommenderSystem
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your TMDB API Key**
   - Create a `.env` file in the root directory
   - Add your API key: `TMDB_API_KEY=your_api_key_here`

5. **Run the application**
   ```bash
   python app.py
   # or if using Streamlit:
   streamlit run app.py
   ```

6. **Access the application**
   - Open your browser and navigate to `http://localhost:5000` (Flask) or `http://localhost:8501` (Streamlit)

## 🚀 Usage

1. Open the web application in your browser
2. Enter the name of a movie you enjoy in the search box
3. Click the "Recommend" or "Get Recommendations" button
4. View the 5 similar movies displayed with:
   - Movie title
   - Movie poster
   - Additional details (rating, release year, etc.)
5. Click on a movie to learn more or add to watchlist

### Example
```
Input: "The Shawshank Redemption"
Output: 
  1. The Green Mile
  2. Forrest Gump
  3. The Godfather
  4. Pulp Fiction
  5. Inception
```

## 📁 Project Structure

```
MovieRecommenderSystem/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (API keys)
├── data/
│   └── movies.csv        # Movie dataset (preprocessed)
├── models/
│   └── vectorizer.pkl    # Saved CountVectorizer model
├── templates/
│   └── index.html        # Web interface
├── static/
│   ├── css/
│   └── js/
├── utils/
│   └── tmdb_api.py       # TMDB API integration
└── README.md             # This file
```

## 🧠 Algorithm Details

### CountVectorizer
- **Purpose**: Converts movie features (genres, cast, keywords, plot) into numerical vectors
- **How it works**: Creates a sparse matrix where each dimension represents a unique word/feature
- **Benefit**: Allows mathematical comparison between movies

### Cosine Similarity
- **Formula**: similarity = (A · B) / (||A|| × ||B||)
- **Range**: 0 to 1 (1 = identical, 0 = completely different)
- **Advantage**: Works well with high-dimensional data and text features
- **Result**: Provides a score for each movie's similarity to the input

### Data Processing
1. **Feature Selection**: Genres, cast, keywords, plot summary, budget, revenue
2. **Text Preprocessing**: Lowercase, tokenization, stopword removal
3. **Vector Creation**: Convert text features into numerical representations
4. **Normalization**: Scale similarity scores for consistent comparisons

## 📊 Data Source

- **Database**: The Movie Database (TMDB)
- **API**: [TMDB API v3](https://developers.themoviedb.org/3)
- **Coverage**: 500,000+ movies and TV shows
- **Update Frequency**: Regularly updated with new releases

**Note**: The project uses TMDB API to fetch movie data in real-time. A free API key is required.

## 🎓 Learning Resources

- [Cosine Similarity Explained](https://en.wikipedia.org/wiki/Cosine_similarity)
- [CountVectorizer Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html)
- [TMDB API Documentation](https://developers.themoviedb.org/3)

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a new branch: `git checkout -b feature/YourFeature`
3. **Make** your changes and commit: `git commit -m 'Add YourFeature'`
4. **Push** to the branch: `git push origin feature/YourFeature`
5. **Submit** a Pull Request

### Areas for Contribution
- Improve recommendation algorithm accuracy
- Add user preferences/filtering options
- Implement collaborative filtering
- Enhance UI/UX design
- Add more data sources
- Optimize performance

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**ren555542L**  
GitHub: [@ren555542L](https://github.com/ren555542L)

## 🔗 Links

- [TMDB API](https://www.themoviedb.org/settings/api)
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Python Official Documentation](https://docs.python.org/3/)

## 📞 Support

For issues, questions, or suggestions:
- Open an [Issue](https://github.com/ren555542L/MovieRecommenderSystem/issues)
- Check existing documentation
- Review similar projects for reference

---

**⭐ If you found this project helpful, please consider giving it a star!**

---

*Last Updated: August 2026*
