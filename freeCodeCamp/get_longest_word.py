def get_longest_word(sentence):
    l = sentence.replace('.', '').split()
    maxi = ''
    for i in l:
        if len(i) > len(maxi):
            maxi = i
    return maxi