from django.shortcuts import render
from django.views import View
import pandas as pd
import numpy as np
import plotly.express as px
import jalali_pandas
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import warnings
warnings.filterwarnings('ignore')
from plotly.offline import plot
from plotly.graph_objs import Scatter
df=pd.read_csv('df.csv')
df_dg=pd.read_csv('digital.csv')
def get_sum(warehouse_id):
    s=df[df['warehouse id']==warehouse_id]
    total = s['purchase price'].sum()
    return f'{int(total):,} IRR'

class IndexView(View):
    def get(self,request):
        
        six=get_sum(6)
        five=get_sum(5)
        x_data = [0,1,2,3]
        y_data = [x**2 for x in x_data]
        fig = px.line(df.groupby('Edit Date')['purchase price'].sum())
        fig.update_layout(
            template='plotly_dark',
            hovermode='x unified',)

        chart=fig.to_html()

        brand = df_dg.groupby('Brand').size().reset_index()
        brand.columns=['Brand','Count']
        fig2=px.pie(brand,names=brand['Brand'],values=brand['Count'],color='Count',hover_name='Brand')
        fig2.update_layout(template='plotly_dark',title='Digital Separated by Brand')
        chart2=fig2.to_html()

        fig3 = px.treemap(df, path=['warehouse name', 'Brand'],
                 values='purchase price',color='purchase price')
        fig3.update_layout(template='plotly_dark',title='Treemap separated by Brand')
        chart3=fig3.to_html()

        return render(request,'report/index.html',{'six':six,'five':five,'chart':chart,'chart2':chart2,'chart3':chart3})
    def post(self,request):
        return render(request,'report/index.html')
