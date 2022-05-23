import re
import nltk
import math, random
import heapq


text = "China enforced a lockdown on over 18 million residents living in the Southern part of Shenzhen till at least March 20 on Sunday. China pursued a zero-covid policy due to which multiple cities were locked down. The omicron variant, however, made it very difficult for the country to continue with this approach. On Sunday, China reported twice the number of new cases from the day before, the total reaching 3,400. This makes it the worst outbreak in two years." \
       "Currently, the subways and trains in Shenzhen have stopped operating and the citizens have been instructed to limit their travel. "

text = text.lower()

cleantext = re.sub("[^a-zA-Z]", ' ', text)
cleantext = re.sub("\s+", ' ', cleantext)

stopwords = nltk.corpus.stopwords.words('english')

sentence_list = nltk.sent_tokenize(text)

word_frequencies = {}
for word in nltk.word_tokenize(cleantext):
    if word not in stopwords:
        if word not in word_frequencies:
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1

#tot_words = len(cleantext)
print(word_frequencies)

sentence_score = {}
for sentence in sentence_list:
    freq = 0
    for word in nltk.word_tokenize(sentence):
        if word in word_frequencies:
            word_score = math.log(word_frequencies[word])
            freq = freq + word_score

    sentence_score[sentence] = freq

print(sentence_score)

score_lst = []
for x in sentence_score.values():
    score_lst.append(x)

print(score_lst)

for x in range(50):
    random_idx = random.randrange(len(score_lst))
    rand_number1 = score_lst[random_idx]
    print(rand_number1)
    score_lst.pop(random_idx)
    random_idx2 = random.randrange(len(score_lst))
    rand_number2 = score_lst[random_idx2]
    print(rand_number2)
    score_lst.pop(random_idx2)
    # crossover
    new_num = rand_number1 + rand_number2
    new_num2 = rand_number1 - rand_number2

    # mutation
    op = random.choice([0, 1])
    num_op = random.choice([0.1, 0.2, 0.4])
    if op == 0:
        new_num = new_num + num_op
    elif op == 1:
        new_num = new_num - num_op

    score_lst.append(new_num)
    score_lst.append(new_num2)
    print(score_lst)
    print("\n\n")


sorted_score = sorted(score_lst, reverse=True)
print(sorted_score)


