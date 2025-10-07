"""
檔案說明：
動態調整行動計畫以適應目標反應
AI 知識點：Adaptive Agent（適應性 Agent）
劇情比喻：
李建威觀察李若冰冷淡反應，調整互動方式
"""

current_plan = ["送咖啡", "書籍話題"]
feedback = {"送咖啡": "好", "書籍話題": "冷淡"}

for i, action in enumerate(current_plan):
    if feedback[action] == "冷淡":
        current_plan[i] = "改變話題"

print("調整後行動計畫：", current_plan)

# 操作結果示意
# 調整後行動計畫： ['送咖啡', '改變話題']
