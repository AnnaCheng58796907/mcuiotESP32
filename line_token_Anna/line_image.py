import requests

# LINE Notify 的 發行權杖
line_token = "V1W3C3V1KyenW7WICbscjhVNeAVDTmHNC093cU6f5Hr"

# 自訂表頭
my_headers = {'Authorization': 'Bearer ' + line_token }

# Form資料
my_data = {'message': '附上照片'}
my_image = open('anna.jpg', 'rb')
my_files = { 'imageFile': my_image }

# 將資料加入 POST 請求中
url = 'https://notify-api.line.me/api/notify'
r = requests.post(url, headers = my_headers, data = my_data, files = my_files)
print(r)