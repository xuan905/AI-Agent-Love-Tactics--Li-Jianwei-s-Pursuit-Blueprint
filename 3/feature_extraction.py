"""
檔案說明：
從收集資料中萃取關鍵特徵
AI 知識點：特徵提取（Feature Extraction）
劇情比喻：
李建威將喜好整理成可分析特徵，例如「喜歡拿鐵、愛理財書籍」
"""

# 模擬特徵提取
raw_data = target_preferences = {
    "coffee": "Latte",
    "books": ["理財入門", "心理學"],
    "banking": ["理財產品", "存款偏好"]
}

features = {
    "likes_coffee": raw_data["coffee"],
    "book_count": len(raw_data["books"]),
    "financial_interest": "高" if "理財" in "".join(raw_data["books"]) else "低"
}

print("萃取特徵：", features)

# 操作結果示意
# 萃取特徵： {'likes_coffee': 'Latte', 'book_count': 2, 'financial_interest': '高'}
