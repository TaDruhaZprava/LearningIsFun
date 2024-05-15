import pandas as pd
import math
import json
import csv

netflix = pd.read_csv('netflix_titles.tsv', sep='\t')
netflix = netflix.drop(['TCONST', 'TITLETYPE', 'ORIGINALTITLE', 'ISADULT',
                        'ENDYEAR', 'RUNTIMEMINUTES', 'AVERAGERATING',
                        'NUMVOTES', 'TITLETYPE_NEW', 'SHOW_ID', 'TYPE', 'TITLE',
                        'COUNTRY', 'DATE_ADDED', 'RELEASE_YEAR', 'RATING', 'DURATION',
                        'LISTED_IN', 'DESCRIPTION'], axis='columns')

netflix = netflix[['PRIMARYTITLE', 'DIRECTOR', 'CAST', 'GENRES', 'STARTYEAR']]

netflix.to_csv('netflix.csv', sep=',', header=False,
               index=False, mode='w', encoding='UTF-8')

netflix_composed = []
with open('netflix.csv', encoding='utf-8') as file:
    data = csv.DictReader(file, delimiter=',', fieldnames=[
                          'title', 'directors', 'cast', 'genres', 'decade'])
    for line in data:
        netflix_composed.append(line)

for n in netflix_composed:
    n['decade'] = math.floor(int(n['decade'])/10) * 10
    n['directors'] = n['directors'].split(', ')
    n['cast'] = n['cast'].split(', ')
    n['genres'] = n['genres'].split(', ')
    if n['directors'] == ['']:
        n['directors'] = []
    elif n['cast'] == ['']:
        n['cast'] = []

with open('hw02_output.json', mode='w', encoding='utf-8') as output_file:
    json.dump(netflix_composed, output_file, ensure_ascii=False, indent=4)