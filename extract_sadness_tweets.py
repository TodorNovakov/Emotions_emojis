import pandas
import os
import emojilib
import re

CURRENT_DIR_PATH = os.path.dirname(os.path.realpath(__file__))

DATA_PATH_SADNESS_TWEETS = CURRENT_DIR_PATH + '/data/EI-oc-En-train (1)/EI-oc-En-sadness-train.txt'
DATA_PATH_SADNESS_TWEETS_DEV = CURRENT_DIR_PATH + '/data/2018-EI-oc-En-dev (1)/2018-EI-oc-En-sadness-dev.txt'
DATA_PATH_SADNESS_TWEETS_REG = CURRENT_DIR_PATH + '/data/EI-reg-En-train (1)/EI-reg-En-sadness-train.txt'
DATA_PATH_SADNESS_TWEETS_REG_DEV = CURRENT_DIR_PATH + '/data/2018-EI-reg-En-dev (1)/2018-EI-reg-En-sadness-dev.txt'
DATA_PATH_SADNESS_CROWDFOWLER = CURRENT_DIR_PATH + '/data/dfe_happysad_utf.csv'


def extract_and_save_sadness_tweets():
    sadness_tweets = pandas.read_csv(DATA_PATH_SADNESS_TWEETS, sep='\t', header=0)
    sadness_tweets_dev = pandas.read_csv(DATA_PATH_SADNESS_TWEETS_DEV, sep='\t', header=0)
    sadness_tweets_reg = pandas.read_csv(DATA_PATH_SADNESS_TWEETS_REG, sep='\t', header=0)
    sadness_tweets_reg_dev = pandas.read_csv(DATA_PATH_SADNESS_TWEETS_REG_DEV, sep='\t', header=0)
    sadness_tweets_crowdfowler = pandas.read_csv(DATA_PATH_SADNESS_CROWDFOWLER, header=0)

    actual_sadness_tweets = sadness_tweets[sadness_tweets['Intensity Class'] != '0: no sadness can be inferred'].copy()
    actual_sadness_tweets_dev = sadness_tweets_dev[
        sadness_tweets_dev['Intensity Class'] != '0: no sadness can be inferred'].copy()
    actual_sadness_tweets_reg = sadness_tweets_reg[sadness_tweets_reg['Intensity Score'] > 0.1].copy()
    actual_sadness_tweets_dev_reg = sadness_tweets_reg_dev[sadness_tweets_reg_dev['Intensity Score'] > 0.1].copy()
    sadness_tweets_crowdfowler = sadness_tweets_crowdfowler[sadness_tweets_crowdfowler['label'] == 'sadness'].copy()
    sadness_tweets_crowdfowler.rename(columns={'features': 'Tweet'}, inplace=True)

    sadness_tweets = pandas.DataFrame({'Tweet': actual_sadness_tweets['Tweet'].copy()})
    sadness_tweets.append(actual_sadness_tweets_dev['Tweet'])
    sadness_tweets.append(actual_sadness_tweets_reg['Tweet'])
    sadness_tweets.append(actual_sadness_tweets_dev_reg['Tweet'])

    sadness_tweets['Label'] = 'sadness'
    sadness_tweets_crowdfowler['Label'] = 'sadness'

    sadness_tweets.to_csv('./annotated data/tweets_sadness.csv', columns=['Tweet', 'Label'], encoding='utf-8', index=False, header=False, mode='a')
    sadness_tweets_crowdfowler.to_csv('./annotated data/tweets_sadness.csv', columns=['Tweet', 'Label'], encoding='utf-8', index=False, header=False, mode='a')

extract_and_save_sadness_tweets()
