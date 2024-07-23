import cv2
import mediapipe as mp
import time
import math


def calculate_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

#this is to see if line 6-7-8 is straight (30degree allowed)
def calculate_angle(point1, point2, point3):
    # Calculate the angle between three points
    a = (point1[0] - point2[0], point1[1] - point2[1])
    b = (point3[0] - point2[0], point3[1] - point2[1])

    dot_product = a[0] * b[0] + a[1] * b[1]
    magnitude_a = math.sqrt(a[0] ** 2 + a[1] ** 2)
    magnitude_b = math.sqrt(b[0] ** 2 + b[1] ** 2)

    if magnitude_a == 0 or magnitude_b == 0:
        return 0

    # Clamp the value to the range [-1, 1] to avoid domain errors in acos
    cos_angle = dot_product / (magnitude_a * magnitude_b)
    cos_angle = max(-1.0, min(1.0, cos_angle))

    angle = math.acos(cos_angle)
    angle = math.degrees(angle)

    return angle




def pixelDistance():
    p1 = handLms.landmark[4]
    p2 = handLms.landmark[8]

    point1 = (int(p1.x * w), int(p1.y * h))
    point2 = (int(p2.x * w), int(p2.y * h))

    distance = calculate_distance(point1, point2)
    print(f"Distance between landmark 4 and 8: {distance:.2f} pixels")
    cv2.putText(img, f"{distance:.2f}", (point1[0] - 50, point1[1] - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.line(img, point1, point2, ((0, 0, 255)), 2)

def straightLine():
    lm6 = handLms.landmark[6]
    lm7 = handLms.landmark[7]
    lm8 = handLms.landmark[8]

    point6 = (int(lm6.x * w), int(lm6.y * h))
    point7 = (int(lm7.x * w), int(lm7.y * h))
    point8 = (int(lm8.x * w), int(lm8.y * h))

    # Calculate the angle
    angle = calculate_angle(point6, point7, point8)
    print(f"Angle between landmarks 6, 7, and 8: {angle:.2f} degrees")
    cv2.line(img, point6, point7, (0, 255, 0), 2)
    cv2.line(img, point7, point8, (0, 255, 0), 2)

    # check if angle is less than 10 then straught line
    if abs(angle - 180) <= 10:
        cv2.putText(img, "Straight Line", (10, 100), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    else:
        cv2.putText(img, "Not Straight Line", (10, 100), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

  #cv2.putText(img, "129="+str(distance129), (10, 250), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    #cv2.putText(img, "109="+str(distance109), (10, 300), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)








def fingers():

    if indexUp() and middleUp() and ringUp() and pinkyUp() and thumbUp():
        cv2.putText(img, "number shown: 5", (10, 70), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 0), 3)
    elif indexUp() and middleUp() and ringUp() and pinkyUp():
        cv2.putText(img, "number shown: 4", (10, 70), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 0), 3)
    elif indexUp() and middleUp() and ringUp() and not pinkyUp():
        cv2.putText(img, "number shown: 3", (10, 70), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 0), 3)
    elif indexUp() and middleUp() and not ringUp() and not pinkyUp():
        cv2.putText(img, "number shown: 2", (10, 70), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 0), 3)
    elif indexUp() and not middleUp() and not ringUp() and not pinkyUp():
        cv2.putText(img, "number shown: 1", (10, 70), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 0), 3)
    else:
        cv2.putText(img, "ZERO/unrecognised", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 2)




