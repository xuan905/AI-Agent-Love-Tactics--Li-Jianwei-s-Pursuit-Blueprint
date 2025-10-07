"""
檔案說明：
監控目標行為，建立觀察模型
Agent 收集目標偏好、互動模式等資料
劇情比喻：
李建威注意李若冰的咖啡習慣、手機使用頻率與同事互動方式
"""

# 模擬目標行為
target_behavior = {
    "coffee": "Latte",
    "phone_usage": "低頻",
    "interaction": "親切但專注"
}

# 觀察目標
print("觀察目標行為中...")
for key, value in target_behavior.items():
    print(f"{key}: {value}")

# 操作結果示意
# 觀察目標行為中...
# coffee: Latte
# phone_usage: 低頻
# interaction: 親切但專注
