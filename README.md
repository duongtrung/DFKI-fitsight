# FITSIGHT: A Computer Vision-Based Approach for Performance Analysis, Error Classification and Feedback in Gym Exercises 🏋️‍♂️

## Authors
- **Hitesh Kotte**
- **Nghia Duong-Trung**
- **Milos Kravcik**



### Login Page Preview 🚪
<p align="left">
  <img src="https://github.com/hiteshkotte/DFKI-fitsight/assets/35593884/b34dc785-0b50-4bf8-86c5-cefe984ebba4" width="350">
</p>

### Main Page 🖥️
<p align="left">
  <img src="https://github.com/hiteshkotte/DFKI-fitsight/assets/35593884/5f795e99-be9e-48a1-9fdc-2b950b76a724" width="350">
</p>

### Demo 🏋️‍♂️
<p align="left">
  <a href="https://github.com/hiteshkotte/MILeS_2023/assets/35593884/7835485c-a494-40b1-826d-0bdde969e541">Demo Video</a>
</p>


# 🚀 How to Run

## Setting Up the Virtual Environment 🛠️

### Prerequisites 📋
- Ensure you have [Anaconda](https://www.anaconda.com/products/individual) installed to manage your environments and packages.
  
- Clone the project repository from GitHub. Run the following command in your terminal:
  ```bash
  git clone https://github.com/hiteshkotte/DFKI-fitsight.git

After cloning, extract the project files to your desired location. Ensure that you have sufficient permissions in the directory where you wish to extract the files.

### Creating and Activating the Virtual Environment 🌐

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
   - Change your current directory to the `DFKI-fitsight` folder, which is your working directory. Run the following command:
     ```bash
     cd path/to/your/downloads/DFKI-fitsight
     ```
   Replace `path/to/your/downloads/DFKI-fitsight` with the actual path where the `DFKI-fitsight` folder is located on your machine.
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
     - Download and extract the [FFmpeg](https://ffmpeg.org/download.html) build to the working directory.
       
     - Add the path of the extracted FFmpeg `bin` folder to your system's PATH:
	    - Locate the `bin` folder inside the extracted FFmpeg directory.
	    - Copy the full path to this `bin` folder.
	    - Add this path to your system's PATH:
	     
     - Add FFmpeg to your system's PATH:
       - For all users:
         ```bash
         setx /M PATH "%PATH%;your_path"
         ```
       - For the current user:
         ```bash
         setx PATH "%PATH%;your_path"
         ```
     - In this version, "your_path" should be replaced by the user with the actual path to the FFmpeg `bin` directory. The command updates the PATH environment variable, making FFmpeg accessible from anywhere in the command line interface.



5. **Run the Application:**
   - Start the application by running the following command in your terminal or command prompt:
     ```bash
     python app.py
     ```
   - Once the application is running, open your web browser.
   - Navigate to the local host address provided in the application's output. Typically, this will be `http://localhost:PORT`


6. **Accessing the Application in the Browser:**
   - When you open the application in the browser, it will prompt you for credentials.
   - Use the following 🗝️Login Credentials:
     - **Username:** admin
     - **Password:** admin

   This will grant you access to the application's features. 




## Additional Information

### Input Videos for Exercises

To access the input videos used for exercise analysis, please visit the following Google Drive link:

[Exercise Videos](https://drive.google.com/drive/folders/10dz-wZCnio7Sub48rYiIDp3Gb_mW_Fq-?usp=sharing)

These videos are essential for testing and demonstrating the functionalities of the application. Ensure you have appropriate permissions to access this content.




