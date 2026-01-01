import matplotlib.pyplot as plt

# # line chart 
# x=[4,6,7,8,9]
# y=[5,6,2,8,5]

# plt.plot(x,y)
# plt.xlabel("X-axis")
# plt.ylabel("Y-label")
# plt.title("Graph type - line chart")
# plt.show()

# # bar chart 
# categories=['A','B','C','D','E','F']
# values=[40,70,30,85,10,45]

# plt.bar(categories,values)
# plt.xlabel("Categories")
# plt.ylabel("Values")
# plt.title("Bar Chart Example")
# plt.show()


# # histogram chart
# data=[12,15,14,16,18,19,20,22,24,25]

# plt.hist(data,bins=5)
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.title("Histogram Example")
# plt.show()


# # scatter chart
# x=[1,2,3,4,5]
# y=[5,7,4,8,6]

# plt.scatter(x,y)
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("Scatter Plot")
# plt.show()


# # pie chart
# labels=['Python','Java','C++','Others']
# sizes=[45,25,15,15]

# plt.pie(sizes,labels=labels,autopct='%1.1f%%')
# plt.title("Programming Language Usage")
# plt.show()

x = [1, 2, 3, 4]
y1 = [10, 20, 30, 40]
y2 = [15, 25, 35, 45]

plt.plot(x, y1, label="Line 1")
plt.plot(x, y2, label="Line 2")
plt.legend()
plt.show()