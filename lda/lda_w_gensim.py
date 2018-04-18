# data: https://www.kaggle.com/mousehead/songlyrics

# file reading
import pandas as pd
# NLTK preprocessing
import nltk
from nltk import word_tokenize
#from nltk.corpus import stopwords
#from nltk.stem.snowball import SnowballStemmer

# LDA
import gensim

df=pd.read_csv("songdata.csv",sep=",")


raw_text = list(df['text'])

stopword_list = nltk.corpus.stopwords.words("english")
stemmer = nltk.stem.snowball.SnowballStemmer("english")
tokenizer = nltk.tokenize.regexp.RegexpTokenizer("[^\W\d]+")

dir(stemmer)

# word_tokenize

texts = []
for txt in raw_text[0:100]:
    # tokenize
    word_list = tokenizer.tokenize(txt.lower())
    # stem + stop word removal
    word_list = [stemmer.stem(i) for i in word_list if i not in stopword_list]
    
    texts.append(word_list)

# Conver to vector space
# https://radimrehurek.com/gensim/tut1.html
dictionary = gensim.corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

# Do LDA
#https://rare-technologies.com/multicore-lda-in-python-from-over-night-to-over-lunch/
lda = gensim.models.ldamodel.LdaModel(corpus, num_topics=10)

