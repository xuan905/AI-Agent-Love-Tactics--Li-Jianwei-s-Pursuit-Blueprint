"""
檔案說明：
調整策略優先順序，將資源集中在最有效策略
AI 知識點：Dynamic Priority（動態優先級）
劇情比喻：
李建威將高回報互動策略提前執行
"""

priority_list = ["送咖啡", "書籍話題", "貼心提醒"]
effectiveness = {"送咖啡": 0.9, "書籍話題": 0.4, "貼心提醒": 0.7}

priority_list.sort(key=lambda x: effectiveness[x], reverse=True)
print("調整後策略優先順序：", priority_list)

# 操作結果示意
# 調整後策略優先順序： ['送咖啡', '貼心提醒', '書籍話題']
