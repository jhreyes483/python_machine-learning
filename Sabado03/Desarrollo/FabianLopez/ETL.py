
import csv
import datetime
import uuid
import iso8601 as iso8601
import numpy
import snscrape.modules.twitter as sntwitter
import pandas as pd
from deep_translator import GoogleTranslator
from mysql import connector

def connection():
    conexion = connector.connect(host='localhost', user='root', password='')
    return conexion

def extraccion():
    maxTweets = 100
    tweets_list2 = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper('feliz since:2020-08-01 until:2022-12-01').get_items()):
        if i > maxTweets:
            break
        tweets_list2.append([
            tweet.date,
            tweet.url,
            tweet.lang,
            tweet.retweetCount,
            tweet.id,
            tweet.content,
            tweet.user.username
        ])

    tweets_df2 = pd.DataFrame(tweets_list2,
                              columns=[
                                  'Datetime',
                                  'url of tweet',
                                  'lenguaje',
                                  're-twittes',
                                  'Tweet Id',
                                  'Text',
                                  'Username'
                              ])
    tweets_df2.head()
    tweets_df2.to_csv('text-query-tweets.csv', sep=',', index=False)


def transform():
    data = []
    with open('text-query-tweets.csv', encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')

        for row in spamreader:
            if (spamreader.line_num > 1):
                row[0] = datetime.datetime.fromisoformat(row[0])
                row[5] = row[5].format("utf-8")
                if (row[2] != 'es'):
                    translation = GoogleTranslator(
                        source='auto', target='es').translate(row[5])
                    row[5] = translation
                    row[5] = row[5].encode('ascii', errors='ignore')
                data.append(row)
    return data


def load(dataclean):
    cur = dbconn.cursor()
    arraySize = len(dataclean)
    for r in range(0, arraySize):
        try:
            uuidstr = uuid.uuid4()
            cur.execute('SET NAMES utf8mb4')
            cur.execute("SET CHARACTER SET utf8mb4")
            cur.execute("SET character_set_connection=utf8mb4")
            cur.execute(
                """INSERT INTO tweets(id,fecha,url, lenguaje,`re-tweets`, `tweet ID`, contenido, usuario) VALUES( %s,%s,%s,%s,%s,%s,%s,%s)""",
                (str(uuidstr), dataclean[r][0], dataclean[r][1], dataclean[r][2], dataclean[r][3], dataclean[r][4],
                 dataclean[r][5], dataclean[r][6]))
            dbconn.commit()
        except ValueError:
            print("Error")
            print(ValueError)
    pass


if __name__ == '__main__':

    print('realizando extracción')
    extraccion()

    print('realizando transformación')
    dataclean = transform()
    dataclean.pop(0)
    an_array = numpy.array(dataclean)
    print(an_array)
    show_db_query = "use etl"
    dbconn = connection()
    cur = dbconn.cursor()
    cur.execute(show_db_query)
    for x in cur:
        print(x)

    print('realizando carga de datos')
    load(dataclean)
