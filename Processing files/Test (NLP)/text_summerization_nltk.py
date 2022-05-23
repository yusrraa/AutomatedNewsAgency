import nltk, re
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx



text = "China enforced a lockdown on over 18 million residents living in the Southern part of Shenzhen till at least March 20 on Sunday. China pursued a zero-covid policy due to which multiple cities were locked down. The omicron variant, however, made it very difficult for the country to continue with this approach. On Sunday, China reported twice the number of new cases from the day before, the total reaching 3,400. This makes it the worst outbreak in two years." \
       "Currently, the subways and trains in Shenzhen have stopped operating and the citizens have been instructed to limit their travel. "
sentence = nltk.sent_tokenize(text)


for i in range(len(sentence)):
    sen = re.sub('[^a-zA-Z]', " ", sentence[i])
    sen = sen.lower()
    sen = sen.split()
    sen = ' '.join([i for i in sen])


def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords=[]
    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]
    all_words =list(set(sent1+sent2))
    vector1 = [0] * len(all_words)

    vector2 = [0] * len(all_words)
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1
    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1
    return 1-cosine_distance(vector1,vector2)

def gen_sim_matrix(sentences, stop_words):
    similarity_matrix = np.zeros((len(sentences),len(sentences)))
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2:
                continue
            similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

    return similarity_matrix

def generate_summary(top_n=5):
    stop_words=stopwords.words('english')
    summarize_text=[]
    # sentences = read_article(file_name)
    #sentences = "Imran Khan is the first prime minister in the country's history to be vetoed out from his office as a result of a no-confidence motion.174 members have recorded their votes in favour of the resolution."
    sentence_similarity_matrix = gen_sim_matrix(sen, stop_words)
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_matrix)
    scores = nx.pagerank(sentence_similarity_graph, max_iter=6000)
    np.seterr(invalid='ignore')
    ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sen)), reverse=True)
    for j in range(top_n):
        summarize_text.append(" ".join(ranked_sentences[j][1]))
    print("Summary \n", ". ".join(summarize_text))


generate_summary(2)
