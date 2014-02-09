import re
from Tools.Scripts.ftpmirror import raw_input

__author__ = 'KOL'


def clean_tweet(tweet, meta=False):
    if not meta:
        matcher = re.compile(r"#[a-zA-Z0-9-_]+")
        tweet = matcher.sub("", tweet)
        matcher = re.compile(r"@")
        return matcher.sub("", tweet)
    else:
        keys = ("#", "@")
        dictionary = {}
        matcher = re.compile(r"#[a-zA-Z0-9-_]+")
        hash_tags = matcher.findall(tweet)
        matcher = re.compile(r"@[a-zA-Z0-9-_]+")
        re_tweets = matcher.findall(tweet)
        dictionary[keys[0]] = hash_tags
        dictionary[keys[1]] = re_tweets
        return dictionary, clean_tweet(tweet)

while True:
    testText = raw_input("Please, input string: ")
    print("Meta flag = False")
    print(clean_tweet(testText))
    print("Meta flag = True")
    dict, tweet = clean_tweet(testText, True)
    print(dict)
    print(tweet)