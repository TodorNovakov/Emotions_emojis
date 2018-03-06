import pandas
import os
import emojilib
import re

CURRENT_DIR_PATH = os.path.dirname(os.path.realpath(__file__))

DATA_PATH_JOY_TWEETS = CURRENT_DIR_PATH + '/data/EI-oc-En-train (1)/EI-oc-En-joy-train.txt'
DATA_PATH_JOY_TWEETS_DEV = CURRENT_DIR_PATH + '/data/2018-EI-oc-En-dev (1)/2018-EI-oc-En-joy-dev.txt'
DATA_PATH_JOY_TWEETS_REG = CURRENT_DIR_PATH + '/data/EI-reg-En-train (1)/EI-reg-En-joy-train.txt'
DATA_PATH_JOY_TWEETS_REG_DEV = CURRENT_DIR_PATH + '/data/2018-EI-reg-En-dev (1)/2018-EI-reg-En-joy-dev.txt'
DATA_PATH_JOY_CROWDFOWLER = CURRENT_DIR_PATH + '/data/dfe_happysad_utf.csv'


def extract_and_save_joy_tweets():
    joy_tweets = pandas.read_csv(DATA_PATH_JOY_TWEETS, sep='\t', header=0)
    joy_tweets_dev = pandas.read_csv(DATA_PATH_JOY_TWEETS_DEV, sep='\t', header=0)
    joy_tweets_reg = pandas.read_csv(DATA_PATH_JOY_TWEETS_REG, sep='\t', header=0)
    joy_tweets_reg_dev = pandas.read_csv(DATA_PATH_JOY_TWEETS_REG_DEV, sep='\t', header=0)
    joy_tweets_crowdfowler = pandas.read_csv(DATA_PATH_JOY_CROWDFOWLER, header=0)

    actual_joy_tweets = joy_tweets[joy_tweets['Intensity Class'] != '0: no joy can be inferred'].copy()
    actual_joy_tweets_dev = joy_tweets_dev[
        joy_tweets_dev['Intensity Class'] != '0: no joy can be inferred'].copy()
    actual_joy_tweets_reg = joy_tweets_reg[joy_tweets_reg['Intensity Score'] > 0.1].copy()
    actual_joy_tweets_dev_reg = joy_tweets_reg_dev[joy_tweets_reg_dev['Intensity Score'] > 0.1].copy()
    joy_tweets_crowdfowler = joy_tweets_crowdfowler[joy_tweets_crowdfowler['label'] == 'happiness'].copy()
    joy_tweets_crowdfowler.rename(columns={'features': 'Tweet'}, inplace=True)


    joy_tweets = pandas.DataFrame({'Tweet': actual_joy_tweets['Tweet'].copy()})
    joy_tweets.append(actual_joy_tweets_dev['Tweet'])
    joy_tweets.append(actual_joy_tweets_reg['Tweet'])
    joy_tweets.append(actual_joy_tweets_dev_reg['Tweet'])

    joy_tweets['Label'] = 'joy'
    joy_tweets_crowdfowler['Label'] = 'joy'

    joy_tweets.to_csv('./annotated data/tweets_joy.csv', columns=['Tweet', 'Label'], encoding='utf-8', index=False, header=False, mode='a')
    joy_tweets_crowdfowler.to_csv('./annotated data/tweets_joy.csv', columns=['Tweet', 'Label'], encoding='utf-8', index=False, header=False, mode='a')

extract_and_save_joy_tweets()
