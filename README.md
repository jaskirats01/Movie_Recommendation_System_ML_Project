# Movie Recommendation System · Training & Exploration

Content-based movie recommendations built with **TF-IDF and cosine similarity**. This repository contains the exploratory notebook and artifact-generation workflow used alongside the [Movie Recommendation App](https://github.com/jaskirats01/Movie_Recommendation_App).

**[Try the companion app](https://movie-recommend-jaskirat.streamlit.app/)** · [Reproduction and evaluation](docs/REPRODUCIBILITY.md) · [Open the notebook](Movie_Recommendation_System.ipynb)

## What the notebook implements

1. Load `movies_metadata.csv` and inspect missing values and duplicates.
2. Retain movie titles and metadata; parse genre names.
3. Combine **overview, genres and tagline** into a text representation.
4. Lowercase, remove punctuation/stopwords and lemmatize text.
5. Fit a TF-IDF vectorizer with unigrams/bigrams and a maximum of 50,000 features.
6. Rank other movies by cosine similarity to the selected title.
7. Export the processed data, title index, vectorizer and sparse matrix.

## Recorded dataset snapshot

| Item | Notebook output |
|---|---:|
| Input metadata rows | 45,466 |
| Final movie rows | 45,447 |
| TF-IDF feature columns | 50,000 |
| Sparse matrix non-zero entries | 1,548,114 |

**50,000 is the feature-column count, not the movie count.** The implemented text pipeline does not use cast, crew or keywords. Saved outputs are historical notebook results and should be regenerated when data or preprocessing changes.

## Run the notebook

```bash
git clone https://github.com/jaskirats01/Movie_Recommendation_System_ML_Project.git
cd Movie_Recommendation_System_ML_Project
python -m venv .venv
# Activate: source .venv/bin/activate (macOS/Linux)
# Activate: .venv\Scripts\Activate.ps1 (PowerShell)
python -m pip install pandas numpy matplotlib seaborn scikit-learn nltk jupyter
python -m notebook Movie_Recommendation_System.ipynb
```

Place the original `movies_metadata.csv` beside the notebook before running it. The CSV is not included, and its exact source/version is not recorded here. NLTK stopword and WordNet resources are downloaded by the notebook and require network access on the first run.

After running the preprocessing and model cells:

```python
recommend("Avatar", 5)
```

This returns similar titles from the loaded dataset. The notebook exports `df.pkl`, `indices.pkl`, `tfidf.pkl` and `tfidf_matrix.pkl` for the companion serving application.

## Scope and next steps

This is a content-similarity baseline, without personalized user-history modelling or a measured relevance benchmark. Next work should record dataset provenance, test duplicate-title handling, add a relevance evaluation set and measure query latency/memory. The current implementation computes similarity to the requested movie on demand rather than storing a full movie-by-movie similarity matrix.

Created by **Jaskirat Singh**.
