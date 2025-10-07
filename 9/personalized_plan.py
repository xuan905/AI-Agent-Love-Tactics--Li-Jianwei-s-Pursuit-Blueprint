"""
檔案說明：
根據目標喜好生成專屬互動計畫
AI 知識點：個性化推薦（Personalization）
劇情比喻：
李建威安排李若冰喜歡的咖啡、書籍話題互動
"""

preferences = {"咖啡": "拿鐵", "書籍": "理財書", "休閒": "瑜伽"}
personalized_plan = {k: f"互動方案-{v}" for k, v in preferences.items()}

print("個性化互動計畫：", personalized_plan)

# 操作結果示意
# 個性化互動計畫： {'咖啡': '互動方案-拿鐵', '書籍': '互動方案-理財書', '休閒': '互動方案-瑜伽'}
