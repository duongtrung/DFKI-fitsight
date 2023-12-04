import numpy as np
from trainer import findAngle
import requests
import json

# Define the URL to which you want to send the POST request
url = 'https://impect.milki-psy.dbis.rwth-aachen.de/client/6167/evaluate'  




#...................................BICEP CURL.................................................................

def bicep_findAngle(img, kpts, fw, fh, drawskeleton): 
    
    angleLH = findAngle(img, kpts, 5, 7, 9, draw=drawskeleton)
    angleRH = findAngle(img, kpts, 6, 8, 10, draw=drawskeleton)
    angleLL = findAngle(img, kpts, 11, 13, 15, draw=drawskeleton)
    angleRL = findAngle(img, kpts, 12, 14, 16, draw=drawskeleton)

    print(angleLH, angleRH, angleLL, angleRL)
    
    percentages = [np.interp(angleLH, (30, 178), (100, 0)), np.interp(angleRH, (182, 327), (0, 100)), np.interp(angleLL, (90, 180), (0, 100)), np.interp(angleRL, (90, 180), (0, 100)) ]
    percentage = sum(percentages) / len(percentages) 
    percentage = np.interp(percentage, (50, 100), (0, 100))
    print(percentage)

    bars = [np.interp(angleLH, (30, 178), (200, fh-100)), np.interp(angleRH, (182, 327), (fh-100, 200)), np.interp(angleLL, (90, 180), (fh-100, 200)), np.interp(angleRL, (90, 180), (fh-100, 200)) ]
    bar = sum(bars) / len(bars)
    bar = np.interp(bar, (200, 400), (200, fh-100))
    print(bar)
    return angleLH, angleRH, angleLL, angleRL,  percentage, bar

def bicep_feedback(min_angleLH, min_angleRH , min_angleLL, min_angleRL, max_angleLH, max_angleRH, max_angleLL, max_angleRL, max_percentage, recommendation):
    feedback = ""
    url = 'https://impect.milki-psy.dbis.rwth-aachen.de/client/2140/evaluate' 
    if max_percentage <= 90:

        if min_angleLH >= 70: 
            feedback += "Your Left hand needs to be fixed \n" if recommendation else "" 
            
            data = {
                'evaluation': 'mistake1',
            }
            response = requests.post(url, json=data)
            if response.status_code == 200:
                print('POST request successful!')
                print(response.text)  
            else:
                print('POST request failed with status code:', response.status_code)

        if max_angleRH <= 255:    
            feedback += "Your Right hand needs to be fixed \n" if recommendation else ""
            data = {
                'evaluation': 'mistake2',
            }
            response = requests.post(url, json=data)
        if max_angleLL >= 190:   
            feedback += "Your Left Leg needs to be fixed \n" if recommendation else ""
            data = {
                'evaluation': 'mistake3',
            }
            response = requests.post(url, json=data)
        if max_angleRL <= 175:   
            feedback += "Your Right Leg needs to be fixed \n" if recommendation else ""
            data = {
                'evaluation': 'mistake4',
            }
            response = requests.post(url, json=data)

    else:
        feedback = "Great work! Keep going" if recommendation else ""
        data = {
                'evaluation': 'mistake5',
        }
        response = requests.post(url, json=data)


    return feedback

#......................................................................LUNGES...........................................................................................................

