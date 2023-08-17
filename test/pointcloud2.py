import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Read point cloud data from the text file
point_cloud = []
with open('amp_cloud.txt', 'r') as f:
    for line in f:
        x, y, depth_value = map(float, line.strip().split())
        point_cloud.append((x, y, depth_value))

# Separate x, y, and z values for plotting
x_vals, y_vals, z_vals = zip(*point_cloud)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot the points
ax.scatter(x_vals, y_vals, z_vals, c=z_vals, cmap='viridis')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Depth')
ax.set_title('3D Point Cloud')

plt.show()
