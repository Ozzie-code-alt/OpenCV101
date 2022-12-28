import cv2
import numpy as np
import datetime

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





# #Video ~~~

# cap = cv2.VideoCapture(0)# arguments accept filename or cam index 0 ("video.png") or(0)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.mp4', fourcc, 30,(640,480))#saves the video
# while(cap.isOpened()):# will return false if cap is not opened or not found
#
#     ret,frame = cap.read()#read returns true if frame is available to Frame and true to ret
#     if ret == True:# checks if ret is true then proceeds down
#         print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #print both width and heigh of frames
#         print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#
#         out.write(frame)#instantiate video writer for saving
#
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # grayscale the image
#         cv2.imshow('Frame', gray)#hows the fraeme to window
#
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break
# cap.release() # important since we have to release after reading
# out.release() #release resources for video writer...
# cv2.destroyAllWindows()




# # Drawing Geometric Shapes on Images
#
# # img = cv2.imread('Images/lena.jpg',1)
# img = np.zeros([512,512,3],np.uint8) # using numpy as image with black background
#
# img = cv2.line(img,(0,0),(255,255),(0,255,0),5)# create a line in the image, argumen pt1 == start pt2 == end
# img = cv2.arrowedLine(img,(0,255),(255,255),(0,0,255),5)
# img = cv2.rectangle(img,(384,0),(510,128),(255,0,0),2) #arguments pt1 == top left coordinates && pt2 == lower right , -1 will fill shape with color
# img = cv2.circle(img,(447,63),63,(0,255,0),-1)
# font = cv2.FONT_ITALIC
# img = cv2.putText(img, 'OpenCV',(10,500),font,4,(255,255,100),2,cv2.LINE_AA)# Puts text on an Image , 3rd argument is the coordinates
# cv2.imshow('Lena Picture', img)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()






# # setting camera parameters

# cap = cv2.VideoCapture(0)
# print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # width of frame
# print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # height of frame
#
# cap.set(3, 3000)# arguments (number of property , value)
# cap.set(4, 3000)
# # Note this sets the resolution only available for the camera
# # will only return MAX resolution of cam
# print(cap.get(3))
# print(cap.get(4))
# while(cap.isOpened()):
#     ret, frame = cap.read() # returns true if there are frames
#     if ret == True:
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         cv2.imshow('setting cam parameters', gray)# display
#
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
#     else:
#         break
#
# cap.release()
# cv2.destroyAllWindows()


# Showing Date time on videos

# cap = cv2.VideoCapture(0)
#
# cap.get(cv2.CAP_PROP_FRAME_WIDTH)
# cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
#
# cap.set(3,3000)
# cap.set(4,3000)
#
# print(cap.get(3))
# print(cap.get(4))
#
# while(cap.isOpened()):
#     ret,frame= cap.read()
#
#     if ret == True:
#
#         font = cv2.FONT_HERSHEY_SIMPLEX # in using text , instantiate font first
#         text = "Width: " + str(cap.get(3)) + " Height: " + str(cap.get(4))
#         date = str(datetime.datetime.now())
#         frame = cv2.putText(frame,text,(10,50), font, 1, (0,255,0), 2, cv2.LINE_AA )
#         frame = cv2.putText(frame, date, (700, 50), font, 1, (255, 255, 0), 2, cv2.LINE_AA)# adding date text in video screen
#         cv2.imshow("Showing Date Time", frame )
#
#         if cv2.waitKey(1) & 0xFF == ord ("q"):
#             break
#
#     else:
#         break
#
# cap.release()
# cv2.destroyAllWindows()


#Mouse events on OpenCV

# events = [i for i in dir(cv2) if 'EVENT'in i]#shows all the built in methods in CV2
# print(events)

# def click_event (event, x,y, flags, param): # specific format for mouse event functions
#     if event == cv2.EVENT_LBUTTONDOWN:# if left mouse button is clicked
#         print(x,', ' ,y) # this prints the x and y Axis in console
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         str1= str(x) + ', ' +  str(y)  # container for x and y values
#         cv2.putText(img, str1, (x, y), font, 1, (0, 255, 255), 2)
#         cv2.imshow('LeftClick', img)
#     if event == cv2.EVENT_RBUTTONDOWN: #onlcick that will check what color
#         blue = img[y, x, 0]
#         green = img[y, x, 1]
#         red = img[y, x, 2]
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         bgr = str(blue) + ', ' + str(green) + ',' + str(red)  # container for x and y values
#         cv2.putText(img, bgr, (x, y), font, 1, (255, 255, 0), 2)
#         cv2.imshow('LeftClick', img)
#
# # img = np.zeros((512,512,3), np.uint8)
# img = cv2.imread('Images/lena.jpg')
# cv2.imshow('LeftClick', img)
# cv2.setMouseCallback('LeftClick', click_event)#used to call the click_event function
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#More Mouse Events (Lines and Points Specifically)
#
# def click_event (event, x,y, flags, param): # specific format for mouse event functions
#     if event == cv2.EVENT_LBUTTONDOWN:# if left mouse button is clicked
#         cv2.circle(img, (x, y), 3, (0,255,0), -1) # circle coordinates, remember -1 fills the color
#         points.append((x, y))# saving the point on which the mouse is clicked in the form of an array
#         if len(points) >= 2:
#             cv2.line(img,points[-1],points[-2],(255, 0, 255), 5 )# last 2 elements in the array
#         cv2.imshow('LeftClick', img)
#         print(points)
#
# # img = np.zeros((512,512,3), np.uint8)
# img = cv2.imread('Images/lena.jpg')
# cv2.imshow('LeftClick', img)
# points = []#empty array
# print(points)
# cv2.setMouseCallback('LeftClick', click_event)#used to call the click_event function
# cv2.waitKey(0)
# cv2.destroyAllWindows()


