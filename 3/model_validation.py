"""
檔案說明：
驗證模型準確性與預測能力
AI 知識點：模型驗證（Model Validation）
劇情比喻：
李建威觀察李若冰對新話題的反應，確認特徵與行為模式是否有效
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

# 模擬驗證
new_feedback = {"理財": "積極回應", "咖啡": "微笑回應"}
validation_results = {t: (predictions[t] == new_feedback[t]) for t in new_feedback}

print("模型驗證結果：", validation_results)

# 操作結果示意
# 模型驗證結果： {'理財': True, '咖啡': True}
