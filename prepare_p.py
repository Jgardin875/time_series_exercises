#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import acquire_p
import matplotlib.pyplot as plt


# In[87]:


def fillna(df, values):
    df.fillna(value=values, inplace =True)
    return df


# In[24]:


def convert_time(col):
    col = pd.to_datetime(col, infer_datetime_format=True)
    return col


# In[67]:


def convert_index(df, col):
    df = df.set_index(col)
    return df


# In[57]:



def hist_enum(df, col):
    plt.figure(figsize=(16, 3))

    for i, col in enumerate(col):

        # i starts at 0, but plot nos should start at 1
        plot_number = i + 1

        # Create subplot.
        # plt.subplot(row X col, where?)
        plt.subplot(1,4,plot_number)

        # Title with column name.
        plt.title(col)

        # Display histogram for column.
        df[col].hist(bins=5, edgecolor='black')

        # Hide gridlines.
        plt.grid(False)


# In[84]:


def time_metric_col(df):
    df['month'] = df.index.month_name()
    df['weekday'] = df.index.day_name()
    df['year'] = df.index.year
    return df


# In[94]:


def col_mult_function(df, col1, col2):
    df['product'] = col1 *col2
    return df

