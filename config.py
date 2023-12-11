import numpy as np
from trainer import findAngle
import requests
import json

# Define the URL to which you want to send the POST request
url = 'https://impect.milki-psy.dbis.rwth-aachen.de/client/6167/evaluate'  




#...................................BICEP CURL.................................................................

#def bicep_findAngle(img, kpts, fw, fh, drawskeleton): 
    
#    angleLH = findAngle(img, kpts, 5, 7, 9, draw=drawskeleton)
#    angleRH = findAngle(img, kpts, 6, 8, 10, draw=drawskeleton)
#    angleLL = findAngle(img, kpts, 11, 13, 15, draw=drawskeleton)
#    angleRL = findAngle(img, kpts, 12, 14, 16, draw=drawskeleton)

#    print(angleLH, angleRH, angleLL, angleRL)
    
#    percentages = [np.interp(angleLH, (30, 178), (100, 0)), np.interp(angleRH, (182, 327), (0, 100)), np.interp(angleLL, (90, 180), (0, 100)), np.interp(angleRL, (90, 180), (0, 100)) ]
#    percentage = sum(percentages) / len(percentages) 
#    percentage = np.interp(percentage, (50, 100), (0, 100))
#    print(percentage)

#    bars = [np.interp(angleLH, (30, 178), (200, fh-100)), np.interp(angleRH, (182, 327), (fh-100, 200)), np.interp(angleLL, (90, 180), (fh-100, 200)), np.interp(angleRL, (90, 180), (fh-100, 200)) ]
#    bar = sum(bars) / len(bars)
#    bar = np.interp(bar, (200, 400), (200, fh-100))
#    print(bar)
#    return angleLH, angleRH, angleLL, angleRL,  percentage, bar

#def bicep_feedback(min_angleLH, min_angleRH , min_angleLL, min_angleRL, max_angleLH, max_angleRH, max_angleLL, max_angleRL, max_percentage, recommendation):
#    feedback = ""
#    url = 'https://impect.milki-psy.dbis.rwth-aachen.de/client/2140/evaluate' 
#    if max_percentage <= 90:

#        if min_angleLH >= 70: 
#            feedback += "Your Left hand needs to be fixed \n" if recommendation else "" 
            
#            data = {
#                'evaluation': 'mistake1',
#            }
#            response = requests.post(url, json=data)
#            if response.status_code == 200:
#                print('POST request successful!')
#                print(response.text)  
#            else:
#                print('POST request failed with status code:', response.status_code)

#        if max_angleRH <= 255:    
#            feedback += "Your Right hand needs to be fixed \n" if recommendation else ""
#            data = {
#                'evaluation': 'mistake2',
#            }
#            response = requests.post(url, json=data)
#        if max_angleLL >= 190:   
#            feedback += "Your Left Leg needs to be fixed \n" if recommendation else ""
#            data = {
#                'evaluation': 'mistake3',
#            }
#            response = requests.post(url, json=data)
#        if max_angleRL <= 175:   
#            feedback += "Your Right Leg needs to be fixed \n" if recommendation else ""
#            data = {
#                'evaluation': 'mistake4',
#            }
#            response = requests.post(url, json=data)

#    else:
#        feedback = "Great work! Keep going" if recommendation else ""
#        data = {
#                'evaluation': 'mistake5',
#        }
#        response = requests.post(url, json=data)


#    return feedback


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







#......................................................................LUNGES...........................................................................................................

