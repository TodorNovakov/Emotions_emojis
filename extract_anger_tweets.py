import pandas
import os
import emojilib
import re

CURRENT_DIR_PATH = os.path.dirname(os.path.realpath(__file__))

DATA_PATH_TWEETS = CURRENT_DIR_PATH + '/data/EI-oc-En-train (1)/EI-oc-En-anger-train.txt'
DATA_PATH_TWEETS_DEV = CURRENT_DIR_PATH + '/data/2018-EI-oc-En-dev (1)/2018-EI-oc-En-anger-dev.txt'
DATA_PATH_TWEETS_REG = CURRENT_DIR_PATH + '/data/EI-reg-En-train (1)/EI-reg-En-anger-train.txt'
DATA_PATH_TWEETS_REG_DEV = CURRENT_DIR_PATH + '/data/2018-EI-reg-En-dev (1)/2018-EI-reg-En-anger-dev.txt'


def extract_and_save_joy_tweets():
    anger_tweets = pandas.read_csv(DATA_PATH_TWEETS, sep='\t', header=0)
    anger_tweets_dev = pandas.read_csv(DATA_PATH_TWEETS_DEV, sep='\t', header=0)
    anger_tweets_reg = pandas.read_csv(DATA_PATH_TWEETS_REG, sep='\t', header=0)
    anger_tweets_reg_dev = pandas.read_csv(DATA_PATH_TWEETS_REG_DEV, sep='\t', header=0)

    actual_anger_tweets = anger_tweets[anger_tweets['Intensity Class'] != '0: no anger can be inferred'].copy()
    actual_anger_tweets_dev = anger_tweets_dev[anger_tweets_dev['Intensity Class'] != '0: no anger can be inferred'].copy()
    actual_anger_tweets_reg = anger_tweets_reg[anger_tweets_reg['Intensity Score'] > 0.1].copy()
    actual_anger_tweets_dev_reg = anger_tweets_reg_dev[anger_tweets_reg_dev['Intensity Score'] > 0.1].copy()

    all_anger_tweets = pandas.DataFrame({'Tweet': actual_anger_tweets['Tweet'].copy()})
    all_anger_tweets.append(actual_anger_tweets_dev['Tweet'])
    all_anger_tweets.append(actual_anger_tweets_reg['Tweet'])
    all_anger_tweets.append(actual_anger_tweets_dev_reg['Tweet'])

    all_anger_tweets['Label'] = 'anger'

    all_anger_tweets.to_csv('./annotated data/tweets_anger.csv', encoding='utf-8', index=False, header=False)


extract_and_save_joy_tweets()
