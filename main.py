import cv2

#Read an Image~~~~

# images = cv2.imread('Images/smarties.png', -1) #reads File, also accepts arguments (Flags) (1, 0, -1) 0 == Grayscale Version, 1 is Colored -1 includes alpha channel (load image as it is)
#
# print(images) # prints img Matrix value, also checks if image path is correct
#
# cv2.imshow('ImageWindow', images)# displays Image, arguments("Window Name", "Image Variable") displays only 1 millisecond
#
#
#
# k = cv2.waitKey(0)#keyboard binding function to wait for it to close, in milisecond, 0 for it to permanently be open unless closed
#
# if k == 27: # 27 == escape key will close
#     cv2.destroyAllWindows()#destroy a window or close
#
# elif k == ord('j'): #ord is a built-in function that accepts an argument that we will click
#     cv2.imwrite('Candy.png', images)#use to write an image in the form of a file ("Image Name", variable)
#     cv2.destroyAllWindows()



#Video ~~~

cap = cv2.VideoCapture(0)# arguments accept filename or cam index 0 ("video.png") or(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4', fourcc, 30,(640,480))#saves the video
while(cap.isOpened()):# will return false if cap is not opened or not found

    ret,frame = cap.read()#read returns true if frame is available to Frame and rue to ret
    if ret == True:# checks if ret is true then proceeds down
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #print both width and heigh of frames
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)#instantiate video writer for saving

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # grayscale the image
        cv2.imshow('Frame', gray)#hows the fraeme to window

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release() # important since we have to release after reading
out.release() #release resources for video writer.
cv2.destroyAllWindows()