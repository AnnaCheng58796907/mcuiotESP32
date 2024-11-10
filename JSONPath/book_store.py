import datetime
from jsonpath_ng import jsonpath, parse

# 定義一個 JSON 對象
data = {
    "store": {
        "book": [
            {"title": "Book1", "price": 10},
            {"title": "Book2", "price": 15}
        ]
    }
}

# 使用 JSONPath 查詢
jsonpath_expr = parse("$.store.book[?(@.price>12)]")
matches = [match.value for match in jsonpath_expr.find(data)]

print(matches)  # 輸出: ['Book1']