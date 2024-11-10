import datetime
import cv2
import requests

camera = 0  # Camera Port ID
line_token = "uqm6kiuzXwAheucEIFfCyjlLRFx7qIGHa1ZzB..."   # LINE Notify 的 發行權杖

def line_notify(fna):
    my_headers = {'Authorization': 'Bearer ' + line_token }
    my_data = {'message': 'AI視覺輔助居家照護'}
    my_image = open(fna, 'rb')
    my_files = { 'imageFile': my_image }

    # 將資料加入 POST 請求中
    url = 'https://notify-api.line.me/api/notify'
    r = requests.post(url, headers = my_headers, data = my_data, files = my_files)
    print(r)


# For Web Camera Input:
cap = cv2.VideoCapture(camera)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        # If loading a video, use 'break' instead of 'continue'.
        #continue
        break

    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('Home Care', cv2.flip(image, 1))

    k = cv2.waitKey(10) & 0xFF

    if (chr(k) in 'Ww'):
        dtf = datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f')[:-3]
        png = f'images/{dtf}.png' # File Size 比 jpg 大四倍，不建議使用
        jpg = f'images/{dtf}.jpg'
        cv2.imwrite(jpg, image)
        line_notify(jpg)
    elif (k in [27, ord('Q'), ord('q')]):
        break

cap.release()
cv2.destroyAllWindows()