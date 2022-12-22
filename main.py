import cv2


images = cv2.imread('Images/smarties.png', -1) #reads File, also accepts arguments (Flags) (1, 0, -1) 0 == Grayscale Version, 1 is Colored -1 includes alpha channel (load image as it is)

print(images) # prints img Matrix value, also checks if image path is correct

cv2.imshow('ImageWindow', images)# displays Image, arguments("Window Name", "Image Variable") displays only 1 millisecond



k = cv2.waitKey(0)#keyboard binding function to wait for it to close, in milisecond, 0 for it to permanently be open unless closed

if k == 27: # 27 == escape key will close
    cv2.destroyAllWindows()#destroy a window or close

elif k == ord('j'): #ord is a built in function that accepts an argument that we will click
    cv2.imwrite('Candy.png', images)#use to write an image in the form of a file ("Image Name", variable)
    cv2.destroyAllWindows()