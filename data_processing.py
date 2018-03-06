import pandas
import os
import emojilib
import re

CURRENT_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH_SADNESS_TWEETS = CURRENT_DIR_PATH + '/data/EI-oc-En-train (1)/EI-oc-En-sadness-train.txt'


def load_tweets():
    with open(DATA_PATH_SADNESS_TWEETS) as f:
        content = f.read().splitlines()

    return content


def extract_emojis(str):
    return ''.join(c for c in str if c in emojilib.UNICODE_EMOJI)


def load_data():
    sadness_tweets = pandas.read_csv(DATA_PATH_SADNESS_TWEETS, sep='\t', header=0)

    # sadness_tweets['Tweet'].to_csv("sadness_tweets_text.csv", encoding='utf-8', index=False, header=False)

    new_data = pandas.DataFrame(sadness_tweets['Tweet'].copy())
    new_data['Emoji'] = extract_emojis(new_data['Tweet'])

    print(new_data.head(10))


def clean_text(text):
    # remove emojis, remove links, anonymize user mentions
    clean = ""
    text = emojilib.replace_emoji(text, replacement=' ')
    text = re.sub('\s+', ' ', text).strip()
    for t in text.split(" "):
        if t.startswith('@') and len(t) > 1:
            clean += "@user "
        elif t.startswith('http'):
            pass
        else:
            clean += t + " "
    # remove double spaces
    return clean


def get_emojis():
    out_text = open("tweets.sadness.text", 'w')
    out_emojis_name = open("tweets.sadness.emoji.name.txt", 'w')
    out_emojis_code = open("tweets.sadness.emoji.code.txt", 'w')
    tot = 0
    ok = 0

    with open(DATA_PATH_SADNESS_TWEETS) as f_in:
        for line in f_in:
            text = line.replace("\n", "")
            emo_list = emojilib.emoji_list(text)
            emo_set_name = set([d['name'] for d in emo_list if 'name' in d])
            emo_set_code = set([d['code'] for d in emo_list if 'code' in d])
            if len(emo_set_name) == 1:
                emo_name = emo_set_name.pop()
                emo_code = emo_set_code.pop()
                ct = clean_text(text)
                out_text.write(ct + "\n")
                out_emojis_name.write(emo_name + "\n")
                out_emojis_code.write(emo_code + "\n")
                ok += 1
            if tot % 10000 == 0:
                print(str(tot))
            tot += 1

    out_text.close()
    out_emojis_name.close()
    out_emojis_code.close()


get_emojis()
