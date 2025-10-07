"""
檔案說明：
累積回饋形成長期策略
AI 知識點：長期優化（Long-term Optimization）
劇情比喻：
李建威逐步建立攻心策略系統，提高互動成功率
"""

# 模擬累積回饋
cumulative_rewards = {"幽默搭話": 5, "輕鬆話題": -2, "金融建議": 1}

# 選擇長期最優策略
best_strategy = max(cumulative_rewards, key=cumulative_rewards.get)

print("長期最優策略：", best_strategy)

# 操作結果示意
# 長期最優策略： 幽默搭話
