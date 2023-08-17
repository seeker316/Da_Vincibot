import cv2
import numpy as np
from sklearn.cluster import DBSCAN

# Read the depth image
depth_image = cv2.imread('col_output_image2.jpg', cv2.IMREAD_UNCHANGED)

# Voxelization parameters (adjust as needed)
voxel_size = 10  # Size of the 3D regions
threshold_distance = 0.05  # Threshold for DBSCAN clustering

# Create voxelized depth image
voxel_depth_image = depth_image // voxel_size

# Reshape depth data for processing
voxel_depth_data = voxel_depth_image.reshape(-1, 1)

# Perform DBSCAN clustering on voxelized depth data
dbscan = DBSCAN(eps=threshold_distance, min_samples=10)
labels = dbscan.fit_predict(voxel_depth_data)

# Get unique labels from clustering result
unique_labels = np.unique(labels)

# Iterate through each unique label and fit a plane
for label in unique_labels:
    if label == -1:
        continue  # Skip noise points (label -1)

    # Get indices of points belonging to this cluster
    cluster_indices = np.where(labels == label)

    # Extract depth values of the cluster
    cluster_depth_values = voxel_depth_data[cluster_indices]

    # Convert back to original depth values
    cluster_depth_values = cluster_depth_values * voxel_size

    # Fit a plane to the cluster's depth values
    cluster_points = np.column_stack((cluster_indices[0], cluster_indices[1], cluster_depth_values))
    plane_model = np.linalg.lstsq(cluster_points[:, :2], cluster_points[:, 2], rcond=None)[0]
    
    a, b = plane_model
    c = -1  # Assuming plane equation of the form z = ax + by + c
    d = 0   # Distance from the origin (not computed here)

    print(f"Equation of plane for cluster {label}: {a}*x + {b}*y + {c}*z + {d} = 0")
