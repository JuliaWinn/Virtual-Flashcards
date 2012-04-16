import random
from pprint import pprint as pretty
import sys
import nltk
import re

def main(file_name, term_div, term_def_div):
	
	final_dict = {}
	_input = open(file_name, "r")
	
	"""check if terms are divided by a symbol or just a new line"""
	
	if term_div != None:
	    terms = _input.split(term_div)
	
	else:
	    terms = _input.readlines()

	for i, term in enumerate(terms):
		try:
			splitted = term.split(term_definition_divider)
			final_dict[splitted[0]] = splitted[1]
			
		except IndexError:
			pass
	
	init = False
	
	while init == False:
	    mode = raw_input("Do you want to first be shown a term or definition?\n").strip()
	    if "term" in mode:
	        display1 = 0
	        display2 = 1
	        init = True
	        
	    elif "definition" in mode:
	        display1 = 1
	        display2 = 0
	        init = True
	        
	    else:
	        print "Sorry, please try again.\n"
	
	copy_dict = final_dict
	
	while len(copy_dict) > 0:
		term = random.choice(copy_dict.keys())
		definition = copy_dict[term]
		display = [term, definition]
		
		guess = raw_input(display[display1] + '\n')
		if guess == "remove":
			del copy_dict[term]
		else:
		    answer_text = "Answer:\n" + str(display[display2]) + '\n'
            # when correct remove the card from the deck
		    answer = raw_input(answer_text + "Were you correct?\n")
		    print "Our guess was", guess_if_correct(guess, display[display2])
		    a = re.match('(Y|y)es*', answer)
		    if answer == "yes":
		        del copy_dict[term]
		    else:
		        continue

"""a rough metric for guessing if the answer is correct or not"""
def guess_if_correct(guess, answer):
    ans = nltk.word_tokenize(answer)
    guess = nltk.word_tokenize(guess)
    
    common_words = nltk.corpus.stopwords.words('english')
    
    ans_words = [x for x in ans if x not in common_words]
    guess_words = [x for x in guess if x not in common_words]
    
    ans_size = len(ans_words)
    
    total_guessed = 0
    
    for w in guess_words:
        if answer.lower().find(w.lower()) >= 0:
            total_guessed += 1
    
    if (((total_guessed*1.0)/ans_size) > 0.5):
        return "yes"
    elif (0.39 < ((total_guessed*1.0)/ans_size) <= 0.5):
        return "maybe"
    else:
        return "no"		

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: python flashcard.py document.txt ['term divider'] 'term definition divider'"
    else:
        file_name = sys.argv[1]
        if len(sys.argv) == 4:
            term_divider = sys.argv[2]
            term_definition_divider = sys.argv[3]
            main(file_name, term_divider, term_definition_divider)
    
        elif len(sys.argv) == 3:
            term_divider = None
            term_definition_divider = sys.argv[2]
            main(file_name, term_divider, term_definition_divider)
        else:
            print "Usage: python flashcard.py document.txt ['term divider'] 'term definition divider'"