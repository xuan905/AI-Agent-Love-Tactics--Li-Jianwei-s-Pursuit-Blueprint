"""
檔案說明：
評估策略勝率
AI 知識點：成功率評估（Success Rate Evaluation）
劇情比喻：
李建威計算各策略在不同場景的成功率，選擇勝率最高的行動
"""

# 模擬勝率
scenario_success = {"銀行VIP廳": 0.9, "咖啡廳": 0.7, "金融講座": 0.5}
best_scenario = max(scenario_success, key=scenario_success.get)

print("各場景勝率：", scenario_success)
print("最佳場景選擇：", best_scenario)

# 操作結果示意
# 各場景勝率： {'銀行VIP廳': 0.9, '咖啡廳': 0.7, '金融講座': 0.5}
# 最佳場景選擇： 銀行VIP廳
