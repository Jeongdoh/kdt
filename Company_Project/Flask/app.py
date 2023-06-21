from flask import Flask, request, render_template
import csv
import numpy as np
from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity,pairwise_distances
from nltk.metrics import jaccard_distance


app = Flask(__name__)

def preprocess_text(text):
    okt = Okt()
    tokens = okt.morphs(text)
    return tokens

def calculate_jaccard_similarity(tokens1, tokens2):
    set1 = set(tokens1)
    set2 = set(tokens2)
    jaccard_similarity = 1 - jaccard_distance(set1, set2)
    return jaccard_similarity

@app.route('/', methods=['GET', 'POST'])
def calculate_similarity():
    if request.method == 'POST':
        # Get the uploaded CSV files
        fire1 = request.files['fire1']
        fire2 = request.files['fire2']
        
        # Get the selected similarity method
        similarity_method = request.form.get('similarityMethod')

        # Read the CSV files
        fire1_data = fire1.read().decode('utf-8-sig').splitlines()
        fire2_data = fire2.read().decode('utf-8-sig').splitlines()

        # Extract text from CSV data
        texts1 = [row.split(',')[0] for row in fire2_data]
        texts2 = [row.split(',')[0] for row in fire1_data]

        # Tokenize and preprocess texts
        preprocessed_texts1 = [' '.join(preprocess_text(txt1)) for txt1 in texts1]
        preprocessed_texts2 = [' '.join(preprocess_text(txt2)) for txt2 in texts2]

        # Generate TF-IDF vectors for the corpus
        vectorizer = TfidfVectorizer()
        tfidf1 = vectorizer.fit_transform(preprocessed_texts1)
        tfidf2 = vectorizer.transform(preprocessed_texts2)

        # Calculate similarity based on the selected method
        if similarity_method == 'cosine':
            similarity_scores = cosine_similarity(tfidf1, tfidf2)
        elif similarity_method == 'jaccard':
            similarity_scores = []
            for tokens1 in preprocessed_texts1:
                l = []
                for tokens2 in preprocessed_texts2:
                    similarity = calculate_jaccard_similarity(tokens1, tokens2)
                    l.append(similarity)
                similarity_scores.append(l)
        elif similarity_method == 'manhattan':
            similarity_scores = pairwise_distances(tfidf1, tfidf2, metric='manhattan')
        elif similarity_method == 'euclidean':
            similarity_scores = pairwise_distances(tfidf1, tfidf2, metric='euclidean')

        # Prepare the results
        results = []
        for i in range(len(similarity_scores)):
            score = similarity_scores[i]
            x = np.argmax(score)
            result = {
                'index': fire2_data[i].split(',')[1],
                'compared_text': fire1_data[x].split(',')[0],
                'title': preprocessed_texts1[i],
                'compared_index': fire1_data[x].split(',')[1],
                'similarity': score[x]
            }
            results.append(result)

        return render_template('results.html', results=results)

        # # Prepare the results
        # results = []
        # for i in range(len(similarity_scores)):
        #     score = similarity_scores[i]
        #     score = list(score)
        #     x = score.index(max(score))
        #     result = {
        #         'index': fire2_data[i].split(',')[1],
        #         'compared_text': fire1_data[x].split(',')[0],
        #         'title': ' '.join(preprocessed_texts1[i]),
        #         'compared_index': fire1_data[x].split(',')[1],
        #         'similarity': max(score)
        #     }
        #     results.append(result)

        # return render_template('results.html', results=results)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()





# from flask import Flask, request, render_template
# import csv
# import numpy as np
# from konlpy.tag import Okt
# from sklearn.feature_extraction.text import TfidfVectorizer
# from nltk.metrics import jaccard_distance
# from sklearn.metrics.pairwise import cosine_similarity,pairwise_distances

# app = Flask(__name__)

# def preprocess_text(text):
#     okt = Okt()
#     tokens = okt.morphs(text)
#     return tokens

# def calculate_jaccard_similarity(tokens1, tokens2):
#     set1 = set(tokens1)
#     set2 = set(tokens2)
#     jaccard_similarity = 1 - jaccard_distance(set1, set2)
#     return jaccard_similarity

# @app.route('/', methods=['GET', 'POST'])
# def calculate_similarity():
#     if request.method == 'POST':
#         # Get the uploaded CSV files
#         fire1 = request.files['fire1']
#         fire2 = request.files['fire2']
        
#         # Get the selected similarity method
#         similarity_method = request.form.get('similarityMethod')

#         # Read the CSV files
#         fire1_data = fire1.read().decode('utf-8-sig').splitlines()
#         fire2_data = fire2.read().decode('utf-8-sig').splitlines()

#         # Extract text from CSV data
#         texts1 = [row.split(',')[0] for row in fire2_data]
#         texts2 = [row.split(',')[0] for row in fire1_data]

#         # Tokenize and preprocess texts
#         preprocessed_texts1 = [preprocess_text(txt1) for txt1 in texts1]
#         preprocessed_texts2 = [preprocess_text(txt2) for txt2 in texts2]

#         # Calculate similarity based on the selected method
#         if similarity_method == 'cosine':
#             # Generate TF-IDF vectors for the corpus
#             vectorizer = TfidfVectorizer()
#             tfidf1 = vectorizer.fit_transform([' '.join(tokens) for tokens in preprocessed_texts1])
#             tfidf2 = vectorizer.transform([' '.join(tokens) for tokens in preprocessed_texts2])

#             # Calculate cosine similarity
#             similarity_scores = cosine_similarity(tfidf1, tfidf2)
#         elif similarity_method == 'jaccard':
#             similarity_scores = []
#             for tokens1 in preprocessed_texts1:
#                 l = []
#                 for tokens2 in preprocessed_texts2:
#                     similarity = calculate_jaccard_similarity(tokens1, tokens2)
#                     l.append(similarity)
#                 similarity_scores.append(l)
#         elif similarity_method == 'manhattan':
#             # Calculate Manhattan distance
#             similarity_scores = pairwise_distances(tfidf1, tfidf2, metric='manhattan')
#         elif similarity_method == 'euclidean':
#             # Calculate Euclidean distance
#             similarity_scores = pairwise_distances(tfidf1, tfidf2, metric='euclidean')

#         # Prepare the results
#         results = []
#         for i in range(len(similarity_scores)):
#             score = similarity_scores[i]
#             x = score.index(max(score))
#             result = {
#                 'index': fire2_data[i].split(',')[1],
#                 'compared_text': fire1_data[x].split(',')[0],
#                 'title': ' '.join(preprocessed_texts1[i]),
#                 'compared_index': fire1_data[x].split(',')[1],
#                 'similarity': max(score)
#             }
#             results.append(result)

#         return render_template('results.html', results=results)

#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run()
