from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords


text = "China enforced a lockdown on over 18 million residents living in the Southern part of Shenzhen till at least March 20 on Sunday." \
       "China pursued a zero-covid policy due to which multiple cities were locked down. The omicron variant, however, made it very difficult for the country to continue with this approach. " \
       "On Sunday, China reported twice the number of new cases from the day before, the total reaching 3,400. This makes it the worst outbreak in two years." \
       "Currently, the subways and trains in Shenzhen have stopped operating and the citizens have been instructed to limit their travel. "

print(text)
print("\n\n")
print(summarize(text, ratio=0.5))


# Create corpus from given documents
# ---Load, Preprocess, Dictionary and then BagofWords (gensim-downloader, simple-preprocess, doc2bow)

# Create TFIDF matrix
# ---models.TfIdf

# Create Bigrams and Trigrams (Groups of 2 & 3 words)
# --- Phraser model

# Create Word2Vec model
# -- word2vec (we would be using this one), GloVe, fasttext
# -- training of model here, divide your dataset into 2 datasets based on 80/20 ratio and train it
#    using the 80% of the dataset
# -- then update your dataset using the second dataset

# Create Doc2Vec model
# -- doc2vec, Similarly train and update the model

# Topic Modelling using LDA
# --- Prepare data--- NLTK (stopwords), Gensim(simple-preprocess, lemmatize)
# --- Create Dictionary and corpus (gensim.corpora)
# --- Train LDA model (LdaModel, LdaMulticore)


# Similarity Matrix
# -- softcosim, cosine similarity

# Create Summary
# -- gensim.summarization.summarize


