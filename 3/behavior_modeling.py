"""
檔案說明：
建立行為模式模型，預測目標互動
AI 知識點：行為模式建模（Behavior Modeling）
劇情比喻：
李建威模擬李若冰可能互動的行為規律，例如對理財話題的回應
"""

# 模擬行為模型
def predict_reaction(topic):
    if topic == "理財":
        return "積極回應"
    elif topic == "咖啡":
        return "微笑回應"
    else:
        return "一般回應"

topics = ["理財", "咖啡", "天氣"]
predictions = {t: predict_reaction(t) for t in topics}

print("行為模式預測：", predictions)

# 操作結果示意
# 行為模式預測： {'理財': '積極回應', '咖啡': '微笑回應', '天氣': '一般回應'}
