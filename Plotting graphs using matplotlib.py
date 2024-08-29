#Plotting graphs

x = [1, 3, 5, 10]
#importing the relevant modules
import matplotlib.pyplot as plt
plt.plot(x)
plt.show() # actually shows the plot
y = [7, 12, 21, 22]
plt.plot(x, y)
plt.show() # Lists must be the same shape/dimensions

#Line 1 - Points
x = [3, 9, 14]
y = [2, 7, 30]
plt.plot(x, y, c="red", linewidth=2, label="Line 1")

#Line 2 - points
x2 = [1, 15, 18]
y2 = [0, 3, 12]
plt.plot(x2, y2, c="green", linewidth=5, label="Line 2")

plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Two lines")
plt.legend()
plt.show()
#plot figure helps to sperate different plots onto different graphs



x = [3, 9, 14]
y = [2, 7, 30]
plt.plot(x, y, c="green", linewidth=2, label="Line 1", linestyle="dashed", marker='s', markerfacecolor="purple", markersize=10)
plt.show()
#marker = o for round, s for square

#Limits for the axis
plt.ylim(1, 10)
plt.xlim(1, 10)

#other graphs to research: pie chart, histrogram etc...