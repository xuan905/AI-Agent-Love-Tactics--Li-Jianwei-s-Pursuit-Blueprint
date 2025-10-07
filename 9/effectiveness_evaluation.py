"""
檔案說明：
評估個性化互動效果
AI 知識點：效果評估（Effectiveness Evaluation）
劇情比喻：
李建威觀察互動後的好感度累積與策略成功率
"""

effectiveness = {"咖啡話題": 0.8, "書籍話題": 0.9, "休閒話題": 0.7}
total_score = sum(effectiveness.values())
print("互動效果評估：", effectiveness)
print("總效果分數：", total_score)

# 操作結果示意
# 互動效果評估： {'咖啡話題': 0.8, '書籍話題': 0.9, '休閒話題': 0.7}
# 總效果分數： 2.4
