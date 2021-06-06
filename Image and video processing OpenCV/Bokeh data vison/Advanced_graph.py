# Making an advanced Bokeh graph 

#importing Bokeh and pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

#prepare some data 
df = pandas.read_excel("verlegenhuken.xlsx")

#clean the data - this has a scale of 10 in the file
df["Temperature"]=df["Temperature"]/10
df["Pressure"]=df["Pressure"]/10


#prepare the output
output_file("Weather_Data.html")

#create Figure object
f = figure()

#name the axis
f.xaxis.axis_label="Temp(C)"
f.yaxis.axis_label="Pressure (hPa)" 

#create plot
f.circle(df["Temperature"],df["Pressure"],size = 0.3)

#write the plot
show(f)