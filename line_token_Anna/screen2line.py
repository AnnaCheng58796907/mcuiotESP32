import time
import pyautogui
import requests

print("三秒鐘之後進行螢幕截圖")
time.sleep(3)
myScreenshot = pyautogui.screenshot()   # 截圖
myScreenshot.save('screen.png')  # 儲存為 screen.png

# LINE Notify 的 發行權杖
line_token = "uqm6kiuzXwAheucEIFfCyjlLRFx7qIGHa1ZzB..."

# 自訂表頭
my_headers = {'Authorization': 'Bearer ' + line_token }

# Form資料
my_data = {'message': '附上螢幕截圖'}
my_image = open('screen.png', 'rb')
my_files = { 'imageFile': my_image }

# 將資料加入 POST 請求中
url = 'https://notify-api.line.me/api/notify'
r = requests.post(url, headers = my_headers, data = my_data, files = my_files)
print(r)