def lunges_findAngle(img, kpts, fw, fh, drawskeleton): 
    
    angleLH = findAngle(img, kpts, 5, 7, 9, draw=drawskeleton)
    angleRH = findAngle(img, kpts, 6, 8, 10, draw=drawskeleton)
    angleLL = findAngle(img, kpts, 11, 13, 15, draw=drawskeleton)
    angleRL = findAngle(img, kpts, 12, 14, 16, draw=drawskeleton)

    print(angleLH, angleRH, angleLL, angleRL)
    
    percentages = [np.interp(angleLH, (90, 180), (0, 100)), np.interp(angleRH, (90, 180), (0, 100)), np.interp(angleLL, (166, 65), (0, 100)), np.interp(angleRL, (163, 75), (0, 100)) ]
    percentage = sum(percentages) / len(percentages) 
    percentage = np.interp(percentage, (50, 100), (0, 100))
    print(percentage)

    bars = [np.interp(angleLH, (90, 180), (fh-100, 200)), np.interp(angleRH, (90, 180), (fh-100, 200)), np.interp(angleLL, (166, 65), (fh-100, 200)), np.interp(angleRL, (163, 75), (fh-100, 200)) ]
    bar = sum(bars) / len(bars)
    bar = np.interp(bar, (200, 400), (200, fh-100))
    print(bar)
    return angleLH, angleRH, angleLL, angleRL,  percentage, bar

def lunges_feedback(min_angleLH, min_angleRH , min_angleLL, min_angleRL, max_angleLH, max_angleRH, max_angleLL, max_angleRL, max_percentage, recommendation):
    feedback = ""
    if max_percentage <= 90:

        if min_angleLH >= 70: 
            feedback += "Your Left hand needs to be fixed \n" if recommendation else "" 

        if max_angleRH <= 255:    
            feedback += "Your Right hand needs to be fixed \n" if recommendation else ""
            
        if max_angleLL >= 190:   
            feedback += "Your Left Leg needs to be fixed \n" if recommendation else ""
            
        if max_angleRL <= 175:   
            feedback += "Your Right Leg needs to be fixed \n" if recommendation else ""
            
    else:
        feedback = "Great work! Keep going" if recommendation else ""
        
    return feedback

#.............................................PUSHUP..........................................................

def pushup_findAngle(img, kpts, fw, fh, drawskeleton): 
    angle = findAngle(img, kpts, 5, 7, 9, draw=drawskeleton)
    angle1 = findAngle(img, kpts, 6, 8, 10, draw=drawskeleton)
    percentage = np.interp(angle, (210, 280), (0, 100))
    bar = np.interp(angle, (220, 280), (fh-100, 100)) 
    return angle, percentage, bar

def pushup_feedback(max_percentage, recommendation):
    if max_percentage <= 75:
        feedback = "Go down, Engage your Lats" if recommendation else ""
    elif max_percentage <= 90:
        feedback = "Almost There, Lock your lats" if recommendation else ""
    else:
        feedback = "Great work! Keep going" if recommendation else ""  
    return feedback       

#...........................................SHOULDER_LATERAL_RAISE.................................................

def shoulder_lateral_raise_findAngle(img, kpts, fw, fh, drawskeleton): 
    angle = findAngle(img, kpts, 6, 8, 10, draw=drawskeleton)
    angle1 = findAngle(img, kpts, 5, 7, 9, draw=drawskeleton)
    percentage = np.interp(angle, (171, 194), (0, 100))
    bar = np.interp(angle, (171, 194), (fh-100, 100)) 
    return angle, percentage, bar

def shoulder_lateral_raise_feedback(max_percentage, recommendation):
    if max_percentage <= 75:
        feedback = "Lift your arms more up!" if recommendation else ""
    elif max_percentage <= 90:
        feedback = "Almost There!" if recommendation else ""
    else:
        feedback = "Great work! Keep going" if recommendation else ""
    return feedback

#....................................................SQUATS..................................................................

def squats_findAngle(img, kpts, fw, fh, drawskeleton):  
    angle = findAngle(img, kpts, 11, 13, 15, draw=drawskeleton)
    angle1 = findAngle(img, kpts, 12, 14, 16, draw=drawskeleton)
    percentage = np.interp(angle, (210, 280), (0, 100))
    bar = np.interp(angle, (220, 280), (fh-100, 100)) 
    return angle, percentage, bar

def squats_feedback(max_percentage, recommendation):
    if max_percentage <= 75:
        feedback = "Pull ypur arms more closer" if recommendation else ""
    elif max_percentage <= 90:
        feedback = "Almost There!" if recommendation else ""
    else:
        feedback = "Great work! Keep going" if recommendation else ""  
    return feedback      