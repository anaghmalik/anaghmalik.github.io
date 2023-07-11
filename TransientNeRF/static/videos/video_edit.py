import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

def overlay_video(video_name, image_name, cut):
    base = "/Users/anagh/Projects/anaghmalik.github.io/TransientNeRF/static/videos"
    # Load the WebM video
    video_path = os.path.join(base, video_name)
    cap = cv2.VideoCapture(video_path)

    # Determine video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    overlay = (160, 160)
    # Load the image
    image_path = os.path.join(base, image_name)
    image = cv2.imread(image_path)
    image = cv2.resize(image, overlay)  # Adjust the size as desired

    # Overlay the image onto each frame
    frames = []
    frrange = np.arange(cut[0]*int(fps), (cut[1]+1)*int(fps))
    for _ in range(num_frames):
        ret, frame = cap.read()
        if not ret:
            break
        frame[:overlay[0], :overlay[1]] = image  # Adjust the position as desired
        frames.append(frame)

    frames = frames[frrange[0]:frrange[-1]]
    cap.release()

    # Create an output video writer
    # output_path = "/Users/anagh/Projects/anaghmalik.github.io/TransientNeRF/static/videos/output_video.webm"
    output_path = os.path.join(base, os.path.join("final_vids", video_name))
    fourcc = cv2.VideoWriter_fourcc(*"VP90")
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    # Write modified frames to the output video
    for frame in frames:
        out.write(frame)

    out.release()



if __name__=="__main__":
    frame_dict = {"boot":[0, 11], "ficu":[3, 20], "food":[0, 6], "chef":[0, 13], "cine":[2, 9], "hotd":[3, 23], "lego":[3, 24]}
    path = "/Users/anagh/Projects/anaghmalik.github.io/TransientNeRF/static/videos"
    for file in os.listdir(path):
        if file[-4:] == "webm":

            image_name = [x for x in os.listdir(path) if file[:4] in x and "png" in x][0]
            overlay_video(file, image_name, frame_dict[file[:4]])


