"""
檔案說明：
模擬互動後策略學習
AI 知識點：強化學習（Reinforcement Learning）
劇情比喻：
李建威觀察李若冰每次互動效果，逐步改進策略
"""

# 模擬策略值
action_values = {"幽默搭話": 0, "輕鬆話題": 0, "金融建議": 0}

# 假設互動回饋
feedback = {"幽默搭話": 1, "輕鬆話題": -1, "金融建議": 0}

# 更新策略值
for action in action_values:
    action_values[action] += feedback.get(action, 0)

print("策略學習後行動值：", action_values)

# 操作結果示意
# 策略學習後行動值： {'幽默搭話': 1, '輕鬆話題': -1, '金融建議': 0}
