import cv2
import os

# 视频文件路径
video_path = 'video/duck.mp4'
# 保存图片的文件夹路径
frames_folder_path = 'dataset/yellow'

# 确保保存图片的文件夹存在
if not os.path.exists(frames_folder_path):
    os.makedirs(frames_folder_path)

# 使用OpenCV打开视频文件
cap = cv2.VideoCapture(video_path)

# 检查视频是否打开成功
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

frame_index = 0

# 循环读取视频的每一帧
while True:
    ret, frame = cap.read()
    # 如果正确读取帧，ret为True
    if not ret:
        break

    # 保存帧为图片
    frame_filename = os.path.join(frames_folder_path, f'frame_{frame_index:04d}.jpg')
    cv2.imwrite(frame_filename, frame)
    frame_index += 1

# 释放视频捕获对象
cap.release()
print(f'Video has been split into {frame_index} frames.')