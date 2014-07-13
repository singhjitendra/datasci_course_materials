# Contact me @ lidai.tiger at gmail dot com
# Coursera-Data science Assignment 1

# Usage:

# $ python term_sentiment.py <sentiment_file> <tweet_file>

import sys
import json
import re

def main():
    ###### 1 ########
    # load dictionary of sentiments with scores
    #sent_dict = open("AFINN-111.txt")
    sent_dict = open(sys.argv[1])
    scores = {}
    for line in sent_dict:
        term, score = line.split('\t')
        scores[term] = float(score)

    ###### 2 ######    
    # load tweet file  
    #tweet_file = open("output.txt")
    tweet_file= open(sys.argv[2])

    # load each tweet using json
    # score each tweet
    score_output = []
    new_dict = {}
    for line in tweet_file:
        score=0
        tweet_data = json.loads(line)
        if tweet_data.get('text'):
            tweet_text = tweet_data['text'].encode('utf8').split(' ')
            for word in tweet_text:
                 if re.match("^[A-Za-z0-9_-]*$", word.lower()):
                     if word in scores:
                         score += scores.get(word.lower(),0)
            for word in tweet_text:
                if re.match("^[A-Za-z0-9_-]*$", word.lower()):
                     if word not in scores:
                         #if the word is not in the old dictionary, assign the word a new scor
                         new_dict[word.lower()] = float(new_dict.get(word.lower(),0)+ score)
                    
    ###### 3 #######
    # assign score to each word in the tweet
    for word in new_dict:
        print word, float(new_dict.get(word.lower(),0))
    '''
    for i in score_output:
	    print "%.2f" % i
'''
    
if __name__ == '__main__':
  main()