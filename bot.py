 # Meet Pybot: your friend
import nltk
import warnings
warnings.filterwarnings("ignore")
# nltk.download() # for downloading packages
#import tensorflow as tf
import numpy as np
import random
import string # to process standard python strings

f=open('python.txt','r',errors = 'ignore')
m=open('modules pythons.txt','r',errors = 'ignore')
j=open('java.txt','r',errors = 'ignore')
r=open('rust.txt','r',errors = 'ignore')
c=open('C language.txt','r',errors = 'ignore')
p=open('php language.txt','r',errors = 'ignore')
checkpoint = "./chatbot_weights.ckpt"

raw=f.read()
rawone=m.read()
rawtwo=j.read()
rawthree=r.read()
rawfour=c.read()
rawfive=p.read()
raw=raw.lower()# converts to lowercase
rawone=rawone.lower()# converts to lowercase
rawtwo=rawtwo.lower()# converts to lowercase
rawthree=rawthree.lower()# converts to lowercase
rawfour=rawfour.lower()# converts to lowercase
rawfive=rawfive.lower()# converts to lowercase
nltk.download('punkt') # first-time use only
nltk.download('wordnet') # first-time use only
sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)# converts to list of words


sent_tokensone = nltk.sent_tokenize(rawone)# converts to list of sentences 
word_tokensone = nltk.word_tokenize(rawone)# converts to list of words

sent_tokenstwo = nltk.sent_tokenize(rawtwo)# converts to list of sentences 
word_tokenstwo = nltk.word_tokenize(rawtwo)# converts to list of words

sent_tokensthree = nltk.sent_tokenize(rawthree)# converts to list of sentences 
word_tokensthree = nltk.word_tokenize(rawthree)# converts to list of words

sent_tokensfour = nltk.sent_tokenize(rawfour)# converts to list of sentences 
word_tokensfour = nltk.word_tokenize(rawfour)# converts to list of words

sent_tokensfive = nltk.sent_tokenize(rawfive)# converts to list of sentences 
word_tokensfive = nltk.word_tokenize(rawfive)# converts to list of words


sent_tokens[:2]
sent_tokensone[:2]
sent_tokenstwo[:2]
sent_tokensthree[:2]
sent_tokensfour[:2]
sent_tokensfive[:2]

word_tokens[:5]
word_tokensone[:5]
word_tokenstwo[:5]
word_tokensthree[:5]
word_tokensfour[:5]
word_tokensfive[:5]

lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

Introduce_Q =("who are you", "Who are you?","I don't know you","Are you chatbot?","who are you?","WHO ARE YOU","are you chatbot","what is your name","your name")
Introduce_Ans = ["My name is PyBot.","My name is PyBot you can called me pi.","Im PyBot :) ","My name is PyBot. and my nickname is pi and i am happy to solve your queries :) "]
GREETING_INPUTS = ("hello", "hi","hiii","hii","hiiii","hiiii", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "hii there", "hi there", "hello", "I am glad! You are talking to me"]
Basic_Q = ("what is python ?","what is python","what is python?","what is python.")
Basic_Ans = "Python is a high-level, interpreted, interactive and object-oriented scripting programming language python is designed to be highly readable It uses English keywords frequently where as other languages use punctuation, and it has fewer syntactical constructions than other languages."
Basic_Om = ("what is module","what is module.","what is module ","what is module ?","what is module?","what is module in python","what is module in python.","what is module in python?","what is module in python ?")
Basic_AnsM = ["Consider a module to be the same as a code library.","A file containing a set of functions you want to include in your application.","A module can define functions, classes and variables. A module can also include runnable code. Grouping related code into a module makes the code easier to understand and use."]
Basic_On =("How are you?","Are you ok?","how are you","how are you?")
Basic_AnsN=["I am good , what about you", "I am nice , Don't you think so :) ","I am good enough"]

