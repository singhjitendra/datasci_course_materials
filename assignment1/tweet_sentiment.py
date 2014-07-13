import json
import sys

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

# Files contains words and phrases, hence make two different dictonaries
def parse_sentiment_score(sentiment_score_lines):
    scores = {'word': {}, 'phrase': {}}
    for pair in sentiment_score_lines:
        term, score = pair.split('\t')
        if " " in term:
            scores['phrase'][term] = int(score)
        else:
            scores['word'][term] = int(score)
    
    return scores

# Get the score of a given tweet
def get_tweet_score(tweet, scores):
    score = 0
    cleaned_tweet = tweet.lower().strip(':?,#!.')
    # add word scores
    for word in cleaned_tweet.split(" "):
        if word in scores['word']:
            score += scores['word'][word]
            
    # check for phrases present, add the phrase score and remove the scores of individual word
    for phrase, pscore in scores['phrase'].iteritems():
        if phrase in cleaned_tweet:
            score += pscore
            for pword in phrase.split(" "):
                if pword in scores['word']:
                    score -= scores['word'][pword]
        
    return score

# Calculate the score of all the sentiments
def cal_sentiment_score(sentiments, scores):
    for line in sentiments:
        tweet = json.loads(line)
        if 'text' in tweet:
            print '%d' % get_tweet_score(tweet['text'], scores)
        else:
            print 0

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file

    sent_file_lines = sent_file.readlines()
    tweet_file_lines = tweet_file.readlines()
    
    try:
        scores = parse_sentiment_score(sent_file_lines)
        cal_sentiment_score(tweet_file_lines, scores)
    finally:
        sent_file.close()
        tweet_file.close()

if __name__ == '__main__':
    main()
