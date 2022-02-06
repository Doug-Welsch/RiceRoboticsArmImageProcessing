import cv2
import numpy as np

# Initialize Webcam capture (port 0)
video_capture = cv2.VideoCapture(1)

while True:
    # Get webcam value
    retval, frame = video_capture.read()
    cv2.imshow("webcam", frame)

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("webcamgray", gray)

    # Filter out one color channel
    no_red = np.zeros(frame.shape)
    """
    no_red[:, :, 0] = frame[:, :, 0]
    no_red[:,:,1] = frame[:,:,1]
    cv2.imshow("no red", (no_red).astype(np.uint8))
    no_blue = np.zeros(frame.shape)
    no_blue[:,:,1] = frame[:,:,1]
    no_blue[:, :, 2] = frame[:, :, 2]
    cv2.imshow("no blue", (no_blue).astype(np.uint8))
    no_green = np.zeros(frame.shape)
    no_green[:, :, 2] = frame[:, :, 2]
    no_green[:, :, 0] = frame[:, :, 0]
    cv2.imshow("no green", (no_green).astype(np.uint8))
    """

    blue_img = frame[:, :, 0]
    red_img = frame[:, :, 2]
    green_img = frame[:, :, 1]

    blues = np.zeros(frame.shape)
    blues[:, :, 0] = blue_img
    truth_vals0 = blue_img > 120
    truth_vals1 = red_img < 60
    truth_vals2 = green_img > 0
    threshold = truth_vals0 * truth_vals1 * truth_vals2 * blue_img
    blues[:, :, 0] = threshold

    cv2.imshow("Boy Toy Roy", blues);

    # Exit condition
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clear windows, webcam
video_capture.release()
cv2.destroyAllWindows()