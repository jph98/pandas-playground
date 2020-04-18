#!/usr/bin/env python3

from termcolor import colored

import pandas as pd
import numpy as np

def describe(df):
    print(colored('Dataset Description\n', 'green'))
    overview = df.describe()
    print(overview.to_csv())

def head(df):
    print(colored('Dataset Head\n', 'green'))
    print(df.head())

def describe_max(df):
    print(colored('Dataset Description\n', 'green'))
    pd.set_option('display.max_columns', None)
    df.describe()

def sample(df):
    print(colored('Dataset Sample\n', 'green'))
    df.sample(n=100)

def rows_cols(df):

    print(colored('Dataset Rows and Cols\n', 'green'))

    # Get the number of rows
    print('Number of rows: %d' % len(df.index))

    # Get column names, get number of columns        
    print('Number of columns: %d' % len(df.columns))

    # Print columns
    print('Columns: %s' % (' '.join(df.columns)))    

def get_game(df):
    print(colored('Game\n', 'green'))
    print(df.loc[0])

def get_game_names(df):
    print(colored('Game Names\n', 'green'))
    print(df.loc[0:1,['Name']])

def get_all_genres(df):
    print(colored('All Game Genres\n', 'green'))
    print(df['Genre'].unique())

def get_all_games_over_score(df, score):
    print(colored('All Game Over Score %f\n' % score, 'green'))
    print(df[df.Vgchartzscore > score].sort_values(['Vgchartzscore']).head(5))

def dump_to_csv(df):
    print('Dumping to CSV')
    df.to_csv('outputfile.csv')

def drop_rank_col(df):
    print(colored('Drop rank col', 'green'))
    df = df.drop(['Rank'], axis=1)
    print(df)

def groupby(df):
    print(colored('Games grouped by genre', 'green'))
    genre_grouped = df.groupby('Genre').first()
    print(genre_grouped)

    print(colored('Number of games per genre', 'green'))
    print(df.groupby('Genre').size())

    print(colored('Games by genre then platform', 'green'))
    print(df.groupby(['Genre', 'Platform']).first())

def aggregate_fn(df):
    print(colored('Global sales mean and sum ', 'green'))
    g = df.groupby(['Genre', 'Platform'])
    res = g['Global_Sales'].agg(["mean", "sum"])
    print(res)


df = pd.read_csv('vgsales-12-4-2019.csv')
aggregate_fn(df)