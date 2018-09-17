from nltk import sent_tokenize
import json
def tokenize(text):
    '''text: list of text documents'''
    tokenized =  sent_tokenize(text)
    return tokenized
	
with open("hotel_BJ_reviews.json",'r') as f_jsn:
        data = json.load(f_jsn)
		
def shuffle_tokenized(text):
    random.shuffle(text)
    newl=list(text)
    shuffled.append(newl)
    return text

augmented = []
reps=[]
for ng_rev in data['negative']:
    tok = tokenize(ng_rev)
    shuffled= [tok]
    #print(ng_rev)
    for i in range(11):
	#generate 11 new reviews
        shuffle_tokenized(shuffled[-1])
    for k in shuffled:
		'''create new review by joining the shuffled sentences'''
        s = ' '
        new_rev = s.join(k)
        if new_rev not in augmented:
            augmented.append(new_rev)
        else:
            reps.append(new_rev)
