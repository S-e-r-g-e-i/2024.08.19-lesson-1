# Произвольное число параметров


def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(0, len(other_words), 1):
        if other_words[i].upper() == root_word.upper():
            same_words.append(other_words[i])
        if len(other_words[i]) > len(root_word):
            for j in range(0, len(other_words[i]) - len(root_word), 1):
                check_root_word = other_words[i][j:len(root_word) + j]
                if root_word.upper() == check_root_word.upper():
                    same_words.append(other_words[i])
                else:
                    continue
        if len(other_words[i]) < len(root_word):
            for k in range(0, len(root_word) - len(other_words[i]), 1):
                check_other_words = root_word[k:len(other_words[i]) + k]
                if other_words[i].upper() == check_other_words.upper():
                    same_words.append(other_words[i])
                else:
                    continue
    print(same_words)


single_root_words('topas', 'lopa', 'topa', 'ToPa', 'Pa', 'TOp', 'ToPAs', 'tOpaSISD', 'dhdhdhTopasLL')

#Test of task
single_root_words('rich',  'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')