from pandas_datareader import data
from datetime import datetime
from datetime import timedelta

stocksymbol="MARUTI.NS"

now=datetime.now()
end=now.date()
start=end+timedelta(days=-365)
print(end)
print(start)
df=data.DataReader(name=stocksymbol,data_source="yahoo",start=start,end=end)

#to make graphs, we need bokeh
from bokeh.plotting import figure,show,output_file

def inc_dec(c,o):
    if c>o:
        value="Increase"
    elif c<o:
        value="Decrease"
    else:
        value="No Change"
    return value
#making new column to store status

df["Status"]=[inc_dec(c,o) for c,o in zip(df.Close,df.Open)]

df["Middle"]=(df.Open+df.Close)/2
df["Height"]=abs(df.Close-df.Open)

hours_12=12*60*60*1000

#to create the actual figure
#responsive=true so chart fits the page
p=figure(x_axis_type="datetime",width=1000,height=300)
p.title.text="Candlestick Chart"
p.xaxis.axis_label = "TimePeriod"
p.yaxis.axis_label = "StockPrice"
#to reduce opacity
p.grid.grid_line_alpha=0.4

#for segment
p.segment(df.index,df.Low,df.index,df.High,line_color="red")
#for rectangles
p.rect(df.index[df.Status=="Increase"],df.Middle[df.Status=="Increase"],hours_12,df.Height[df.Status=="Increase"],fill_color="#33CC66",line_color="green")
p.rect(df.index[df.Status=="Decrease"],df.Middle[df.Status=="Decrease"],hours_12,df.Height[df.Status=="Decrease"],fill_color="#FF3333",line_color="green")
df.to_csv('rk.csv')

output_file("g1.html")
show (p)
