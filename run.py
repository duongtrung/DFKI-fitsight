import subprocess
import threading

def run_script1():
    subprocess.run(["python", "app.py"], check=True)

def run_script2():
    subprocess.run(["python", "beep.py"], check=True)

# Create threads for each script
thread1 = threading.Thread(target=run_script1)
thread2 = threading.Thread(target=run_script2)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()