#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[38]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# In[39]:


df = pd.read_csv(r'c:/users/srinivas/Data_Analysis_Project 3/boilerplate-medical-data-visualizer-main/medical_examination.csv')


# 1. Importing data and saving in df

# In[40]:


df


# 2. Add 'overweight' column

# In[41]:


df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)


# In[42]:


df


# 3. Normalize data by making 0 always good and 1 always bad

# In[43]:


df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


# In[44]:


df


# 4. Draw Categorical Plot

# In[45]:


def draw_cat_plot():
    # 5. Creating DataFrame for cat plot using pd.melt
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )

    # 6. Grouping and reformating the data to split it by cardio
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']) \
                   .size() \
                   .reset_index(name='total')

    # 7. Drawing the catplot
    fig = sns.catplot(
        data=df_cat,
        kind='bar',
        x='variable',
        y='total',
        hue='value',
        col='cardio'
    ).fig

    return fig

# 8. Heat Map
def draw_heat_map():
    
    # 9. Cleaning the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 10. Calculating the correlation matrix
    corr = df_heat.corr()

    # 11. Generating a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 12. Seting up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # 13. heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5}
    )

    return fig

    


# In[ ]:





# In[ ]:




