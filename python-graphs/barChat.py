import matplotlib.pyplot as plt

# x-coordinates of left sides of bars
left = [1, 2, 3, 4, 5, 6, 7, 8]

# heights of bars
height = [5, 12, 18, 20, 15, 9, 4, 2]

# labels for bars
tick_label = ['1cm', '2cm', '3cm', '4cm', '5cm','6cm', '7cm', '8cm']

# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
		width = 0.8, color = ['green'])

# naming the x-axis
plt.xlabel('x - cm')
# naming the y-axis
plt.ylabel('y - individuals')
# plot title
plt.title('graph of the size frequency distribution of Mytilus galloprovincialis length')

# function to show the plot
plt.show()
