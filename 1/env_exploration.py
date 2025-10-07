"""
檔案說明：
模擬銀行環境探索，收集目標資料
Agent 初次進入場景，掃描座位、人流與環境特徵
劇情比喻：
李建威環顧銀行，熟悉座位分布、人流與保安位置
"""

# 模擬環境元素
bank_env = {
    "seats": ["VIP區", "大廳", "窗口區"],
    "people_flow": ["高", "中", "低"],
    "security": ["警衛A", "警衛B"]
}

# 探索動作
print("開始探索銀行環境...")
for key, value in bank_env.items():
    print(f"{key}: {value}")

# 操作結果示意
# 開始探索銀行環境...
# seats: ['VIP區', '大廳', '窗口區']
# people_flow: ['高', '中', '低']
# security: ['警衛A', '警衛B']
