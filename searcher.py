def calc_score(guess, word):
    score = 0
    for letter in set(guess):
        score += 0.5*word.count(letter)
    for i in range(len(guess)):
        if guess[i] == word[i]:
            score += 0.5
    return score

def calc_all_scores(guess, word_list):
    score = 0
    for word in word_list:
        score += calc_score(guess,word)
    score /= len(word_list)
    return score


file_name = "words.txt"
len_word  = 5
is_alpha  = True

words_file = open(file_name)
all_words  = words_file.read().split()
words_file.close()
words_filt = [word.lower() for word in all_words if len(word) == len_word]
if is_alpha:
    words_filt = [word for word in words_filt if word.isalpha()]

words_filt_file_name = f"{''.join(file_name.split('.')[:-1])}_{len_word}.txt"
words_filt_file = open(words_filt_file_name,"w")

scores_file_name = f"{''.join(file_name.split('.')[:-1])}_{len_word}_score.txt"
scores_file = open(scores_file_name,"w")

i = 0
for word in words_filt:
    print(i)
    i += 1
    words_filt_file.write(f"{word}\n")
    scores_file.write(f"{word},{calc_all_scores(word,words_filt)}\n")

words_filt_file.close()
scores_file.close()
