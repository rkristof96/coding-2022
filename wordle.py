def score_letter(letter, position, true_word):

    # for example score_letter ('A',1, 'ABBA') should be a correct position

    if(true_word[position] == letter):
        return '*' # for correct position


    if(letter in true_word):
           return 'o' # for correct letter in incorrectr position
    else:
           return '-'    

def score_word(guess, true_word):
    # score_word('APPL','ABBA')
    # results '*---'
    # algorithm works for words with the same length
    N=len(true_word)
    for position in range(N):
        print(position, guess[position],score_letter(guess[position], position,true_word))

score_word('AAPL', 'ABBA')

# FIXME: add functions to get user inputs & read random word