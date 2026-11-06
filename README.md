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
- [ ] 完成資料前處理報告 `DATA_REPORT.md`：draft saved; teacher reference photo checked and values entered; student review pending
- [x] 完成指定 chunk 產生器 `notebooks/09_midterm_chunks.ipynb`
- [ ] 報告所需之截圖：dashboard saved; replace the three rendered source comparisons with VS Code Compare screenshots
- [ ] 於 GitHub Release 建立 Tag `v0.5-midterm`

### Midterm review status

- Use `notebooks/01_Data_Ingestion.ipynb` for submission. It reruns the saved Docling Markdown through cleaning, chunking, metrics, and the dashboard; `USE_CACHED_MARKDOWN = False` enables fresh PDF conversion.
- `01_Data_Injestion.ipynb` is a working compatibility copy. Its earlier version is preserved locally under `.ipynb_checkpoints/`.
- Assigned chunks use SEED `1106`: verification codes `7c7d73b6` and `ce165359`.
- `reports/prepare_midterm.py` rebuilds the three labelled source comparison figures. They are not VS Code screenshots.
- Before submission: capture the required Compare screenshots, review the AI-assisted report and usage log, then commit/push and create Release `v0.5-midterm`.

- Teacher reference evidence: `reports/figures/teacher_metrics_reference.jpg`; cleaned values 270.5, 100%, 0, and about 5.06.
