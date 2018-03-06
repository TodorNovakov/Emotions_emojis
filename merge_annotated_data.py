import pandas
import os

CURRENT_DIR_PATH = os.path.dirname(os.path.realpath(__file__))

DATA_PATH_JOY_TWEETS = CURRENT_DIR_PATH + '/annotated data/tweets_joy.csv'
DATA_PATH_ANGER_TWEETS = CURRENT_DIR_PATH + '/annotated data/tweets_anger.csv'
DATA_PATH_FEAR_TWEETS = CURRENT_DIR_PATH + '/annotated data/tweets_fear.csv'
DATA_PATH_SADNESS_TWEETS = CURRENT_DIR_PATH + '/annotated data/tweets_sadness.csv'


def load_and_concatenate_data():
    fear_tweets = pandas.read_csv(DATA_PATH_FEAR_TWEETS, header=None)
    joy_tweets = pandas.read_csv(DATA_PATH_JOY_TWEETS, header=None)
    sadness_tweets = pandas.read_csv(DATA_PATH_SADNESS_TWEETS, header=None)
    anger_tweets = pandas.read_csv(DATA_PATH_ANGER_TWEETS, header=None)

    fear_tweets.to_csv('./annotated data/merged_tweets.csv', encoding='utf-8', index=False, header=False, mode='a')
    joy_tweets.to_csv('./annotated data/merged_tweets.csv', encoding='utf-8', index=False, header=False, mode='a')
    sadness_tweets.to_csv('./annotated data/merged_tweets.csv', encoding='utf-8', index=False, header=False, mode='a')
    anger_tweets.to_csv('./annotated data/merged_tweets.csv', encoding='utf-8', index=False, header=False, mode='a')


load_and_concatenate_data()