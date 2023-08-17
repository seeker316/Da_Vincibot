import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image

# Load the depth image
depth_image = Image.open('output_image.jpg')  # Replace with your depth image file
depth_map = np.array(depth_image)

# Define camera parameters
focal_length_x = 500
focal_length_y = 500
center_x = depth_map.shape[1] / 2
center_y = depth_map.shape[0] / 2

# Create meshgrid
x, y = np.meshgrid(np.arange(depth_map.shape[1]), np.arange(depth_map.shape[0]))

# Convert depth map to 3D point cloud
point_cloud_x = (x - center_x) * depth_map / focal_length_x
point_cloud_y = (y - center_y) * depth_map / focal_length_y
point_cloud_z = depth_map

# Replace colors with numerical values (for example, depth values)
# You can modify this based on the numerical data you want to use
numerical_values = point_cloud_z.flatten()

# Normalize numerical values to use as colors
min_value = numerical_values.min()
max_value = numerical_values.max()
normalized_values = (numerical_values - min_value) / (max_value - min_value)

# Visualize the 3D point cloud with colored points
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(point_cloud_x, point_cloud_y, point_cloud_z, c=normalized_values, s=1, cmap='viridis')
fig.colorbar(scatter, ax=ax, label='Numerical Values')  # Add colorbar to show value-to-color mapping
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Depth')
plt.show()

# Plane fitting code (same as before)
points = np.stack((point_cloud_x.flatten(), point_cloud_y.flatten(), point_cloud_z.flatten()), axis=-1)
coefficients = np.linalg.lstsq(points, -point_cloud_z.flatten(), rcond=None)[0]
A, B, C = coefficients
D = -1
print(f"Equation of the plane: {A}x + {B}y + {C}z + {D} = 0")
