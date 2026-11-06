# NLP 自然語言處理 (115 S1) - 課程專案

本專案為 NLP 課程開發環境與實作練習區。

---

## 開發者資訊 (Developer Info)
* **學號**：[U12627901]
* **姓名**：[黃章盛]

## 硬體與環境狀態 (Environment Setup)
* **PyTorch 執行環境**：[Windows CPU]

---

## 課程任務清單 (Task Checklist)

### Week 2：開發環境與專案架構初始化
請在完成下列任務後，將 `[ ]` 改為 `[x]`：
- [x] 成功建立 GitHub 帳號並 Clone 本專案至本機端。
- [x] 成功建立 `.venv` 虛擬環境，並透過 `.gitignore` 隱藏底層檔案。
- [x] 成功於虛擬環境內安裝通用套件清單 (`requirements.txt`) 與專屬硬體版本的 PyTorch。
- [x] 更新本 README 文件，填寫學號、姓名與 PyTorch 環境狀態。
- [x] 成功使用 Git 完成 `commit` 並 `push` 同步至 GitHub 雲端。

### Week 4 / 8：PDF 資料輸入與前處理
- [x] 三個斷言 (1-A、1-B、1-C) 都顯示 [Success]
- [x] Notebook (`notebooks/01_Data_Ingestion.ipynb`) 已存檔，保留輸出結果
- [x] `metrics.json` 在專案根目錄
- [x] `AI_USAGE.md` 的 Week 04/08 段落已填寫
- [x] `requirements.txt` 已新增 `docling` 與 `matplotlib`
- [x] `.gitignore` 已設定忽略 PDF、大量 JSON 與 MD 檔案
- [x] 在 GitHub 網頁上打開 notebook，看得到儀表板

### Week 9：期中評量 (Midterm Assessment)

Teacher instructions: [`week09_midterm.md`](reports/instructions/week09_midterm.md).

**Midterm does not require a Git Tag or Release.** Submit by Commit & Push. The teacher states a deadline of **2026-11-06 11:50 (Asia/Taipei)** and grades the version available at that time. Later updates need the teacher's acceptance.

- [x] `DATA_REPORT.md` sections 1–5 drafted; section 3.4 includes verification codes.
- [x] Images are stored in `reports/figures/`; three Compare images and the dashboard were visually checked locally.
- [x] `AI_USAGE.md` includes the Week 09 record.
- [x] `notebooks/09_midterm_chunks.ipynb` is saved with execution outputs.
- [ ] Student has read and confirmed the AI-assisted explanations.
- Submission method: Commit & Push the report, figures, AI log, and selector notebook, then check their display on GitHub. No `v0.5-midterm` tag or Release is needed.

### Midterm review status

- Use `notebooks/01_Data_Ingestion.ipynb` for the ingestion work. Its saved run reuses existing Docling Markdown, reruns cleaning, chunking, metrics, and the dashboard, and does not claim a new PDF conversion.
- `01_Data_Injestion.ipynb` is an optional compatibility copy with the old spelling.
- Assigned chunks use SEED `1106`, with verification codes `7c7d73b6` and `ce165359`.
- Teacher reference evidence: `reports/figures/teacher_metrics_reference.jpg`; cleaned values 270.5, 100%, 0, and about 5.06. Own metrics remain unchanged.
- `reports/prepare_midterm.py` generates optional rendered previews under `reports/source_previews/`. It does not replace the submission images in `reports/figures/`.
- Earlier checkpoints were pushed before the deadline. The time of the latest correction does not establish that it was part of the version graded at 11:50.
