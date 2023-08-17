import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image

# Load your JPG depth image and convert it to grayscale
depth_image = Image.open('images/bin_img.jpg')
depth_array = np.array(depth_image)
print(depth_array)



# Create a grid of coordinates based on the image size
rows, cols = depth_array.shape
x = np.arange(0, cols)
y = np.arange(0, rows)
x_grid, y_grid = np.meshgrid(x, y)

# Flatten the grids and the depth array to create the point cloud
x_points = x_grid.flatten()
y_points = y_grid.flatten()
z_points = depth_array.flatten()

# Remove invalid depth values (you can adjust the threshold)
valid_indices = np.where(z_points > 0)
x_points = x_points[valid_indices]
y_points = y_points[valid_indices]
z_points = z_points[valid_indices]

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the point cloud
ax.scatter(x_points, y_points, z_points, c=z_points, cmap='jet')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Depth')
ax.set_title('10')

# Show the plot
plt.show()