# importing the required module
import matplotlib.pyplot as plt

# x axis values
x = [1,2,3]
# corresponding y axis values
y = [2,4,1]


#1 cm x 5 individuals2 cm x 12 individuals3 cm x 18 individuals4 cm x 20 individuals5 cm x 15 individuals6 cm x 9 individuals7 cm x 4 individuals8 cm x 2 individuals

# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

# function to show the plot
plt.show()
