"""
檔案說明：
評估多策略整合後的效果
AI 知識點：成果評估（Outcome Evaluation）
劇情比喻：
李建威觀察多策略互動後累積的好感度
"""

effectiveness = {"公司活動": 0.8, "金融講座": 0.6, "貼心小禮物": 0.7}
total_score = sum(effectiveness.values())
print("多策略整合效果：", effectiveness)
print("整合後總分：", total_score)

# 操作結果示意
# 多策略整合效果： {'公司活動': 0.8, '金融講座': 0.6, '貼心小禮物': 0.7}
# 整合後總分： 2.1
