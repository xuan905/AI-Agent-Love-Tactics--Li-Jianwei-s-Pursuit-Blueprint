AI Agent: Love Tactics - Li Jianwei's Pursuit Blueprint

專案簡介
------------
這個專案以模組化的方式收錄多個與「追求策略／互動策略」相關的 Python 範例檔案（教學與實驗性質）。各章節以數字資料夾分組，例如 `1/`, `2/`, ..., `12/`，每個資料夾內為不同主題的實作或說明腳本。

專案目錄（自動掃描）
------------------
以下為本次掃描到的 Python 檔案清單（依資料夾），每個項目後方附上與 AI agent 學習相關的一行用途說明：

- 1/（目標觀察與資料面）
  - `data_collection.py` — 目標觀察與資料收集的範例程式，負責採集環境狀態與行為回饋，作為學習資料來源。
  - `preliminary_strategy.py` — 初始策略／基準策略設定，用來啟動 agent 或做 A/B 比較的 baseline。
  - `target_observation.py` — 目標特徵觀察與前處理（sensor/feature 收集），用於後續模型輸入。
  - `target_lock.py` — 目標鎖定與追蹤邏輯（長期追蹤單一目標或偏好），可用於 reward 指定或任務保持。
  - `env_exploration.py` — 環境探索流程範例（探索策略與探索率設定），協助建立探索/試誤資料。

- 2/（決策與資源配置）
  - `action_priority.py` — 行動優先順序與權重排序，供 policy 在多候選行動時做選擇。
  - `policy_selection.py` — 策略選擇器（多策略管理/切換），支援線上或離線評估不同 policy。
  - `resource_allocation.py` — 資源分配策略（時間、注意力、互動次數），影響探索—利用平衡。
  - `risk_assessment.py` — 風險評估或預測，提供安全性與保守性度量給 agent。
  - `strategy_iteration.py` — 策略迭代範例（policy improvement／policy iteration 的流程示意）。

- 3/（模型與特徵）
  - `behavior_modeling.py` — 使用觀察資料建立行為模型，預測對方回應或偏好分布。
  - `data_collection.py` —（3/ 裡的）收集與整合實驗資料，可能專注於特徵化以供模型訓練。
  - `feature_engineering.py` — 特徵工程流程（從原始觀察產生適用於模型的特徵）。
  - `feature_extraction.py` — 自動或規則化的特徵抽取，支援後端模型輸入。
  - `model_validation.py` — 模型驗證與交叉驗證流程，用於評估 agent 預測/決策品質。

- 4/（行動選擇與策略設計）
  - `action_selection.py` — 行動選擇範例（policy 的實際選擇函式），可能包含 epsilon-greedy / softmax 等。
  - `diversified_strategy.py` — 多樣性策略（避免單一路徑，促進探索與個人化）。
  - `effect_evaluation.py` — 行動效果評估（短期/長期影響評估）。
  - `feedback_loop.py` — 互動回饋迴路（從回饋更新策略或模型），屬於 online learning 的核心。
  - `policy_design.py` — 策略設計原則與範例（如何定義 state、action、reward）。

- 5/（探索/利用與強化學習）
  - `exploration_exploitation.py` — epsilon-greedy 範例（使用標準函式庫 `random`），示範探索—利用 trade-off 的基本實作。
  - `long_term_optimization.py` — 長期回饋累積與最佳策略選擇，關注累積報酬（discounting / return）。
  - `policy_update.py` — 策略更新機制（如基於回饋執行 policy gradient 或 Q-learning 型更新）。
  - `reinforcement_learning.py` — 強化學習流程/簡單 agent 範例（環境互動→回饋→更新）。
  - `reward_function.py` — 報酬函數設計，定義成功/失敗與獎勵訊號的重要性。

- 6/（調整、模擬與測試）
  - `dynamic_adjustment.py` — 動態參數調整（如 epsilon 或學習率隨時間改變）。
  - `environment_simulation.py` — 環境模擬器（用於離線訓練或實驗的平台）。
  - `policy_testing.py` — 策略測試流程（A/B、模擬批次測試與指標收集）。
  - `reaction_prediction.py` — 預測目標反應的模型，供 agent 選擇更佳行動。
  - `success_rate_evaluation.py` — 成功率與績效指標統計，用於迭代改進。

- 7/（優化與群體策略）
  - `dynamic_optimization.py` — 動態優化問題示例（隨時間調整最優行動）。
  - `ensemble_strategy.py` — 多策略集成（ensemble）以獲得更穩健決策。
  - `multi_channel_interaction.py` — 跨多通道互動策略（例如線上訊息 + 面對面等多通路）。
  - `outcome_evaluation.py` — 結果衡量與效能指標設計。
  - `strategy_weighting.py` — 策略加權與融合方式（決策融合的權重更新）。

- 8/（時間與規劃）
  - `discount_factor.py` — 折扣因子相關概念（長期 vs 短期回報的權衡）。
  - `dynamic_adjustment.py` —（8/ 的）時間或計畫相關參數動態調整。
  - `long_term_plan.py` — 長期計劃與分階段策略設計。
  - `progress_tracking.py` — 進度追蹤與學習曲線記錄（training/online metrics）。
  - `time_allocation.py` — 時間資源分配（探索 vs 投入互動的時間策略）。

