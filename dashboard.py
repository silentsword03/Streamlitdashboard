#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit


# In[2]:


st.set_page_config(page_title="Emplyee_Performance", page_icon=":bar_chart:", layout="wide")


# In[3]:


df = pd.read_excel(io="Raw_data.xlsx",engine="openpyxl",nrows=1000)


# In[4]:


mask = df['Agents'].isin(["Nikita De' Lange",'Shesham Venkata Varun','Pooja T','Huma Anjum','Priyanka Seethiraju','Bhavneet.chaddha','Sandhya Lakshmi CH','Amal TV','Shada Sadiq','Puli Anusha','Aquib Shaik','Kabeer Ahmed N','Sandesh N'])
df=df[mask]


# In[5]:


df.reset_index(drop=True)


# In[6]:


df['Total_Surveys'] = df[['Rating 1 Star','Rating 2 Star','Rating 3 Star','Rating 4 Star','Rating 5 Star']].sum(axis=1)


# In[7]:


df['sum'] = df['Rating 1 Star'].apply(lambda x: x*1) + df['Rating 2 Star'].apply(lambda x: x*2) + df['Rating 3 Star'].apply(lambda x: x*3) +  df['Rating 4 Star'].apply(lambda x: x*4) +  df['Rating 5 Star'].apply(lambda x: x*5)


# In[8]:


df['Csat_Score'] = df['sum'] / df['Total_Surveys']
df['Csat_Score']=df['Csat_Score'].round(2)


# In[9]:


df['Csat_Percentage'] = df['Csat_Score']/5*100


# In[10]:


df['TTFR'] = df['Time to First Response'] /3600
df['TTFR'] = df['TTFR'].round(2)


# In[11]:


df


# In[12]:


df.columns


# In[13]:


df['Time to First Response'] = df['Time to First Response'] / 60000


# In[14]:


df['Time to First Response'] = df['Time to First Response'].round(2)


# In[15]:


df['Holding Time'] = df['Holding Time'] / 60000


# In[16]:


df['Holding Time'] = df['Holding Time'].round(2)


# In[17]:


df['Average Time to Resolve'] = df['Average Time to Resolve'] / 60000


# In[18]:


df['Average Time to Resolve'] = df['Average Time to Resolve'].round(2)


# In[19]:


df['Median Time to Resolve'] = df['Median Time to Resolve'] / 60000


# In[20]:


df['Median Time to Resolve'] = df['Median Time to Resolve'].round(2)


# In[21]:


df.reset_index(drop=True)


# In[22]:


df.drop(['sum'], axis=1,inplace=True)


# In[23]:


df


# In[24]:


st.sidebar.header("Filter Here:")
Agents = st.sidebar.multiselect(
    "Select the Agents:",
    options=df["Agents"].unique(),
    default=df["Agents"].unique()
)


# In[25]:


df_selection = df.query('Agents == @Agents')


# #  Main Page
# 

# In[26]:


st.title(':bar_chart: Team Metrics Dashboard')
st.markdown('##')


# # TOP KPI'S
# 

# In[27]:


total_surveys = int(df['Total_Surveys'].sum()) # Total No of surveys for the Team


# In[28]:


Average_Csat_Score = round(df['Csat_Score'].mean(), 1) # Average CSAT Team level


# In[29]:


star_rating = ':star:' * int(round(Average_Csat_Score, 0))


# In[30]:


Average_TTFR = round(df['TTFR'].mean(), 1)


# In[31]:


left_column, middle_column, right_column = st.columns(3)


# In[32]:


with left_column:
    st.subheader('Total Surveys:')
    st.subheader(f'✔ {total_surveys: ,}')
    
    


# In[33]:


with middle_column:
    st.subheader('Average Csat Score:')
    st.subheader(f'{Average_Csat_Score} {star_rating}')
    


# In[34]:


with right_column:
    st.subheader('Average TTFR:')
    st.subheader(f'🕐 {total_surveys: ,}')


# In[35]:


st.dataframe(df)


# In[ ]:




