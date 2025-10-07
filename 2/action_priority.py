"""
檔案說明：
設定多個行動順序，決定先後執行
AI 知識點：行動優先級（Action Priority）
劇情比喻：
李建威安排VIP活動為首，次日安排咖啡偶遇，確保最佳接觸順序
"""

# 模擬行動優先級
actions = ["安排VIP活動", "咖啡偶遇", "送小禮物"]
# 優先級設定
priority_order = sorted(actions, key=lambda x: actions.index(x))

print("行動優先順序：")
for i, action in enumerate(priority_order, 1):
    print(f"{i}. {action}")

# 操作結果示意
# 行動優先順序：
# 1. 安排VIP活動
# 2. 咖啡偶遇
# 3. 送小禮物
