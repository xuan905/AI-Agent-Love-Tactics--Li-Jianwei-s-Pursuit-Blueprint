"""
檔案說明：
根據反饋動態調整策略組合
AI 知識點：動態優化（Dynamic Optimization）
劇情比喻：
若效果不佳，李建威調整策略比例或互動順序，提高成功率
"""

feedback = {"公司活動": "好感提升", "金融講座": "冷淡", "貼心小禮物": "好感提升"}

for strategy, result in feedback.items():
    if result == "冷淡":
        print(f"{strategy}策略減少資源分配")
    else:
        print(f"{strategy}策略保持或增加資源分配")

# 操作結果示意
# 公司活動策略保持或增加資源分配
# 金融講座策略減少資源分配
# 貼心小禮物策略保持或增加資源分配