"""
def middleDown():
    # middle

    p12 = handLms.landmark[12]
    p9 = handLms.landmark[9]
    point12 = (int(p12.x * w), int(p12.y * h))
    point9 = (int(p9.x * w), int(p9.y * h))
    distance129 = calculate_distance(point9, point12)

    p10 = handLms.landmark[10]
    p9 = handLms.landmark[9]
    point10 = (int(p10.x * w), int(p10.y * h))
    point9 = (int(p9.x * w), int(p9.y * h))
    distance109 = calculate_distance(point9, point10)
    checkmd=distance129/distance109
    cv2.putText(img, "checkmd=" + str(checkmd), (10, 300), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
"""
def indexUp():
    #if index is up
    p8 = handLms.landmark[8]
    p7 = handLms.landmark[7]
    p6 = handLms.landmark[6]
    p5 = handLms.landmark[5]

    point8 = (int(p8.x * w), int(p8.y * h))
    point7 = (int(p7.x * w), int(p7.y * h))
    point6 = (int(p6.x * w), int(p6.y * h))
    point5 = (int(p5.x * w), int(p5.y * h))

    distance87 = calculate_distance(point8, point7)
    distance76 = calculate_distance(point7, point6)
    distance65 = calculate_distance(point6, point5)
    distance58 = calculate_distance(point5, point8)
    checkiu = (distance76 / distance87) + (distance65 / distance76)



    # Calculate the angle
    angle = calculate_angle(point5, point6, point8)






    #if other fingers down



    if 2.65 < checkiu < 2.95 and abs(angle - 180) <= 30:
        cv2.putText(img, "1", (10, 200), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

        return True


def middleUp():
    # if index is up
    p12 = handLms.landmark[12]
    p11 = handLms.landmark[11]
    p10 = handLms.landmark[10]
    p9 = handLms.landmark[9]

    point12 = (int(p12.x * w), int(p12.y * h))
    point11 = (int(p11.x * w), int(p11.y * h))
    point10 = (int(p10.x * w), int(p10.y * h))
    point9 = (int(p9.x * w), int(p9.y * h))

    distance1211 = calculate_distance(point12, point11)
    distance1110 = calculate_distance(point11, point10)
    distance109 = calculate_distance(point10, point9)
    checkmu = (distance1110 / distance1211) + (distance109 / distance1110)

    angle = calculate_angle(point12, point10, point9)

   # cv2.putText(img, str(checkmu), (10, 250), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    # if other fingers down
    if 2.58 < checkmu < 3.1 and abs(angle - 180) <= 30:
        cv2.putText(img, "2", (10, 250), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

        return True




def ringUp():
    #if index is up
    p16 = handLms.landmark[16]
    p15 = handLms.landmark[15]
    p14 = handLms.landmark[14]
    p13 = handLms.landmark[13]

    point16 = (int(p16.x * w), int(p16.y * h))
    point15 = (int(p15.x * w), int(p15.y * h))
    point14 = (int(p14.x * w), int(p14.y * h))
    point13 = (int(p13.x * w), int(p13.y * h))

    distance1615 = calculate_distance(point16, point15)
    distance1514 = calculate_distance(point15, point14)
    distance1413 = calculate_distance(point14, point13)

    checkru = (distance1514 / distance1615) + (distance1413 / distance1514)



    # Calculate the angle
    angle = calculate_angle(point13, point14, point16)






    #if other fingers down

    #cv2.putText(img, str(checkru), (10, 300), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    if 2.35 < checkru < 2.85 and abs(angle - 180) <= 20:
        cv2.putText(img, "3", (10, 300), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

        return True


def pinkyUp():
    # if index is up
    p20 = handLms.landmark[20]
    p19 = handLms.landmark[19]
    p18 = handLms.landmark[18]
    p17 = handLms.landmark[17]

    point20 = (int(p20.x * w), int(p20.y * h))
    point19 = (int(p19.x * w), int(p19.y * h))
    point18 = (int(p18.x * w), int(p18.y * h))
    point17 = (int(p17.x * w), int(p17.y * h))

    distance2019 = calculate_distance(point20, point19)
    distance1918 = calculate_distance(point19, point18)
    distance1817 = calculate_distance(point18, point17)

    checkpu = (distance1918 / distance2019) + (distance1817 / distance1918)

    # Calculate the angle
    angle = calculate_angle(point17, point18, point20)

    # if other fingers down
    #cv2.putText(img, str(checkpu), (10, 350), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    if 2.35 < checkpu < 2.75 and abs(angle - 180) <= 25:
        cv2.putText(img, "4", (10, 350), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

        return True


def thumbUp():
    # if index is up
    p4 = handLms.landmark[4]
    p3 = handLms.landmark[3]
    p2 = handLms.landmark[2]
    p13 = handLms.landmark[13]

    point4 = (int(p4.x * w), int(p4.y * h))
    point3 = (int(p3.x * w), int(p3.y * h))
    point2 = (int(p2.x * w), int(p2.y * h))
    point13 = (int(p13.x * w), int(p13.y * h))

    distance42 = calculate_distance(point4, point2)

    distance413 = calculate_distance(point4, point13)

    checktu = distance42/distance413

    # Calculate the angle
    angle = calculate_angle(point2, point3, point4)

    # if other fingers down
    #cv2.putText(img, str(checktu)+"----"+str(angle), (10, 450), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    if checktu < 1.0 and abs(angle) >= 90:
        cv2.putText(img, "5", (10, 400), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

        return True




cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    cv2.putText(img, "Made by dm", (10, 450), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 2)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                #print(id, cx, cy)
                # if id == 4:
                cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                #cv2.p
                cv2.putText(img, str(id), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

            # this is for mapping all landmarks acc to mediapipe
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)



            #this is for pixel distance




            #this is for straight line
            fingers()

            #trial for distance


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

   # cv2.putText(img, "fps: "+str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 2,
     #           (255, 0, 255), 2)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.waitKey(1)