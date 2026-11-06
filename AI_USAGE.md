# AI 協作紀錄 (AI Usage Log)


- **學號 / 姓名**：U12627901 / 黃章盛

## 使用的 AI 工具

| 工具 (例：ChatGPT、Gemini、Claude、Copilot) | 版本 / 方案 (例：免費版) | 用在哪幾週 |
|---|---|---|
| Antigravity (Gemini) | 專業版 | Week 04, Week 08, Week 09 |
| OpenAI Codex | Model/version and plan not specified | Week 09 |

---

## Week 04 / 08：PDF 資料輸入與前處理

### 任務 1-A：頁首頁尾溢出清除 (老師示範)

- AI 的白話解釋，我看懂了嗎？　[x] 看懂　[ ] 部分看懂　[ ] 看不懂
- 一句話說明 `_(.+)\.pdf` 這類正則在做什麼：從檔名底線「_」後方動態擷取直到「.pdf」副檔名之前的所有字元，作為該文件的中文法規標題。

### 任務 1-B：雙語標題合併

1. **我寫的部分 (第 4 格「不能發生的事」)**
   ```text
   不能把中文標題與非標題的內文合併，也不能只合併兩個標題而漏掉第三個相鄰的英文標題。
   ```
2. **AI 給的正則表示式**
   ```text
   r"(##\s*[^\n]+)\s*\n+##\s*([^\n]+)"
   ```
3. **第一次斷言結果**：[x] 通過　[ ] 失敗
4. **追問 (若第一次失敗)**：無，第一次測試即通過
5. **AI 的解釋**
   - 我看懂的一個符號：`\n+`，它的作用是 比對連續標題之間的一個或多個換行與多餘空白
   - 我看不懂的地方：無
6. **反例測試**：AI 舉的「不應該被改到」的例子是 一般無 ## 標記的段落內文
   - [x] 我有實際測試，結果：一般內文未被誤改，僅有連續相鄰的 ## 標題被加上 " / " 合併
   - [ ] 我沒有測試

### 任務 1-C：雙語條文合併

1. **我寫的部分 (第 1 格「我想做什麼」與第 4 格「不能發生的事」)**
   ```text
   【1. 我想做什麼】
   將以「-」開頭的中文法規條文與其緊隨在後的英文對照條文合併為單一區塊，中間以 " / " 間隔。

   【4. 不能發生的事】
   絕對不能把「中文條文」與「下一條中文條文」誤併（例如第十五條和第十六條），第二個清單項目必須是英文條文才能合併。
   ```
2. **AI 給的正則表示式**
   ```text
   r"(\S[^\n]*)\s*\n+\s*-\s+([A-Za-z].*)"
   ```
3. **第一次斷言結果**：[x] 通過　[ ] 失敗
4. **追問 (若第一次失敗)**：無，第一次測試即通過
5. **AI 的解釋**
   - 我看懂的一個符號：`[A-Za-z]`，它的作用是 強制要求第二個清單項目必須以英文字母開頭，避免誤併中文條文
   - 我看不懂的地方：無
6. **反例測試**：AI 舉的「不應該被改到」的例子是 連續兩條中文條文（如 - 第十五條 接 - 第十六條）
   - [x] 我有實際測試，結果：連續兩條中文條文各自獨立未被合併，只有中英對照條文成功合併
   - [ ] 我沒有測試

### 本週反思

- AI 第一次給的答案錯在 無錯誤，AI 一次就通過，我用連續兩條中文條文的反例確認它沒有改到不該改的地方。
- 下次寫提示詞，我會多寫 明確的邊界防禦條件（如限定語言字元範圍 [A-Za-z]），因為 這樣能大幅提升程式碼的強健性，避免誤改到結構相似的其他內容。

---

## Week 09：期中資料報告

- **AI tool**: OpenAI Codex. The earlier Gemini entries above are preserved as the existing record.
- **What I requested**: Correct the SEED to 1106, rerun the assigned chunk selector, complete section 3.4, use simple English for the answers, check the remaining work, and help complete the report.
- **Example prompts from this chat**: “seed là 1106, chỉnh chỉnh lại”; “hãy chỉnh câu trả lời thành tiếng anh đơn giản”; “hãy làm giúp tôi”.
- **What Codex did**: Reran the selector and filled the assigned chunk details; drafted the report in simple English; inspected the dashboard; compared real raw and cleaned files; generated labelled source comparison figures; and reran cleaning, chunking, assertions, metrics, and the dashboard using saved Docling Markdown. It did not perform a new PDF conversion.
- **How the results were checked**: Codex matched the selected chunks to JSON records and Markdown lines, checked the SHA-256 codes, recalculated counts and metric values, and verified that regenerated processed JSON files were unchanged. These are AI-assisted checks, not a claim that I independently ran each check by hand.
- **Important correction**: The initial notebook used SEED 1102. I supplied 1106, and Codex reran it. The final verification codes are `7c7d73b6` and `ce165359`.
- **What the review found**: TAR is 100%, but a chunk can still contain only a form number. Passing sample assertions also does not prevent incorrect merges in real documents, such as joining a Part heading and a Chapter heading.
- **AI interpretation and evidence**: See `DATA_REPORT.md` sections 3.2–3.3. The numeric claims are supported by the files; they do not prove improved retrieval accuracy.
- **What still needs my review**: Read the AI-written explanations and independently check at least two claims for section 3.3. Codex originally could not capture desktop screenshots. The three images were later replaced in the workspace with images showing VS Code Compare; Codex visually checked the updated files against the cited examples.

---

- **Reference update**: I supplied a classmate's table with reference values 273.0, 1.0, 0.0, and 5.05. Codex entered them as classmate-supplied values and compared them with my unchanged results. Median length and entropy do not match; the exact cause has not been confirmed.

- **Teacher evidence update**: I later supplied a photo of the teacher's metrics. Codex saved an unchanged copy as `reports/figures/teacher_metrics_reference.jpg` and replaced the classmate-supplied reference values with 270.5, 1.0, 0.0, and 5.0623172389748445. My own metrics were not changed. The raw entropy also differs slightly at full precision, so the exact cause of the differences remains unconfirmed.

- **Teacher instruction correction**: I supplied `week09_midterm.md`. It explicitly says the midterm needs no Git Tag or Release, only Commit & Push by 2026-11-06 11:50 (Asia/Taipei). Codex corrected its earlier Release advice, updated the checklist and README, and preserved the newer Compare images. This correction was made after the deadline; acceptance of a later version must be confirmed with the teacher.
