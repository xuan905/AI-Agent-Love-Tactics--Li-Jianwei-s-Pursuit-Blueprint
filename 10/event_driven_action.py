"""
檔案說明：
根據事件觸發特定互動行動
AI 知識點：Event-Driven Action（事件觸發行動）
劇情比喻：
李若冰作息改變 → 自動送貼心提醒
"""

events = {"作息變化": True, "心情冷淡": False}
actions = []

if events["作息變化"]:
    actions.append("送貼心提醒")
if events["心情冷淡"]:
    actions.append("安排新活動")

print("事件觸發行動：", actions)

# 操作結果示意
# 事件觸發行動： ['送貼心提醒']
