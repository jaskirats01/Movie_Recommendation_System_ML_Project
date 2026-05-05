🎬 Movie Recommendation System (ML)

A content-based movie recommendation system built using machine learning techniques on a dataset of 50,000+ movies. This project demonstrates how to transform raw movie metadata into meaningful recommendations using natural language processing and similarity measures.

🚀 Overview

This project focuses on building a scalable recommendation engine by leveraging text-based features such as:

Genres
Keywords
Cast
Crew

These features are combined into a unified representation and processed using TF-IDF vectorization, followed by cosine similarity to identify similar movies.

🧠 Key Features
🔹 Content-based filtering approach
🔹 Handles 50K+ movies dataset efficiently
🔹 Advanced feature engineering pipeline
🔹 Uses TF-IDF for vectorization
🔹 Computes similarity using cosine similarity
🔹 Generates Top-N similar movie recommendations
🛠️ Tech Stack
Python
Pandas, NumPy
Scikit-learn
NLP (TF-IDF Vectorization)
⚙️ Workflow
Data Collection
Movie dataset containing metadata (genres, keywords, cast, crew)
Data Preprocessing
Handling missing values
Parsing JSON-like columns
Cleaning and normalizing text
Feature Engineering
Combining relevant features into a single “tags” column
Tokenization & text normalization
Vectorization
Applying TF-IDF to convert text into numerical vectors
Similarity Computation
Using cosine similarity to measure closeness between movies
Recommendation Function
Returns top-N similar movies based on input title
📊 Dataset
Size: 50,000+ movies
Attributes used:
Title
Genres
Keywords
Cast
Crew
🎯 Example
recommend("Inception")

Output:

Interstellar
The Dark Knight
Tenet
Prestige
...
📈 Highlights
Built a high-dimensional similarity matrix for large-scale data
Efficient lookup for generating recommendations
Demonstrates real-world application of NLP + ML in recommender systems
🔮 Future Improvements
Add collaborative filtering (hybrid system)
Improve recommendations using deep learning
Optimize for faster similarity search (e.g., FAISS)
Deploy as API or web application
👨‍💻 Author

Jaskirat Singh

⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!
