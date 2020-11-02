import os
os.environ["PROJ_LIB"] = 'C:\\Users\\Chethan\\Anaconda3\\Library\\share'

import pandas as pd
import visualize as v
import glob
import cv2

def save_video():
    
    # Save the video to the location
    image_folder = 'C:/Users/Chethan/Desktop/TUD/TUD Sem 3/screenshots/'
    video_name = 'C:/Users/Chethan/Desktop/TUD/TUD Sem 3/screenshots/video.mp4'
    
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
#    print(images)
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape
    
    video = cv2.VideoWriter(video_name, 0, 1, (width,height))
    
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))
    
    cv2.destroyAllWindows()
    video.release()

def show_video():
    # Show the video
    cap = cv2.VideoCapture('C:/Users/Chethan/Desktop/TUD/TUD Sem 3/screenshots/video.mp4')
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
    #         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', frame)
            if cv2.waitKey(350) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()


def graph_with_date():
    d = input("""Enter the date for visualization in YYYYMMDD format. 
              Example: 20200115 (for January 15th 2020)
              Range: January 1st 2019 till August 31st 2020: """)
    input_date = d
    
    d = d[:-2]

    path = r'C:/Users/Chethan/Desktop/TUD/TUD Sem 3/Research Project/DataSet/' # use your path
    all_files = glob.glob(path + "*" + d + "*.csv")

    li = [] 
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        li.append(df)
        
    df = df.dropna()
    input_date = input_date[0:4] + "-" + input_date[4:6] + "-" + input_date[6:] + " 00:00:00+00:00"
    temp = df[df["day"] == input_date]
    v.show(temp,input_date[0:11],video=0)
    
def graph_of_month():
    d = input("""Enter the year and month for visualization in YYYYMM format. 
              Example: 202001 (for January 2020 video): """)

    path = r'C:/Users/Chethan/Desktop/TUD/TUD Sem 3/Research Project/DataSet/' # use your path
    all_files = glob.glob(path + "*" + d + "*.csv")

#    print(all_files)
    li = [] 
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        li.append(df)
        
    df = df.dropna()
    
    dates = list(dict.fromkeys(df["day"]))
    files = glob.glob(r'C:/Users/Chethan/Desktop/TUD/TUD Sem 3/screenshots/*')
    for f in files:
        os.remove(f)
    
    for d in range(len(dates)):
        temp = df[df["day"] == dates[d]]
        v.show(temp,dates[d][0:11],video=1)
    save_video()
    show_video()

while True:   
# print options to user:
    choice = input("""What do you want to do?
    0\tSee the visualization of a particular date.
    1\tSee the video of one month's visualizations.
    2\tExit program.
    enter answer (0/1/2): """)
    
    # Evaluate user's choice and proceed accordingly
    if choice == "0": # Image
        graph_with_date() 
    elif choice == "1": # Video
        graph_of_month()
    elif choice == "2": # Exit program 
        print("Thank you for using this program.")
        break 
    else:
        print("Please enter correct input.")
