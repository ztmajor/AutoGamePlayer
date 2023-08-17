import cv2

img_path = "./game_area.jpg"

img = cv2.imread(img_path)

top_left = (100, 100)
w = 50
h = 50
bottom_right = (top_left[0] + w, top_left[1] + h)
print(top_left, bottom_right)
img = cv2.rectangle(img, top_left, bottom_right, 0, 8)

# Display the image
cv2.imshow("Image", img)
 
# Wait for the user to press a key
cv2.waitKey(0)
 
# Close all windows
cv2.destroyAllWindows()