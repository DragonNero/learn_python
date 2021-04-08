import matplotlib.pyplot as plt

# x-axis values
x = [1,2,3,4,5,6,7,8]
# y-axis values
y = [5, 12, 18, 20, 15, 9, 4, 2]

# plotting points as a scatter plot
plt.subplot(222)
plt.plot(x, y, label= "line", color= "green")

# x-axis label
plt.xlabel('x - cm')
# frequency label
plt.ylabel('y - individuals')
# plot title
plt.title('My scatter plot!')
# showing legend
plt.legend()

# function to show the plot
plt.show()
#N° of observations: 75 1 cm x 5 individuals2 cm x 12 individuals3 cm x 18 individuals4 cm x 20 individuals5 cm x 15 individuals6 cm x 9 individuals7 cm x 4 individuals8 cm x 2 individuals
