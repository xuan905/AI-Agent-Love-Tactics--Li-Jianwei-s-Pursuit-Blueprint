"""
檔案說明：
評估策略延遲回報
AI 知識點：延遲回報（Discount Factor）
劇情比喻：
李建威了解某次互動短期效果小，但累積信任後總收益高
"""

short_term_effect = 0.3
discount_factor = 0.9
long_term_value = short_term_effect * discount_factor**3

print("短期互動效果：", short_term_effect)
print("折算長期價值：", long_term_value)

# 操作結果示意
# 短期互動效果： 0.3
# 折算長期價值： 0.2187