def lunges_findAngle(img, kpts, fw, fh, drawskeleton):
    # Angle calculation for lunges
    angleLH = findAngle(img, kpts, 5, 7, 9, draw=drawskeleton)  # Left hand
    angleRH = findAngle(img, kpts, 6, 8, 10, draw=drawskeleton)  # Right hand
    angleLL = findAngle(img, kpts, 11, 13, 15, draw=drawskeleton)  # Left leg
    angleRL = findAngle(img, kpts, 12, 14, 16, draw=drawskeleton)  # Right leg

    print(angleLH, angleRH, angleLL, angleRL)

    # Adjusting the interpolation values for lunges
    percentages = [
        np.interp(angleLH, (187, 190), (100, 0)),
        np.interp(angleRH, (204, 277), (100, 0)),
        np.interp(angleLL, (112, 158), (100, 0)),
        np.interp(angleRL, (56, 124), (100, 0))
    ]
    percentage = sum(percentages) / len(percentages) 
    percentage = np.interp(percentage, (50, 100), (0, 100))
    print(percentage)

    bars = [
        np.interp(angleLH, (187, 190), (fh-100, 200)),  # Reverse the range for correct mapping
        np.interp(angleRH, (204, 277), (fh-100, 200)),
        np.interp(angleLL, (112, 158), (fh-100, 200)),
        np.interp(angleRL, (56, 124), (fh-100, 200))
    ]
    bar = sum(bars) / len(bars)

    # Adjusting the final interpolation range
    # Ensure that 0% corresponds to the start position of the bar
    bar = np.interp(percentage, (0, 100), (fh-100, 200))

    print(bar)

    return angleLH, angleRH, angleLL, angleRL, percentage, bar


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
    # Angle calculation for pushups
    angleLH = findAngle(img, kpts, 5, 7, 9, draw=drawskeleton)  # Left hand
    angleRH = findAngle(img, kpts, 6, 8, 10, draw=drawskeleton)  # Right hand
    angleLL = findAngle(img, kpts, 11, 13, 15, draw=drawskeleton)  # Left leg
    angleRL = findAngle(img, kpts, 12, 14, 16, draw=drawskeleton)  # Right leg

    print(angleLH, angleRH, angleLL, angleRL)

    # Adjusting the interpolation values for pushups
    percentages = [
        np.interp(angleLH, (88, 218), (100, 0)),
        np.interp(angleRH, (1, 201), (100, 0)),
        np.interp(angleLL, (153, 156), (100, 0)),
        np.interp(angleRL, (148, 152), (100, 0))
    ]
    percentage = sum(percentages) / len(percentages) 
    percentage = np.interp(percentage, (50, 100), (0, 100))
    print(percentage)

    bars = [
        np.interp(angleLH, (88, 218), (200, fh-100)),
        np.interp(angleRH, (1, 201), (200, fh-100)),
        np.interp(angleLL, (153, 156), (200, fh-100)),
        np.interp(angleRL, (148, 152), (200, fh-100))
    ]
    bar = sum(bars) / len(bars)
    bar = np.interp(bar, (200, fh-100), (200, fh-100))
    print(bar)

    return angleLH, angleRH, angleLL, angleRL, percentage, bar

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
    
    angleLH = findAngle(img, kpts, 5, 7, 9, draw=drawskeleton)
    angleRH = findAngle(img, kpts, 6, 8, 10, draw=drawskeleton)
    angleLL = findAngle(img, kpts, 11, 13, 15, draw=drawskeleton)
    angleRL = findAngle(img, kpts, 12, 14, 16, draw=drawskeleton)

    print(angleLH, angleRH, angleLL, angleRL)
    
    percentages = [np.interp(angleLH, (170, 192), (100, 0)), np.interp(angleRH, (170, 192), (0, 100)), np.interp(angleLL, (90, 180), (0, 100)), np.interp(angleRL, (90, 180), (0, 100)) ]
    percentage = sum(percentages) / len(percentages) 
    percentage = np.interp(percentage, (50, 100), (0, 100))
    print(percentage)

    bars = [np.interp(angleLH, (170, 192), (200, fh-100)), np.interp(angleRH, (172, 192), (fh-100, 200)), np.interp(angleLL, (90, 180), (fh-100, 200)), np.interp(angleRL, (90, 180), (fh-100, 200)) ]
    bar = sum(bars) / len(bars)
    bar = np.interp(bar, (200, 400), (200, fh-100))
    print(bar)
    return angleLH, angleRH, angleLL, angleRL,  percentage, bar

def shoulder_lateral_raise_feedback(min_angleLH, min_angleRH , min_angleLL, min_angleRL, max_angleLH, max_angleRH, max_angleLL, max_angleRL, max_percentage, recommendation):
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


#....................................................SQUATS..................................................................

def squats_findAngle(img, kpts, fw, fh, drawskeleton): 
    angleLH = findAngle(img, kpts, 5, 7, 9, draw=drawskeleton)  # Left Hand
    angleRH = findAngle(img, kpts, 6, 8, 10, draw=drawskeleton)  # Right Hand
    angleLL = findAngle(img, kpts, 11, 13, 15, draw=drawskeleton)  # Left Leg
    angleRL = findAngle(img, kpts, 12, 14, 16, draw=drawskeleton)  # Right Leg

    print(angleLH, angleRH, angleLL, angleRL)
    
    # Interpolation for percentage and bar
    percentageLL = np.interp(angleLL, (182, 234), (0, 100))  # Adjusted range for left leg
    percentageRL = np.interp(angleRL, (127, 178), (100, 0))  # Adjusted range for right leg
    percentage = (percentageLL + percentageRL) / 2
    print(percentage)

    barLL = np.interp(angleLL, (182, 234), (fh-100, 200))  # Adjusted range for left leg
    barRL = np.interp(angleRL, (127, 178), (200, fh-100))  # Adjusted range for right leg
    bar = min(barLL, barRL)  # Using the lower bar value to represent squat depth
    print(bar)

    return angleLH, angleRH, angleLL, angleRL, percentage, bar

def squats_feedback(min_angleLH, min_angleRH, min_angleLL, min_angleRL, max_angleLH, max_angleRH, max_angleLL, max_angleRL, max_percentage, recommendation):
    feedback = ""
    
    if max_percentage <= 90:
       
        deep_squat_threshold_LL = 190  # Example threshold for left leg
        deep_squat_threshold_RL = 175  # Example threshold for right leg

        if max_angleLL >= deep_squat_threshold_LL or max_angleRL >= deep_squat_threshold_RL:
            feedback = "Try to squat deeper while maintaining balance and form." if recommendation else ""
        else:
            feedback = "Your squat depth is good. Keep up the good work!"

    else:
        feedback = "Great work! Keep going" if recommendation else ""
        
    return feedback



    


    