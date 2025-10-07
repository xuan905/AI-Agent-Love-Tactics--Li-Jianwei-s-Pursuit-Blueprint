"""
檔案說明：
設定行動限制，確保策略不越界
AI 知識點：Constraint Policy（行為約束）
劇情比喻：
李建威限定互動範圍，只在合理時間與場合行動
"""

allowed_actions = ["咖啡邀約", "書籍話題", "送禮物"]
proposed_actions = ["深夜電話", "咖啡邀約"]

# 檢查行動是否允許
safe_actions = [a for a in proposed_actions if a in allowed_actions]
print("可執行策略：", safe_actions)

# 操作結果示意
# 可執行策略： ['咖啡邀約']
