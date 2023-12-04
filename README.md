# FITSIGHT: A Computer Vision-Based Approach for Performance Analysis, Error Classification and Feedback in Gym Exercises 🏋️‍♂️

## Authors
- **Hitesh Kotte**
- **Nghia Duong-Trung**
- **Milos Kravcik**

### Login Credentials 🗝️

- **Username:** `admin`
- **Password:** `admin`

### Login Page Preview 🚪
<img src="https://github.com/hiteshkotte/DFKI-fitsight/assets/35593884/b34dc785-0b50-4bf8-86c5-cefe984ebba4" width="350">

### Main Page 🖥️
<img src="https://github.com/hiteshkotte/DFKI-fitsight/assets/35593884/5f795e99-be9e-48a1-9fdc-2b950b76a724" width="350">


### Demo 🏋️‍♂️
https://github.com/hiteshkotte/MILeS_2023/assets/35593884/7835485c-a494-40b1-826d-0bdde969e541" width


Create Virtual environment and activate the Virtual environment.

1. Create a virtual environment (Install this preferrably on Anaconda Prompt. 
This will create a empty virtual environment.

		conda create -n fitsight

3. To activate the virtual environment:

		conda activate fitsight

4. If you are using Anaconda Powershell, To install ffmpeg
		conda install -c conda-forge ffmpeg

Otherwise zou can add the ffmpeg/bin folder to your system variables
		setx /M PATH "%PATH%;C:\Users\hiko01-admin\Desktop\fitsight\ffmpeg-master-latest-win64-gpl\bin"
		for all users

		setx PATH "%PATH%;C:\Users\hiko01-admin\Desktop\fitsight\ffmpeg-master-latest-win64-gpl\bin"
		for specific users



---------------------------------------------------------------------------------------------------------------------------------------------
Scripts :

app.py - Python flask application that needs to run on a web server to handle the website communication with the YOLO model.

index.html - Html file to manage the website webpage and handle UI. (This can be found inside the "Templates" folder)


----------------------------------------------------------------------------------------------------------------------------------------------
How to run:

We are using publicly available yolov7 model from github repo: https://github.com/WongKinYiu/yolov7.git

1. Install the necessary dependencies
   
		pip install -r requirements.txt
	
3. Click on [`yolov7-w6-pose.pt`](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-w6-pose.pt) to get the pre trained model weights pytorch file and place it the yolov7 directory.

4. Run the python app.py to run the website on local server.
   
   		python app.py


-----------------------------------------------------------------------------------------------------------------------------------------------
For Input videos of exercises, Please download from the below google drive link.

	https://drive.google.com/drive/folders/10dz-wZCnio7Sub48rYiIDp3Gb_mW_Fq-?usp=sharing





