"""
檔案說明：
實時更新策略，根據新互動反饋調整
AI 知識點：Online Learning（在線學習）
劇情比喻：
李建威每次與李若冰互動後，立即分析反應並更新策略
"""

feedback = {"微笑策略": 0.2, "話題策略": -0.1}  # 直接用策略名稱做 Key
strategy_model = {"微笑策略": 1.0, "話題策略": 0.5}

for action, value in feedback.items():
    strategy_model[action] += value

print("更新後策略模型：", strategy_model)
# 更新後策略模型： {'微笑策略': 1.2, '話題策略': 0.4}


# 操作結果示意
# 更新後策略模型： {'微笑策略': 1.2, '話題策略': 0.4}
