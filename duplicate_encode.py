def duplicate_encode(word):
    
    solution = ''
    word = word.upper()
    
    for letter in word:
        if word.count(letter) == 1:
            solution += '('
        else:
            solution += ')'
            
    return solution
