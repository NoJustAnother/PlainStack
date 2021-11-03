import glob
import numpy as np
import cv2


extention = input("Enter extention: ")
filename = input("Enter filename to be saved(with extention): ")

# Import all image files with the .<specified> extension
image_files = glob.glob ("*." + extention)
image_data = []
for selected_file in image_files:
    image_data.append(cv2.imread(selected_file, 1))
 
# Average image calculation
dst = image_data[0]
for i in range(len(image_data)):
    if i != 0:
        alpha = 1/(i + 1)
        dst = cv2.addWeighted(image_data[i], alpha, dst, 1-alpha, 0.0)
 
# Save final image
cv2.imwrite(filename, dst)
print("Saved!")