- 9/（個人化與效果）
  - `behavior_tracking.py` — 行為追蹤紀錄，用作個人化模型的訓練資料。
  - `effectiveness_evaluation.py` — 個別策略成效評估（個人化績效指標）。
  - `feature_collection.py` — 特徵資料匯總（用於訓練個人化模型）。
  - `personalized_plan.py` — 個人化互動計畫生成（根據偏好與歷史）。
  - `strategy_matching.py` — 將可用策略與使用者/目標特徵進行匹配。

- 10/（適應性與線上學習）
  - `adaptive_agent.py` — 自適應 agent 範例（根據回饋調整行為）。
  - `dynamic_priority.py` — 動態優先權調整（哪些目標或互動先處理）。
  - `event_driven_action.py` — 事件驅動的行動（觸發條件與即時回應）。
  - `online_learning.py` — 線上學習範例（即時更新模型或 policy）。
  - `strategy_monitor_update.py` — 策略監控與更新執行（包含安全與回滾機制）。

- 11/（限制與安全）
  - `action_space_restriction.py` — 限制行動空間（避免危險/不可接受行為）。
  - `boundary_recognition.py` — 邊界識別（情境/規範偵測，避免踩線）。
  - `constraint_policy.py` — 約束式策略（policy 被硬性約束的實作）。
  - `olicy_monitor.py` —（檔名疑似打字，應為 `policy_monitor.py`）策略監控器，用於檢測違規或下降的決策行為。
  - `safe_interaction.py` — 安全互動機制（隱私、倫理與用戶舒適度）。

- 12/（優化收斂與驗證）
  - `continuous_optimization.py` — 持續優化流程（online tuning / gradient-based optimization）。
  - `feedback_loop.py` —（12/）回饋迴路設計（強化學習/監督訊號迴圈）。
  - `strategy_convergence.py` — 策略收斂觀測（何時停止學習或切換策略）。
  - `success_verification.py` — 成功驗證機制（實驗後驗證與統計檢定）。
  - `task_completion.py` — 任務完成狀態與後處理（收斂後的重置或長期追蹤）。

注意：上面檔案／註解為自動掃描結果與推測用途；若某些檔案有不同用途或需要更詳細的說明，請告訴我我會協助補充。

依賴與 requirements.txt
-------------------------
我已經自動掃描專案中的 `import`／`from ... import ...` 陳述式，並嘗試判斷是否有第三方（非標準函式庫）套件需要安裝。當前掃描結果顯示：

- 未偵測到需要額外安裝的第三方套件（檔案多為教學範例，僅使用 Python 標準函式庫，例如 `random`）。

因此我已在專案根目錄新增一份 `requirements.txt`，內容說明目前未偵測到第三方套件。如果你接下來加入像 `numpy`, `pandas`, `scikit-learn`, `torch` 等套件，請手動把它們加到 `requirements.txt`（格式為 `package==version`），或讓我代為掃描並加上具體版本。

在本地建立虛擬環境與安裝（Windows / macOS）
-------------------------------------------------
以下為在 Windows 與 macOS 上常見且穩定的 Python 開發環境初始化步驟。示範使用 Python 3.10+（也支援 3.8+），以及內建 `venv` 來建立虛擬環境。

macOS（zsh 範例）

1) 確認系統 Python 或安裝 pyenv（推薦用 pyenv 管理多版本）
	 - 透過 Homebrew 安裝（若尚未安裝 Homebrew，請先至 https://brew.sh 取得安裝指令）
		 brew install pyenv
2) 安裝 Python（例如 3.11）
	 - 使用 pyenv:
		 pyenv install 3.11.6
		 pyenv local 3.11.6
3) 建立虛擬環境（在專案根目錄執行）
	 python -m venv .venv
4) 啟動虛擬環境
	 source .venv/bin/activate
5) 安裝 requirements
	 pip install -U pip
	 pip install -r requirements.txt

Windows（PowerShell 範例）

1) 安裝 Python（從 https://www.python.org/downloads/ 或使用 winget/installers）
2) 建立虛擬環境（在專案根目錄）
	 python -m venv .venv
3) 啟動虛擬環境（PowerShell）
	 .\.venv\Scripts\Activate.ps1
4) 安裝 requirements
	 python -m pip install -U pip
	 pip install -r requirements.txt

常見問題
---------
- 如果在安裝或啟動虛擬環境遇到權限/執行政策（Windows PowerShell）問題，請改用 cmd 或執行：
	Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
- 若要列出已安裝套件並寫回 `requirements.txt`，可在虛擬環境啟動後執行：
	pip freeze > requirements.txt

下一步建議
-------------
- 如果你希望我：
	1) 更精確地偵測第三方套件（包含版本）我可以在一個乾淨的虛擬環境中嘗試 import 每個檔案並收集實際需要的套件清單；
	2) 或是你可把新增的外部套件告訴我，我會把它們加入 `requirements.txt` 並提供安裝/測試指令。

更新紀錄
-----------
- 新增 `requirements.txt`（目前標註為無第三方套件）
- 建立並填入 `README.MD` 專案結構與 Python 環境指引
