from flask import Flask, request, render_template
import pandas as pd
from io import StringIO
import csv
import numpy as np
import matplotlib.pyplot as plt
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



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/introduce', methods=['GET'])
def introduce():
    return render_template('introduce.html')

@app.route('/code', methods=['POST','GET'])
def code():
    if request.method == 'POST':
        fire1 = request.files['fire1']
        fire1_df = pd.read_csv(fire1)
        fire2 = request.files['fire2']
        fire2_df = pd.read_csv(fire2)
        similarity_method = request.form.get('similarityMethod')

        # Read the CSV files
        # fire1_data = fire1.read().decode('utf-8-sig').splitlines()
        # fire2_data = fire2.read().decode('utf-8-sig').splitlines()

        # Extract text from CSV data
        # texts1 = [row.split(',')[0] for row in fire2_data]
        # texts2 = [row.split(',')[0] for row in fire1_data]

        # # Tokenize and preprocess texts
        # preprocessed_texts1 = [' '.join(preprocess_text(txt1)) for txt1 in texts1]
        # preprocessed_texts2 = [' '.join(preprocess_text(txt2)) for txt2 in texts2]

        # # Generate TF-IDF vectors for the corpus
        # vectorizer = TfidfVectorizer()
        # tfidf1 = vectorizer.fit_transform(preprocessed_texts1)
        # tfidf2 = vectorizer.transform(preprocessed_texts2)




        # Calculate similarity based on the selected method
        if similarity_method == 'cosine':
            # Extract text from CSV data
            texts1=[]
            for i in range(fire2_df.shape[0]):
                texts1.append(fire2_df.iloc[i,0])
            texts2=[]
            for i in range(fire1_df.shape[0]):
                texts2.append(fire1_df.iloc[i,0])


            # Tokenize and preprocess texts
            preprocessed_texts1 = [' '.join(preprocess_text(txt1)) for txt1 in texts1]
            preprocessed_texts2 = [' '.join(preprocess_text(txt2)) for txt2 in texts2]

            # Generate TF-IDF vectors for the corpus
            vectorizer = TfidfVectorizer()
            tfidf1 = vectorizer.fit_transform(preprocessed_texts1)
            tfidf2 = vectorizer.transform(preprocessed_texts2)

            similarity_scores = cosine_similarity(tfidf1, tfidf2)

            # Prepare the results
            match_list = []
            match_cnt = 0
            results = []
            for i in range(len(similarity_scores)):
                score = similarity_scores[i]
                x = np.argmax(score)
                match_status = "일치" if fire2_df.iloc[i, 1] == fire1_df.iloc[x, 1] else "불일치"
                if match_status == '일치':
                    match_cnt += 1
                match_list.append(match_status)
                # if match_status == "일치":
                #     method.append(max(score))
                # reconstructed_title = ' '.join(preprocessed_texts1[i])
                result = {
                    'compared_index': fire1_df.iloc[x,1],
                    'index': fire2_df.iloc[i,1],
                    'compared_text': fire1_df.iloc[x,0],
                    'title': fire2_df.iloc[i,0],
                    'similarity': round(score[x],3),
                    'match': match_status
                }
            
                results.append(result)
            match_ratio = round(match_cnt/(len(match_list)),4)    
            return render_template('results.html', results=results, match_ratio=match_ratio)


        elif similarity_method == 'jaccard':
            # Extract text from CSV data
            texts1=[]
            for i in range(fire2_df.shape[0]):
                texts1.append(fire2_df.iloc[i,0])
            texts2=[]
            for i in range(fire1_df.shape[0]):
                texts2.append(fire1_df.iloc[i,0])


            # Tokenize and preprocess texts
            preprocessed_texts1 = [preprocess_text(txt1) for txt1 in texts1]
            preprocessed_texts2 = [preprocess_text(txt2) for txt2 in texts2]


            similarity_scores = []
            for tokens1 in preprocessed_texts1:
                l = []
                for tokens2 in preprocessed_texts2:
                    similarity = calculate_jaccard_similarity(tokens1, tokens2)
                    l.append(similarity)
                similarity_scores.append(l)

            # Prepare the results
            match_list = []
            match_cnt = 0
            results = []
            for i in range(len(similarity_scores)):
                score = similarity_scores[i]
                x = np.argmax(score)
                match_status = "일치" if fire2_df.iloc[i, 1] == fire1_df.iloc[x, 1] else "불일치"
                if match_status == '일치':
                    match_cnt += 1
                match_list.append(match_status)
                # if match_status == "일치":
                #     method.append(max(score))
                # reconstructed_title = ' '.join(preprocessed_texts1[i])
                result = {
                    'compared_index': fire1_df.iloc[x,1],
                    'index': fire2_df.iloc[i,1],
                    'compared_text': fire1_df.iloc[x,0],
                    'title': fire2_df.iloc[i,0],
                    'similarity': round(score[x],3),
                    'match': match_status
                }
            
                results.append(result)
            match_ratio = round(match_cnt/(len(match_list)),4)
            return render_template('results.html', results=results, match_ratio=match_ratio)


        elif similarity_method == 'manhattan':
            # Extract text from CSV data
            texts1=[]
            for i in range(fire2_df.shape[0]):
                texts1.append(fire2_df.iloc[i,0])
            texts2=[]
            for i in range(fire1_df.shape[0]):
                texts2.append(fire1_df.iloc[i,0])


            # Tokenize and preprocess texts
            preprocessed_texts1 = [' '.join(preprocess_text(txt1)) for txt1 in texts1]
            preprocessed_texts2 = [' '.join(preprocess_text(txt2)) for txt2 in texts2]


            # Extract text from CSV data
            texts1=[]
            for i in range(fire2_df.shape[0]):
                texts1.append(fire2_df.iloc[i,0])
            texts2=[]
            for i in range(fire1_df.shape[0]):
                texts2.append(fire1_df.iloc[i,0])


            # Tokenize and preprocess texts
            preprocessed_texts1 = [' '.join(preprocess_text(txt1)) for txt1 in texts1]
            preprocessed_texts2 = [' '.join(preprocess_text(txt2)) for txt2 in texts2]

            # Generate TF-IDF vectors for the corpus
            vectorizer = TfidfVectorizer()
            tfidf1 = vectorizer.fit_transform(preprocessed_texts1)
            tfidf2 = vectorizer.transform(preprocessed_texts2)

            similarity_scores = pairwise_distances(tfidf1, tfidf2, metric='manhattan')

            # Prepare the results
            match_list = []
            match_cnt = 0
            results = []
            for i in range(len(similarity_scores)):
                score = similarity_scores[i]
                x = np.argmax(score)
                match_status = "일치" if fire2_df.iloc[i, 1] == fire1_df.iloc[x, 1] else "불일치"
                if match_status == '일치':
                    match_cnt += 1
                match_list.append(match_status)
                # if match_status == "일치":
                #     method.append(max(score))
                # reconstructed_title = ' '.join(preprocessed_texts1[i])
                result = {
                    'compared_index': fire1_df.iloc[x,1],
                    'index': fire2_df.iloc[i,1],
                    'compared_text': fire1_df.iloc[x,0],
                    'title': fire2_df.iloc[i,0],
                    'similarity': round(score[x],3),
                    'match': match_status
                }
            
                results.append(result)
            match_ratio = round(match_cnt/(len(match_list)),4)  
            return render_template('results.html', results=results, match_ratio=match_ratio)



        elif similarity_method == 'euclidean':
            # Extract text from CSV data
            texts1=[]
            for i in range(fire2_df.shape[0]):
                texts1.append(fire2_df.iloc[i,0])
            texts2=[]
            for i in range(fire1_df.shape[0]):
                texts2.append(fire1_df.iloc[i,0])


            # Tokenize and preprocess texts
            preprocessed_texts1 = [' '.join(preprocess_text(txt1)) for txt1 in texts1]
            preprocessed_texts2 = [' '.join(preprocess_text(txt2)) for txt2 in texts2]

            # Generate TF-IDF vectors for the corpus
            vectorizer = TfidfVectorizer()
            tfidf1 = vectorizer.fit_transform(preprocessed_texts1)
            tfidf2 = vectorizer.transform(preprocessed_texts2)
            similarity_scores = pairwise_distances(tfidf1, tfidf2, metric='euclidean')

            # Prepare the results
            match_list = []
            match_cnt = 0
            results = []
            for i in range(len(similarity_scores)):
                score = similarity_scores[i]
                x = np.argmax(score)
                match_status = "일치" if fire2_df.iloc[i, 1] == fire1_df.iloc[x, 1] else "불일치"
                if match_status == '일치':
                    match_cnt += 1
                match_list.append(match_status)
                # if match_status == "일치":
                #     method.append(max(score))
                # reconstructed_title = ' '.join(preprocessed_texts1[i])
                result = {
                    'compared_index': fire1_df.iloc[x,1],
                    'index': fire2_df.iloc[i,1],
                    'compared_text': fire1_df.iloc[x,0],
                    'title': fire2_df.iloc[i,0],
                    'similarity': round(score[x],3),
                    'match': match_status
                }
            
                results.append(result)
            match_ratio = round(match_cnt/(len(match_list)),4)    
            return render_template('results.html', results=results, match_ratio=match_ratio)


        

    return render_template('code.html')

if __name__ == '__main__':
    app.run(debug=True)