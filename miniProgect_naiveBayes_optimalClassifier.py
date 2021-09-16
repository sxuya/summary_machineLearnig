#------------------------------------------------------------------

#
#   Bayes Optimal Classifier
#
#   In this quiz we will compute the optimal label for a second missing word in a row
#   based on the possible words that could be in the first blank
#
#   Finish the procedurce, LaterWords(), below
#
#   You may want to import your code from the previous programming exercise!
#

sample_memo = '''
Milt, we're gonna need to go ahead and move you downstairs into storage B. We have some new people coming in, and we need all the space we can get. So if you could just go ahead and pack up your stuff and move it down there, that would be terrific, OK?
Oh, and remember: next Friday... is Hawaiian shirt day. So, you know, if you want to, go ahead and wear a Hawaiian shirt and jeans.
Oh, oh, and I almost forgot. Ahh, I'm also gonna need you to go ahead and come in on Sunday, too...
Hello Peter, whats happening? Ummm, I'm gonna need you to go ahead and come in tomorrow. So if you could be here around 9 that would be great, mmmk... oh oh! and I almost forgot ahh, I'm also gonna need you to go ahead and come in on Sunday too, kay. We ahh lost some people this week and ah, we sorta need to play catch up.
'''

corrupted_memo = '''
Yeah, I'm gonna --- you to go ahead --- --- complain about this. Oh, and if you could --- --- and sit at the kids' table, that'd be --- 
'''

data_list = sample_memo.strip().split()

words_to_guess = ["ahead","could"]

def NextWordProbability(sampletext,word):
    text_lists = sampletext.split(" ")
    words_dict = {}

    for i, item in enumerate(text_lists):
    	if item == word:
    		if i < len(text_lists) -1:
    			if text_lists[i+1] not in words_dict:	
    			# "text_lists[i+1]"" is coded as "item" , so that the count number is wrong
    				words_dict[text_lists[i+1]] = 1
    			else:
    				words_dict[text_lists[i+1]] += 1
    # print words_dict

    all_number = 0
    for item in words_dict:
    	all_number += words_dict[item]

    for item in words_dict:
    	words_dict[item] = words_dict[item] * 1.0 / all_number

    return words_dict

# print NextWordProbability(sample_memo, "you")

def LaterWords(sample,word,distance):
    '''@param sample: a sample of text to draw from
    @param word: a word occuring before a corrupted sequence
    @param distance: how many words later to estimate (i.e. 1 for the next word, 2 for the word after that)
    @returns: a single word which is the most likely possibility
    '''
    
    # TODO: Given a word, collect the relative probabilities of possible following words
    # from @sample. You may want to import your code from the maximum likelihood exercise.
    first_word_dict = NextWordProbability(sample, word)
    print first_word_dict
    # TODO: Repeat the above process--for each distance beyond 1, evaluate the words that
    # might come after each word, and combine them weighting by relative probability
    # into an estimate of what might appear next.
    second_word_dict_temp = {}
    second_word_dict = {}
    for item in first_word_dict:
    	second_word_dict_temp = NextWordProbability(sample, item)
    	# print second_word_dict_temp
    	for item_second in second_word_dict_temp:
    		if item_second not in second_word_dict:
    			second_word_dict[item_second] = first_word_dict[item] * second_word_dict_temp[item_second]
    		else:
    			second_word_dict[item_second] += first_word_dict[item] * second_word_dict_temp[item_second]

    second_most_word = max(second_word_dict, key=second_word_dict.get)
    return second_most_word
    # return second_word_dict
    
print LaterWords(sample_memo,"gonna",2)
print LaterWords(sample_memo,"ahead",2)
print LaterWords(sample_memo,"could",2)
print LaterWords(sample_memo,"be",2)