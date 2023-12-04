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
https://github.com/hiteshkotte/MILeS_2023/assets/35593884/7835485c-a494-40b1-826d-0bdde969e541


# 🚀 How to Run

## Setting Up the Virtual Environment

### Prerequisites
- Ensure you have [Anaconda](https://www.anaconda.com/products/individual) installed to manage your environments and packages.

### Creating and Activating the Virtual Environment

1. **Create a Virtual Environment:**
   - Open Anaconda Prompt.
   - Run the following command to create a new virtual environment named `fitsight`:
     ```bash
     conda create -n fitsight
     ```

2. **Activate the Virtual Environment:**
   - Activate the `fitsight` environment by executing:
     ```bash
     conda activate fitsight
     ```

3. **Install Required Packages:**
   - Ensure that the `fitsight` environment is activated.
   - Install the required packages by running:
     ```bash
     pip install -r requirements.txt
     ```


4. **FFmpeg Installation:**
   FFmpeg is required for handling multimedia files.

   - **Using Anaconda Powershell:**
     - Run the following command to install FFmpeg:
       ```bash
       conda install -c conda-forge ffmpeg
       ```

   - **For Non-Anaconda Environments:**
     - Download and extract the FFmpeg build to a known directory (e.g., `C:\\Users\\your-username\\Desktop\\fitsight\\ffmpeg-master-latest-win64-gpl\\bin`).
     - Add FFmpeg to your system's PATH:
       - For all users:
         ```bash
         setx /M PATH "%PATH%;C:\\Users\\your-username\\Desktop\\fitsight\\ffmpeg-master-latest-win64-gpl\\bin"
         ```
       - For the current user:
         ```bash
         setx PATH "%PATH%;C:\\Users\\your-username\\Desktop\\fitsight\\ffmpeg-master-latest-win64-gpl\\bin"
         ```
     - Replace `your-username` with your actual Windows username.

### Installing Dependencies

#### FFmpeg Installation:
FFmpeg is required for handling multimedia files.

- **Using Anaconda Powershell:**
  - Run the following command to install FFmpeg:
    ```bash
    conda install -c conda-forge ffmpeg
    ```

- **For Non-Anaconda Environments:**
  - Download and extract the FFmpeg build to a known directory (e.g., `C:\\Users\\your-username\\Desktop\\fitsight\\ffmpeg-master-latest-win64-gpl\\bin`).
  - Add FFmpeg to your system's PATH:
    - For all users:
      ```bash
      setx /M PATH "%PATH%;C:\\Users\\your-username\\Desktop\\fitsight\\ffmpeg-master-latest-win64-gpl\\bin"
      ```
    - For the current user:
      ```bash
      setx PATH "%PATH%;C:\\Users\\your-username\\Desktop\\fitsight\\ffmpeg-master-latest-win64-gpl\\bin"
      ```
  - Replace `your-username` with your actual Windows username.

### Notes:
- Adjust the file paths according to where you've installed or extracted FFmpeg.
- Replace `your-username` with your actual Windows username in the file paths.
- Ensure to test these instructions in your environment to confirm they work as expected.

## Additional Project Information

(Here you can add other sections relevant to your project like 'Usage', 'Contributing', 'License', etc.)




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





