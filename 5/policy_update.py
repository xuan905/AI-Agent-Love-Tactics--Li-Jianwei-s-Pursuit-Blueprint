"""
檔案說明：
根據回饋調整策略
AI 知識點：策略更新（Policy Update）
劇情比喻：
李建威保留有效策略，淘汰失敗策略
"""

# 模擬策略更新
strategy_prob = {"幽默搭話": 0.4, "輕鬆話題": 0.3, "金融建議": 0.3}
feedback = {"幽默搭話": 1, "輕鬆話題": -1, "金融建議": 0}

for action, f in feedback.items():
    if f > 0:
        strategy_prob[action] += 0.1
    elif f < 0:
        strategy_prob[action] -= 0.1

print("更新後策略機率：", strategy_prob)

# 操作結果示意
# 更新後策略機率： {'幽默搭話': 0.5, '輕鬆話題': 0.2, '金融建議': 0.3}
