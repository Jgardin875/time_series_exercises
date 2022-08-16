#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

import requests


# In[2]:


import os

def get_zgulde_data():
    filename = "merged_zgulde.csv"
    
    # if file is available locally, read it
    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col = 0)
    
    # if file not available locally, acquire data from SQL database
    # and write it as csv locally for future use
    else:
        return print('use new_zgulde_data')


# In[3]:


def new_zgulde_data(items, stores, sales):
    # setup
    domain = 'https://python.zgulde.net'
    endpoint = '/api/v1/items'
    items = []

    while endpoint != None:
        url = domain + endpoint
        response = requests.get(url)
        data = response.json()
        items.extend(data['payload']['items'])
        # update the endpoint
        endpoint = data['payload']['next_page']
    items = pd.DataFrame(items)
    
    url = 'https://python.zgulde.net/api/v1/stores'
    response = requests.get(url)
    stores = response.json()
    
    # setup
    domain = 'https://python.zgulde.net'
    endpoint = '/api/v1/sales'
    sales = []

    while endpoint != None:
        url = domain + endpoint
        response = requests.get(url)
        data = response.json()
        sales.extend(data['payload']['sales'])
        # update the endpoint
        endpoint = data['payload']['next_page']
    sales = pd.DataFrame(sales)
    
    zgulde = sales.merge(items, how='left', left_on='item', right_on='item_id')
    
    zgulde = zgulde.merge(stores, how='left', left_on='store', right_on='store_id')
    
    zgulde.drop(columns=['item', 'sale_id', 'item_id', 'item_upc12', 'item_upc14', 'store_id'], inplace=True)   
      
    return zgulde


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




