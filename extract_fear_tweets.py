import pandas
import os
import emojilib
import re

CURRENT_DIR_PATH = os.path.dirname(os.path.realpath(__file__))

DATA_PATH_JOY_TWEETS = CURRENT_DIR_PATH + '/data/EI-oc-En-train (1)/EI-oc-En-fear-train.txt'
DATA_PATH_JOY_TWEETS_DEV = CURRENT_DIR_PATH + '/data/2018-EI-oc-En-dev (1)/2018-EI-oc-En-fear-dev.txt'
DATA_PATH_JOY_TWEETS_REG = CURRENT_DIR_PATH + '/data/EI-reg-En-train (1)/EI-reg-En-fear-train.txt'
DATA_PATH_JOY_TWEETS_REG_DEV = CURRENT_DIR_PATH + '/data/2018-EI-reg-En-dev (1)/2018-EI-reg-En-fear-dev.txt'


def extract_and_save_joy_tweets():
    fear_tweets = pandas.read_csv(DATA_PATH_JOY_TWEETS, sep='\t', header=0)
    fear_tweets_dev = pandas.read_csv(DATA_PATH_JOY_TWEETS_DEV, sep='\t', header=0)
    fear_tweets_reg = pandas.read_csv(DATA_PATH_JOY_TWEETS_REG, sep='\t', header=0)
    fear_tweets_reg_dev = pandas.read_csv(DATA_PATH_JOY_TWEETS_REG_DEV, sep='\t', header=0)

    actual_fear_tweets = fear_tweets[fear_tweets['Intensity Class'] != '0: no fear can be inferred'].copy()
    actual_fear_tweets_dev = fear_tweets_dev[fear_tweets_dev['Intensity Class'] != '0: no fear can be inferred'].copy()
    actual_fear_tweets_reg = fear_tweets_reg[fear_tweets_reg['Intensity Score'] > 0.1].copy()
    actual_fear_tweets_dev_reg = fear_tweets_reg_dev[fear_tweets_reg_dev['Intensity Score'] > 0.1].copy()

    all_fear_tweets = pandas.DataFrame({'Tweet': actual_fear_tweets['Tweet'].copy()})
    all_fear_tweets.append(actual_fear_tweets_dev['Tweet'])
    all_fear_tweets.append(actual_fear_tweets_reg['Tweet'])
    all_fear_tweets.append(actual_fear_tweets_dev_reg['Tweet'])

    all_fear_tweets['Label'] = 'fear'

    all_fear_tweets.to_csv('./annotated data/tweets_fear.csv', encoding='utf-8', index=False, header=False)


extract_and_save_joy_tweets()
