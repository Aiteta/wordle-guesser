scores_file_name = "words_5_score.txt"
word_len = 5

scores_file = open(scores_file_name)
scores      = {line.split(',')[0]:line.split(',')[-1] for line in scores_file.read().split('\n')}
scores.pop("")
scores      = {word:float(scores[word]) for word in scores}

most = 0
best = {}
for word_a in scores:
    #if scores[word_a] < 1:
     #   continue
    for word_b in scores:
        if not (len(set(word_a) & set(word_b))):
       #  if scores[word_b] < 1:
       #     continue
        #if not (len(set(word_a) & set(word_b))):
                # print(word_a,word_b,scores[word_a] + scores[word_b])
            if most < scores[word_a] + scores[word_b]:
                most = scores[word_a] + scores[word_b]
                best = {word_a, word_b}

print(most, best)
