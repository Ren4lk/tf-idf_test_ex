from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd


def get_tfidf_html_table(file_content, n_rows=50):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([file_content])
    feature_names = vectorizer.get_feature_names_out()
    idf = vectorizer.idf_
    tf = vectors.sum(axis=0).A1 / vectors.sum()

    df = pd.DataFrame({"TF": tf, "IDF": idf}, index=feature_names)
    df = df.sort_values(by=["IDF", "TF"], ascending=[False, False])
    df = df.head(n_rows)

    return df.to_html()
