"""
檔案說明：
追蹤個性化互動反饋與效果
AI 知識點：行為優化（Behavior Optimization）
劇情比喻：
李建威每次互動後記錄李若冰反應，評估效果
"""

feedback_log = [
    {"互動": "咖啡話題", "好感度": 0.2},
    {"互動": "書籍話題", "好感度": 0.3}
]

total_affection = sum(f["好感度"] for f in feedback_log)
print("互動反饋記錄：", feedback_log)
print("累積好感度：", total_affection)

# 操作結果示意
# 互動反饋記錄： [{'互動': '咖啡話題', '好感度': 0.2}, {'互動': '書籍話題', '好感度': 0.3}]
# 累積好感度： 0.5