# Checking for greetings
def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# Checking for Basic_Q
def basic(sentence):
    for word in Basic_Q:
        if sentence.lower() == word:
            return Basic_Ans

# Checking for Basic_QM
def basicM(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in Basic_Om:
        if sentence.lower() == word:
            return random.choice(Basic_AnsM)


def basicN(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in Basic_On:
        if sentence.lower() == word:
            return random.choice(Basic_AnsN)
        
# Checking for Introduce
def IntroduceMe(sentence):
    for word in Introduce_Q:
        if sentence.lower() == word:
            return random.choice(Introduce_Ans)
    

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Generating response
def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response
      
# Generating response
def responseone(user_response):
    robo_response=''
    sent_tokensone.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokensone)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokensone[idx]
        return robo_response
def responsetwo(user_response):
    robo_response=''
    sent_tokenstwo.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokenstwo)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokenstwo[idx]
        return robo_response

def responsethree(user_response):
    robo_response=''
    sent_tokensthree.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokensthree)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokensthree[idx]
        return robo_response
def responsefour(user_response):
    robo_response=''
    sent_tokensfour.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokensfour)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokensfour[idx]
        return robo_response

def responsefive(user_response):
    robo_response=''
    sent_tokensfive.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokensfive)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokensfive[idx]
        return robo_response


def chat(user_response):
    user_response=user_response.lower()
    keyword = " module "
    keywordone = " module"
    keywordsecond = "module "
    
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            #print("ROBO: You are welcome..")
            return "You are welcome.."
        elif(basicM(user_response)!=None):
            return basicM(user_response)
        else:
            if(user_response.find(keyword) != -1 or user_response.find(keywordone) != -1 or user_response.find(keywordsecond) != -1):
                #print("ROBO: ",end="")
                #print(responseone(user_response))
                return responseone(user_response)
                sent_tokensone.remove(user_response)

            elif(user_response.find("in Java") != -1 or user_response.find("in Java?") != -1 or user_response.find(" in Java ") != -1 or user_response.find(" in Java") != -1 or user_response.find("in Java ") != -1 or user_response.find("in Java?") != -1):
                return responsetwo(user_response)
                sent_tokenstwo.remove(user_response)
                
            #in C language
            elif(user_response.find("c language") != -1 or user_response.find("c language?") != -1 or user_response.find("in c language") != -1 or user_response.find(" in c language") != -1 or user_response.find("in c language ") != -1 or user_response.find("in c language?") != -1):
                return responsefour(user_response)
                sent_tokensfour.remove(user_response)

            #PHP 
            elif(user_response.find("is php") != -1 or user_response.find("in php") != -1 or user_response.find(" in php ") != -1 or user_response.find(" in php") != -1 or user_response.find("php") != -1 or user_response.find("php?") != -1):
                return responsefive(user_response)
                sent_tokensfive.remove(user_response)

            elif(user_response.find("is rust") != -1 or user_response.find("in Rust?") != -1 or user_response.find("in Rust") != -1 or user_response.find(" in Rust") != -1 or user_response.find("in Rust ") != -1 or user_response.find("in Rust?") != -1):
                return responsethree(user_response)
                sent_tokensthree.remove(user_response)

            elif(IntroduceMe(user_response)!=None):
                return IntroduceMe(user_response)
            elif(greeting(user_response)!=None):
                #print("ROBO: "+greeting(user_response))
                return greeting(user_response)
            elif(user_response.find("your name") != -1 or user_response.find(" your name") != -1 or user_response.find("your name ") != -1 or user_response.find(" your name ") != -1):
                return IntroduceMe(user_response)
            elif(basic(user_response)!=None):
                return basic(user_response)
            elif(basicN(user_response)!=None):
                return basicN(user_response)
            else:
                #print("ROBO: ",end="")
                #print(response(user_response))
                return response(user_response)
                sent_tokens.remove(user_response)
                
    else:
        flag=False
        #print("ROBO: Bye! take care..")
        return "Bye! take care.."
        
        

