from nltk.tokenize import regexp_tokenize
from nltk import bigrams
from collections import Counter
from string import ascii_uppercase
import random
file = open(input(), "r", encoding="utf-8")
bigram_list = list(bigrams(regexp_tokenize(file.read(), r'\S+')))
file_list = [str(bigram[0]) for bigram in bigram_list]
trigram_list = []
for i in range(len(file_list) - 2):
    trigram_list.append([file_list[i] + " " + file_list[i + 1], file_list[i + 2]])
head_list = [head[0] for head in trigram_list]


def word_generator(tail_count_list):
    if len(tail_count_list) >= 5:
        return random.choices([tail[0] for tail in tail_count_list.most_common(5)], weights=tuple([tail[1] for tail in tail_count_list.most_common(5)]))[0]
    else:
        return random.choices([tail[0] for tail in tail_count_list.most_common(len(tail_count_list))], weights=tuple([tail[1] for tail in tail_count_list.most_common(len(tail_count_list))]))[0]


for _ in range(10):
    random_sentence = random.choices(head_list)[0].split()
    while True:
        if (random_sentence[0][-1] != '.' and random_sentence[0][-1] != '!' and random_sentence[0][-1] != '?' and random_sentence[-1][-1] != '.' and random_sentence[-1][-1] != '!' and random_sentence[-1][-1] != '?') and random_sentence[0][0] in ascii_uppercase:
            break
        else:
            random_sentence = random.choices(head_list)[0].split()
            continue

    while random_sentence[-1][-1] != '.' or random_sentence[-1][-1] != '!' or random_sentence[-1][-1] != '?' or random_sentence[0][-1] != '.' or random_sentence[0][-1] != '!' or random_sentence[0][-1] != '?':
        tail_counter = Counter([trigram[1] for trigram in trigram_list if trigram[0] == random_sentence[-2] + ' ' + random_sentence[-1]])
        word = word_generator(tail_counter)
        if len(random_sentence) < 4:
            word = word_generator(tail_counter)
            random_sentence.append(word)
        else:
            word = random.choices([tail[0] for tail in tail_counter.most_common(5)], weights=tuple([tail[1] for tail in tail_counter.most_common(5)]))[0]
            if word[-1][-1] == '.' or word[-1][-1] == '!' or word[-1][-1] == '?':
                random_sentence.append(word)
                break
            else:
                random_sentence.append(word)
    generated_sentence = ' '.join(random_sentence)
    print(generated_sentence)
