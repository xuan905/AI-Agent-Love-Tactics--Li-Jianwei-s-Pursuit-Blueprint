"""
檔案說明：
根據反饋動態調整長期策略
AI 知識點：動態調整（Dynamic Adjustment）
劇情比喻：
若短期策略效果不佳，李建威微調每日互動順序或方式
"""

daily_strategy = ["微笑互動", "專業建議", "貼心小禮物"]
feedback = {"微笑互動": "好", "專業建議": "冷淡", "貼心小禮物": "好"}

for strategy in daily_strategy:
    if feedback[strategy] == "冷淡":
        print(f"{strategy}策略順序後移")
    else:
        print(f"{strategy}策略保持")

# 操作結果示意
# 微笑互動策略保持
# 專業建議策略順序後移
# 貼心小禮物策略保持
