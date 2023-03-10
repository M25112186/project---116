import cv2
img = cv2.imread("p116/solar.jpg")
#Sun Text
cv2.putText(img,
            "Sun",
            (20, 300),
            fontFace = cv2.FONT_HERSHEY_COMPLEX,
            fontScale= 2,
            color = (255, 255, 255)
            )
#Mercury
cv2.putText(img,
            "Mercury",
            (110, 180), #68=right 200=height
            fontFace = cv2.FONT_HERSHEY_COMPLEX,
            fontScale= 0.5,
            color = (255, 255, 255)
            )
#Venus
cv2.putText(img,
            "Venus",
            (191, 262), #68=right 200=height
            fontFace = cv2.FONT_HERSHEY_COMPLEX,
            fontScale= 0.5,
            color = (255, 255, 255)
            )
#Earth
cv2.putText(img,
            "Earth",
            (280, 170), #68=right 200=height
            fontFace = cv2.FONT_HERSHEY_COMPLEX,
            fontScale= 0.5,
            color = (255, 255, 255)
            )
#Mars
cv2.putText(img,
            "Mars",
            (380, 262), #68=right 200=height
            fontFace = cv2.FONT_HERSHEY_COMPLEX,
            fontScale= 0.5,
            color = (255, 255, 255)
            )
#Jupiter
cv2.putText(img,
            "Jupiter",
            (570, 50), #68=right 200=height
            fontFace = cv2.FONT_HERSHEY_COMPLEX,
            fontScale= 0.5,
            color = (255, 255, 255)
            )
#Saturn
cv2.putText(img,
            "Saturn",
            (745, 300), #68=right 200=height
            fontFace = cv2.FONT_HERSHEY_COMPLEX,
            fontScale= 0.5,
            color = (255, 255, 255)
            )
#Uranus
cv2.putText(img,
            "Uranus",
            (962, 130), #68=right 200=height
            fontFace = cv2.FONT_HERSHEY_COMPLEX,
            fontScale= 0.5,
            color = (255, 255, 255)
            )
#Neptune
cv2.putText(img,
            "Neptune",
            (1112, 290), #68=right 200=height
            fontFace = cv2.FONT_HERSHEY_COMPLEX,
            fontScale= 0.5,
            color = (255, 255, 255)
            )



cv2.imwrite("SolarSystem.jpg", img)
cv2.imshow("output", img)
cv2.waitKey(0)