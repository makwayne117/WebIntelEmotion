from senticnet.senticnet import SenticNet

from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from textblob import TextBlob

import nltk
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

from nltk.corpus import wordnet


#likely will need a better library. 
def get_synonyms(word:str):
    synonyms = []
    
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name()) 
    
    return synonyms  

#adapted from: https://stackoverflow.com/questions/56980515/how-to-extract-all-adjectives-from-a-strings-of-text-in-a-pandas-dataframe
def extract_descriptive_words(sentence:str):
    blob = TextBlob(sentence)
    return [ word for (word,tag) in blob.tags if tag == "JJ"]


def constructFeature(sentence:str):
    vectors = {}
    adjectives = extract_descriptive_words(sentence)

    for s in adjectives:
        synonyms = get_synonyms(s)
        concept_info = sn.concept(s)
        polarity_label = sn.polarity_label(s)
        polarity_value = sn.polarity_value(s)
        moodtags = sn.moodtags(s)
        semantics = sn.semantics(s)
        sentics = sn.sentics(s)

        senticVector = {"synonyms": synonyms, "moodtags":moodtags, "polarity_label":polarity_label, "polarity_value":polarity_value, "semantics":semantics, "sentics":sentics}
        vectors[s] = senticVector
    return vectors

def generateReviewModel(title:str, sentence:str):
    vectors = {}

    senticVectors = constructFeature(sentence)

    return {"aspect":title, "category":"film quality", "review sentence": sentence, "sentic info":senticVectors}





