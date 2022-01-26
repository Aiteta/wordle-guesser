scores_file_name = "words_5_score.txt"
word_len = 5

scores_file = open(scores_file_name)
scores      = {line.split(',')[0]:line.split(',')[-1] for line in scores_file.read().split('\n')}
scores.pop("")
scores      = {word:float(scores[word]) for word in scores}

"""
most = 0
best = {}
for word_a in scores:
    for word_b in scores:
        if not (len(set(word_a) & set(word_b))):
            if most < scores[word_a] + scores[word_b]:
                most = scores[word_a] + scores[word_b]
                best = {word_a, word_b}

print(most, best)"""

data = dict()

for word in scores:
    for i in range(len(word)):
        if not i in data:
            data[i] = dict()
        if not word[i] in data[i]:
            data[i][word[i]] = 0
        data[i][word[i]] += 1

print(data)
