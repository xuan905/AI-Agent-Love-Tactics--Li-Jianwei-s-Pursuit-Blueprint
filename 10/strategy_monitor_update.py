"""
檔案說明：
持續監控策略效果並更新下一步計畫
AI 知識點：Strategy Monitoring & Update（策略監控與更新）
劇情比喻：
李建威觀察互動效果下降 → 自動調整下一步策略
"""

interaction_effect = {"微笑": 0.2, "送咖啡": 0.5, "話題互動": 0.1}
threshold = 0.3
next_actions = []

for action, score in interaction_effect.items():
    if score < threshold:
        next_actions.append("調整策略-" + action)
    else:
        next_actions.append("保持策略-" + action)

print("下一步策略建議：", next_actions)

# 操作結果示意
# 下一步策略建議： ['保持策略-微笑', '保持策略-送咖啡', '調整策略-話題互動']
