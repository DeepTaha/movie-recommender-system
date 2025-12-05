# 🎬 Movie Recommender System

A content-based movie recommendation system built with Python and Streamlit. The system suggests similar movies based on genres, cast, crew, keywords, and plot descriptions using the TMDb 5000 Movie Dataset.

## 🌟 Features

- **Content-Based Filtering**: Recommends movies based on similarity in genres, cast, keywords, and overview
- **Interactive Web Interface**: Easy-to-use Streamlit app with dropdown selection
- **5000+ Movies**: Comprehensive dataset with diverse movie selections
- **Real-time Recommendations**: Instant suggestions based on your selection

## 🚀 Live Demo

Check out the live app: [Movie Recommender System](https://movie-recommender-system-krnjxdeutr8y47slimqujh.streamlit.app/)

## 📊 Dataset

This project uses the **TMDb 5000 Movie Dataset** which includes:
- Movie titles, overviews, and metadata
- Cast and crew information
- Genres and keywords
- 4,800+ movies after preprocessing

## 🛠️ Technology Stack

- **Python 3.13**
- **Streamlit** - Web framework
- **Pandas** - Data manipulation
- **Scikit-learn** - Machine learning (CountVectorizer, Cosine Similarity)
- **NumPy** - Numerical computations

## 📁 Project Structure
```
movie-recommender-system/
│
├── app.py                      # Main Streamlit application
├── recommender.py              # Recommendation engine logic
├── preprocess.py               # Data preprocessing pipeline
├── recommendation_engine.py    # Helper functions for recommendations
├── explore.py                  # Data exploration script
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
│
├── data/
│   ├── tmdb_5000_movies.csv   # Movie dataset
│   └── tmdb_5000_credits.csv  # Credits dataset
│
└── models/
    ├── movies_list.pkl         # Processed movie data
    ├── movies_processed.pkl    # Intermediate processed data
    └── similarity_matrix.pkl   # Cosine similarity matrix
```

## 🔧 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/DeepTaha/movie-recommender-system.git
cd movie-recommender-system
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Download the dataset
Download the TMDb 5000 dataset and place the CSV files in the `data/` folder:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

### 4. Preprocess the data
```bash
python preprocess.py
python recommender.py
```

### 5. Run the app
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 💡 How It Works

1. **Data Preprocessing**:
   - Merges movie and credits datasets
   - Extracts relevant features (genres, keywords, cast, director, overview)
   - Removes spaces and converts to lowercase
   - Combines all features into a single "tags" column

2. **Vectorization**:
   - Uses CountVectorizer to convert text tags into numerical vectors
   - Creates a 5000-feature vector for each movie

3. **Similarity Calculation**:
   - Computes cosine similarity between all movie vectors
   - Creates a 4806x4806 similarity matrix

4. **Recommendation**:
   - Finds the selected movie's similarity scores
   - Returns top 5 most similar movies

## 📈 Algorithm

The system uses **Content-Based Filtering** with **Cosine Similarity**:
```
Cosine Similarity = (A · B) / (||A|| × ||B||)
```

Where A and B are feature vectors of two movies. Higher similarity score means more similar movies.

## 🎯 Usage Example

1. Open the app
2. Select a movie from the dropdown (e.g., "Avatar")
3. Click "Get Recommendations"
4. View 5 similar movie suggestions

**Example Output for "The Dark Knight":**
- The Dark Knight Rises
- Batman Begins
- Batman Returns
- Batman Forever
- Batman & Robin

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**DeepTaha**
- GitHub: [@DeepTaha](https://github.com/DeepTaha)

## 🙏 Acknowledgments

- TMDb for providing the movie dataset
- Streamlit for the amazing web framework
- Scikit-learn for machine learning tools

## 📧 Contact

For questions or feedback, feel free to open an issue on GitHub.

---

⭐ If you found this project helpful, please give it a star!
