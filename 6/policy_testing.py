"""
檔案說明：
模擬測試不同策略效果
AI 知識點：策略測試（Policy Testing）
劇情比喻：
李建威在腦中測試幽默搭話或專業分析的效果，選擇最佳策略
"""

strategies = ["幽默搭話", "專業分析"]
effectiveness = {"幽默搭話": 0.8, "專業分析": 0.4}  # 成功率模擬
best_strategy = max(effectiveness, key=effectiveness.get)

print("策略效果測試：", effectiveness)
print("最佳策略選擇：", best_strategy)

# 操作結果示意
# 策略效果測試： {'幽默搭話': 0.8, '專業分析': 0.4}
# 最佳策略選擇： 幽默搭話
