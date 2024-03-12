import cv2
import sys

def extract_frames(video_path, output_folder, interval):
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    for i in range(0, frame_count, interval):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()

        if not ret:
            break

        frame_filename = f"{output_folder}/frame_{i}.jpg"
        cv2.imwrite(frame_filename, frame)

    cap.release()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python frames.py <video_path> <output_folder> <interval>")
        sys.exit(1)

    video_path = sys.argv[1]
    output_folder = sys.argv[2]
    interval = int(sys.argv[3])

    extract_frames(video_path, output_folder, interval)



# python frames.py video\\ch01_20240113003938.mp4 . 5