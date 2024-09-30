import json
import nltk
import re
import language_tool_python
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from textblob import TextBlob
from spellchecker import SpellChecker
import joblib 

# Download required NLTK resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

class HeuristicBot:
    def __init__(self, filename=None):
        self.tool = language_tool_python.LanguageTool('en-US')
        self.spell = SpellChecker()
        self.lemmatizer = WordNetLemmatizer()
        
        # Only load data if a filename is provided
        if filename:
            self.questions = self.load_data(filename)
            self.tfidf_vectorizer = TfidfVectorizer()
            self.tfidf_matrix = self.tfidf_vectorizer.fit_transform([self.preprocess_text(q['question']) for q in self.questions])
            self.keyword_weights = self.detect_important_words(top_n=10)
        else:
            self.questions = []  # Initialize questions as an empty list
            self.tfidf_vectorizer = TfidfVectorizer()  # Initialize an empty vectorizer

    def load_data(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            questions = json.load(file)
        return questions

    def correct_spelling(self, text):
        words = text.split()
        corrected_words = [self.spell.candidates(word).pop() if word in self.spell else word for word in words]
        return ' '.join(corrected_words)

    def preprocess_text(self, text):
        text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
        text = text.lower()  # Convert to lowercase
        text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
        
        # Correct spelling
        text = self.correct_spelling(text)
        
        # Correct spelling using TextBlob
        text = str(TextBlob(text).correct())

        # Check grammar using LanguageTool
        matches = self.tool.check(text)
        corrected_text = language_tool_python.utils.correct(text, matches)
        
        # Lemmatize words
        words = word_tokenize(corrected_text)
        text = ' '.join(self.lemmatizer.lemmatize(word) for word in words)

        return text

    def apply_weights(self, tfidf_matrix, keyword_weights):
        weighted_matrix = tfidf_matrix.toarray().copy()
        feature_names = self.tfidf_vectorizer.get_feature_names_out()

        for word, weight in keyword_weights.items():
            if word in feature_names:
                index = np.where(feature_names == word)[0][0]
                weighted_matrix[:, index] *= weight
                
        return weighted_matrix

    def heuristic_approach(self, user_input: str) -> str:
        tokens = word_tokenize(user_input, language='english', preserve_line=True)
        tokens = [self.lemmatizer.lemmatize(word.lower()) for word in tokens]

        for question in self.questions:
            keywords = [self.lemmatizer.lemmatize(word.lower()) for word in word_tokenize(question['question'], language='english', preserve_line=True)]
            match_count = sum(1 for token in tokens if token in keywords)

            if match_count >= len(keywords) * 0.8:
                return question['answer']

        return None

    def semantic_similarity_approach(self, user_input: str):
        user_input_vector = self.tfidf_vectorizer.transform([self.preprocess_text(user_input)])
        
        # Apply weights to the TF-IDF matrix
        weighted_tfidf_matrix = self.apply_weights(self.tfidf_matrix, self.keyword_weights)
        
        # Calculate cosine similarity using the weighted TF-IDF matrix
        similarities = cosine_similarity(user_input_vector, weighted_tfidf_matrix).flatten()
        
        # Find the index of the most similar question
        answer_index = np.argmax(similarities)
        return self.questions[answer_index]['answer']

    def detect_important_words(self, top_n=10):
        texts = [q['question'] for q in self.questions]
        tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf_vectorizer.fit_transform(texts)
        feature_names = tfidf_vectorizer.get_feature_names_out()
        scores = np.asarray(tfidf_matrix.sum(axis=0)).flatten()
        word_scores = dict(zip(feature_names, scores))
        important_words = sorted(word_scores.items(), key=lambda item: item[1], reverse=True)[:top_n]
        return {word: 2.0 for word, score in important_words}  # Assigning a weight of 2.0 to important words

    def chatbot(self, user_input):
        # Check with the heuristic approach first
        answer = self.heuristic_approach(user_input)
        
        # If no answer found, check with semantic similarity
        if answer is None:
            answer = self.semantic_similarity_approach(user_input)

        return answer
    
    def save_model(self, tfidf_filename='../data/tfidf_vectorizer.pkl', questions_filename='../data/questions.json'):
        joblib.dump(self.tfidf_vectorizer, tfidf_filename)  # Save the TF-IDF vectorizer
        with open(questions_filename, 'w', encoding='utf-8') as f:
            json.dump(self.questions, f)  # Save the questions data
            

    def load_model(self, tfidf_filename='../data/tfidf_vectorizer.pkl', questions_filename='../data/questions.json'):
        self.tfidf_vectorizer = joblib.load(tfidf_filename)  # Load the TF-IDF vectorizer
        with open(questions_filename, 'r', encoding='utf-8') as f:
            self.questions = json.load(f)  # Load the questions data
        self.tfidf_matrix = self.tfidf_vectorizer.transform([self.preprocess_text(q['question']) for q in self.questions])
        self.keyword_weights = self.detect_important_words(top_n=10)


def train_and_save_model():
    filename = "../data/nesr_questions.json"
    bot = HeuristicBot(filename=filename)
    bot.save_model()

if __name__ == "__main__":
    train_and_save_model()
