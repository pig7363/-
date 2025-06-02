import matplotlib.pyplot as plt

plt.style.use('dark_background')
x_data = [1, 2, 3, 4, 5, 6]
y_data = [1, 4, 9, 16, 25, 36]
levels = [208, 310, 481, 124, 223, 555]
# colors = ['green', 'olive', 'green', 'olive', 'green', '#341256']
fig, ax = plt.subplots()

ax.plot(x_data, y_data, linewidth=10, color='green')
ax.bar(x_data, y_data)
ax.scatter(x_data, y_data, c=levels, s=levels,
           cmap=plt.cm.get_cmap('viridis'),
           edgecolors='none')
ax.set_xlabel('Value of x', fontsize=16)
ax.set_ylabel('Square of x', fontsize=16)
ax.set_title('Squares', fontsize=24)
ax.tick_params(labelsize=14)
plt.show()