"""
檔案說明：
持續監控策略，確保遵守倫理與邊界
AI 知識點：Policy Monitoring（策略監控）
劇情比喻：
李建威觀察互動被拒絕 → 自動停止或調整策略
"""

interaction_outcome = {"咖啡邀約": "接受", "書籍話題": "拒絕"}
next_actions = []

for action, result in interaction_outcome.items():
    if result == "拒絕":
        next_actions.append("停止策略-" + action)
    else:
        next_actions.append("保持策略-" + action)

print("下一步策略建議：", next_actions)

# 操作結果示意
# 下一步策略建議： ['保持策略-咖啡邀約', '停止策略-書籍話題']
