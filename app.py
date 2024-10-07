import cv2
import os

def extract_frames(video_path, output_folder, interval):
    video = cv2.VideoCapture(video_path)
    
    fps = video.get(cv2.CAP_PROP_FPS)
    
    frame_interval = int(fps * interval)
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    current_frame = 0
    saved_frame_count = 0
    
    while True:
        ret, frame = video.read()
        if not ret:
            break

        if current_frame % frame_interval == 0:
            frame_filename = os.path.join(output_folder, f"frame_{saved_frame_count}.jpg")
            cv2.imwrite(frame_filename, frame)
            print(f"Saved: {frame_filename}")
            saved_frame_count += 1
        
        current_frame += 1

    video.release()
    print("Done")

video_path = "./garage.mp4"
output_folder = 'frames'
interval = 5

extract_frames(video_path, output_folder, interval)
