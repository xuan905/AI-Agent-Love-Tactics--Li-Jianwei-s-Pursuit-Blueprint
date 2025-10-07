"""
檔案說明：
對特徵進行轉換與編碼，方便模型分析
AI 知識點：特徵工程（Feature Engineering）
劇情比喻：
李建威將咖啡種類、書籍類型數值化，便於計算和策略分析
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

# 模擬特徵工程
encoded_features = {
    "coffee_code": 1 if features["likes_coffee"] == "Latte" else 0,
    "book_count": features["book_count"],
    "financial_interest_code": 1 if features["financial_interest"] == "高" else 0
}

print("編碼後特徵：", encoded_features)

# 操作結果示意
# 編碼後特徵： {'coffee_code': 1, 'book_count': 2, 'financial_interest_code': 1}
