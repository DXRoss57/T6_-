# Việc còn lại trước khi nộp

Bản báo cáo tiếng Anh đơn giản và output notebook đã được lưu. Notebook nhập liệu dùng Markdown do Docling xuất trước đó; không có lượt chuyển PDF mới. Không thay đổi quy tắc làm sạch để giữ nguyên dữ liệu thí nghiệm và kết quả SEED 1106.

## 1. Giá trị tham khảo — đã cập nhật từ ảnh giảng viên

Đã lưu ảnh gốc tại `reports/figures/teacher_metrics_reference.jpg` và sửa mục 3.1: Median Length 270.5, TAR 100%, SDV 0, Entropy 5.06. Kết quả của bạn giữ nguyên: 297, 100%, 0, 5.14. Hai chỉ số chưa khớp; báo cáo đã giải thích giới hạn khi xác định nguyên nhân. Không cần tải thêm file của giảng viên để điền bảng này; ảnh hiện có đủ số liệu. Nếu muốn tìm chính xác nguyên nhân khác biệt thì cần thêm mã nguồn và dữ liệu tham khảo.

## 2. Thay ba ảnh minh chứng bằng ảnh chụp VS Code Compare

Các PNG hiện tại là ảnh dựng từ văn bản thật, đã ghi rõ nguồn và số dòng; chúng không phải ảnh chụp VS Code. Để đáp ứng hướng dẫn của bài, chụp lại giao diện Compare:

1. Mở thư mục `data/interim/Academic_Affairs/` trong VS Code.
2. Nhấn chuột phải tệp `raw_...md` → **Select for Compare**.
3. Nhấn chuột phải tệp `cleaned_...md` cùng tên → **Compare with Selected**.
4. Tìm đúng đoạn ở bảng dưới và chụp cả hai phía, thấy tên tệp và thay đổi.
5. Lưu đè PNG tương ứng trong `reports/figures/`.

| Ảnh | Cặp tệp, bỏ tiền tố raw_/cleaned_ | Vị trí cần chụp |
|---|---|---|
| `1a_compare.png` | `A231060004_學生申請期中停修課程實施要點.md` | Raw 49–61, cleaned 47–55: tên quy định lặp sau Article 7 bị xóa |
| `1b_compare.png` | `A232060013_學生抵免學分辦法.md` | Raw 344–346, cleaned 329: Course Substitution Application Form |
| `1c_compare.png` | `A232020018_大學部學則.md` | Raw 240–241, cleaned 222: Article 2 được gộp |

Sau khi thay ảnh, cập nhật ghi chú ở đầu báo cáo, mục 2, AI_USAGE.md và README để mô tả đúng ảnh chụp mới. Không chạy lại `prepare_midterm.py` sau đó vì script sẽ ghi đè ảnh.

## 3. Đọc lại và nộp

- Đọc nhận xét trong báo cáo và nhật ký AI; xác nhận phần bạn hiểu. Các kiểm tra do Codex thực hiện đã được ghi rõ là có AI hỗ trợ.
- Notebook nộp chính: `notebooks/01_Data_Ingestion.ipynb`. Tệp `01_Data_Injestion.ipynb` là bản tương thích tên cũ; không cần nộp cả hai nếu giảng viên chỉ yêu cầu một notebook.
- `notebooks/09_midterm_chunks.ipynb` dùng SEED `1106`, mã `7c7d73b6` và `ce165359`.
- Kiểm tra Markdown Preview hiển thị đủ bốn ảnh.
- Sau khi hoàn tất mục ảnh ở trên, cập nhật checklist README, commit/push các tệp bài nộp và tạo GitHub Release với tag `v0.5-midterm`.
- Không đưa PDF, dữ liệu JSON hàng loạt, `.venv` hoặc notebook sao lưu vào commit. Chưa thực hiện commit, push hay tạo Release trong lần hỗ trợ này.
