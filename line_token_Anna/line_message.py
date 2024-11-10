import requests

# LINE Notify 的 發行權杖
line_token = "uqm6kiuzXwAheucEIFfCyjlLRFx7qIGHa1ZzB..."

# 自訂表頭
my_headers = {'Authorization': 'Bearer ' + line_token, 
    "Content-Type": "application/x-www-form-urlencoded"}

# Form資料
my_data = {'message': 'Hello 您好嗎'}

# 將資料加入 POST 請求中
url = 'https://notify-api.line.me/api/notify'
r = requests.post(url, headers = my_headers, data = my_data)
print(r)