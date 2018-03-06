import pandas
import os
import emojilib
import re

CURRENT_DIR_PATH = os.path.dirname(os.path.realpath(__file__))

DATA_PATH_TWEETS = CURRENT_DIR_PATH + '/annotated data/merged_tweets.csv'

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
    tweets = pandas.read_csv(DATA_PATH_TWEETS, header=None, names=['tweet', 'label'])
    tweets['tweet'].to_csv('./annotated data/no_annotated_tweets.txt', encoding='utf-8', index=False, header=False)

    out_text = open("./annotated data/tweets.text.cleaned.txt", 'w')
    out_emojis_name = open("./annotated data/tweets.emoji.name.txt", 'w')
    out_emojis_code = open("./annotated data/tweets.emoji.code.txt", 'w')

    tot = 0
    ok = 0

    with open('./annotated data/no_annotated_tweets.txt') as f_in:
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
            else:
                ct = clean_text(text)
                out_text.write(ct + "\n")

                for emo_name in emo_set_name:
                    out_emojis_name.write(emo_name + " ")
                out_emojis_name.write("\n")

                for emo_code in emo_set_code:
                    out_emojis_code.write(emo_code + " ")
                out_emojis_code.write("\n")

            if tot % 10000 == 0:
                print(str(tot))
            tot += 1

    out_text.close()
    out_emojis_name.close()
    out_emojis_code.close()

get_emojis()
