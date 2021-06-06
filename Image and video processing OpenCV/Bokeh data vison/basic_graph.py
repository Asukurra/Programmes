# Making a basic Bokeh line graph 

#importing Bokeh 
from bokeh.plotting import figure
from bokeh.io import output_file, show

#prepare some data 
x = [1,2,3,4,5]
y = [6,7,8,9,10]
# for Bokeh the lists need the same amount 

#prepare the output
output_file("test_line_graph.html")

#create Figure object
f = figure()

#create line plot
f.line(x,y)

show(f)


######################################################################################################
# importing from CSV method below

# Making a basic Bokeh line graph 

# #importing Bokeh and pandas
# from bokeh.plotting import figure
# from bokeh.io import output_file, show
# import pandas

# #prepare some data 
# df = pandas.read_csv("bachelors.csv")
# x = df["Year"]
# y = df["Engineering"]

# # for Bokeh the lists need the same amount 

# #prepare the output
# output_file("Education_Data.html")

# #create Figure object
# f = figure()

# #create line plot
# f.line(x,y)

# #write the plot
# show(f)

######################################################################################################

# You can add a title to the plot, set the figure width and height, change title font, etc. Below is a summary of properties which can be added to change the style of the plot:

# import pandas
# from bokeh.plotting import figure, output_file, show

# p=figure(plot_width=500,plot_height=400, tools='pan',logo=None)

# p.title.text="Cool Data"
# p.title.text_color="Gray"
# p.title.text_font="times"
# p.title.text_font_style="bold"
# p.xaxis.minor_tick_line_color=None
# p.yaxis.minor_tick_line_color=None
# p.xaxis.axis_label="Date"
# p.yaxis.axis_label="Intensity"    

# p.line([1,2,3],[4,5,6])
# output_file("graph.html")
# show(p)