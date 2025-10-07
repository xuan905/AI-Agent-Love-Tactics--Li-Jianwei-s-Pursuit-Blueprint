"""
檔案說明：
設定回饋函數，量化互動效果
AI 知識點：Reward Function
劇情比喻：
微笑 = +1，冷淡 = -1，幫助李建威判斷策略有效性
"""

# 模擬回饋函數
def reward(reaction):
    return 1 if reaction == "微笑" else -1

# 測試回饋
test_reactions = ["微笑", "冷淡", "微笑"]
rewards = [reward(r) for r in test_reactions]

print("互動回饋值：", rewards)

# 操作結果示意
# 互動回饋值： [1, -1, 1]
