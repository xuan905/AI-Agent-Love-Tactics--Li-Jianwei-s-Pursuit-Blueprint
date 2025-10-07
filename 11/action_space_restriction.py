"""
檔案說明：
限制策略行動範圍，僅採取安全可接受行動
AI 知識點：Action Space Restriction（行動空間限制）
劇情比喻：
李建威只選擇合理互動策略清單，不強迫目標
"""

all_actions = ["咖啡邀約", "書籍話題", "貼心提醒", "深夜電話"]
restricted_actions = ["咖啡邀約", "書籍話題", "貼心提醒"]

available_actions = [a for a in all_actions if a in restricted_actions]
print("可執行策略：", available_actions)

# 操作結果示意
# 可執行策略： ['咖啡邀約', '書籍話題', '貼心提醒']
