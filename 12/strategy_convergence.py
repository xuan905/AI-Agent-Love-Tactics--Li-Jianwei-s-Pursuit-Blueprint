"""
檔案說明：
策略收斂分析，確保互動策略穩定
AI 知識點：Strategy Convergence（策略收斂）
劇情比喻：
李建威多次互動後，策略逐漸穩定，不再頻繁調整
"""

strategy_history = [0.2, 0.5, 0.8, 0.85, 0.86]
converged = abs(strategy_history[-1] - strategy_history[-2]) < 0.05

print("策略已收斂：" if converged else "策略尚未收斂")

# 操作結果示意
# 策略已收斂
