import cv2

# Read Image
img = cv2.imread("butterfly.jpg")

# Display Colored Image
cv2.imshow("Display Image",img)

# Convert Colored Image To Grayscale
print(img)
cv2.waitKey(100000)
