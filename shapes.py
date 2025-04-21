#    Different Shapes

# --- Drawing a line ---

#import cv2

#img = cv2.imread("img.png")

#start = (500,100)
#end = (1200,100)
#colour = (255,0,0)
#thickness = 10

#img2 = cv2.line(img,start,end,colour,thickness)

#cv2.imshow("Original",img)
#cv2.imshow("line",img2)
#cv2.waitKey(0)
#cv2.destroyAllWindows

# --- Drawing a square ---

#import cv2

#img = cv2.imread("img.png")

#start = (500,500)
#end = (1000,1000)
#colour = (255,0,0)
#thickness = 10

# -1 thickness = filled

#img = cv2.rectangle(img,start,end,colour,thickness)

#cv2.imshow("square",img)
#cv2.waitKey(0)
#cv2.destroyAllWindows

# --- Drawing a square ---

#import cv2

#img = cv2.imread("img.png")

#center = (800,700)
#radius = 500
#colour = (0,0,0)
#thickness = 10

# -1 thickness = filled

#img = cv2.circle(img, center,radius,colour,thickness)

#cv2.imshow("cricle",img)
#cv2.waitKey(0)
#cv2.destroyAllWindows

# --- Writing a text ---

import cv2

img = cv2.imread("img.png")

font = cv2.FONT_ITALIC
orgin = (0,100)
scale = 2
colour = (0,0,0)
thickness = 10

img = cv2.putText(img," A Big Orange Coat ",orgin,font,scale,colour,thickness,cv2.LINE_AA)

cv2.imshow("Text",img)
cv2.waitKey(0)
cv2.destroyAllWindows


