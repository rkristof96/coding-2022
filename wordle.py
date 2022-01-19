USER_PROMPT = 'Guess the word: '


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
    if len(guess)!=len(true_word):
        return 'TWO WORDS ARE NOT SAME LENGTH.'

    score=''
    N=len(true_word)

    for position in range(N):
        # print(position, true_word[position], guess[position],score_letter(guess[position], position,true_word))
        score = score + score_letter(guess[position], position,true_word)
    return score


# message=score_word('APPLE', 'ABBA')
# print(message)
message=score_word('APPB', 'ABBA')
print(message)
# FIXME: add functions to get user inputs & read random word

def get_and_score_guess(true_word):
    guess=input(USER_PROMPT)
    score=(score_word(guess, true_word))
    print(len(USER_PROMPT)*''+score)
    return score

def loop_until_success(true_word):
    correct_guess = False
    while not correct_guess:
        score=get_and_score_guess(true_word)
        if score == 6*'*':
            correct_guess = True

loop_until_success('across')
