"""
檔案說明：
辨識目標邊界，避免敏感或冒犯行為
AI 知識點：Boundary Recognition（邊界識別）
劇情比喻：
李建威觀察李若冰情緒反應，避免敏感話題
"""

target_reactions = {"工作話題": "好奇", "私人問題": "不耐煩"}
safe_topics = [topic for topic, reaction in target_reactions.items() if reaction != "不耐煩"]

print("可安全討論話題：", safe_topics)

# 操作結果示意
# 可安全討論話題： ['工作話題']
