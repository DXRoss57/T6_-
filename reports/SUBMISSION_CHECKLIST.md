# Checklist theo yêu cầu Week 09 của cô

Nguồn: [week09_midterm.md](instructions/week09_midterm.md). Yêu cầu mới thay thế checklist cũ về Tag/Release.

**Giữa kỳ không cần Git Tag hoặc Release.** Không cần tạo `v0.5-midterm`. Cô sẽ dạy phần này trước kỳ cuối; bài cuối mới yêu cầu `v1.0-final`.

**Hạn nộp:** 6/11/2026 lúc 11:50, giờ Đài Bắc. Cô ghi rõ chấm phiên bản đã Push tại thời điểm 11:50. Lần đối chiếu hướng dẫn này diễn ra sau hạn; cần xác nhận với cô việc nhận bản cập nhật, không thể coi bản sau hạn là bản đã nộp đúng giờ.

## Đối chiếu năm phần báo cáo

| Phần | Tỷ trọng | Trạng thái |
|---|---:|---|
| 1. Tổng quan dữ liệu | 10% | Có bảng 9 PDF, 410 raw chunks, 327 cleaned chunks và giải thích |
| 2. Làm sạch | 20% | Có ba ví dụ thật, ba ảnh Compare, thay đổi, lợi ích và lỗi phát hiện |
| 3. Chỉ số và kiểm chứng AI | 30% | Có số của bạn và cô, giải thích dashboard, ít nhất hai kiểm chứng, hai chunk được chỉ định và mã xác minh |
| 4. Một vấn đề còn tồn tại | 30% | Có tệp, dòng, trích dẫn, nguyên nhân, cách sửa và ảnh hưởng; khác hai chunk ở mục 3.4 |
| 5. Hợp tác AI | 10% | Có nhật ký Week 09 và bài học; cần bạn đọc để xác nhận mình hiểu |

## Tệp bắt buộc Commit & Push

- [x] `DATA_REPORT.md`: đã có nội dung mục 1–5; SEED 1106; mã `7c7d73b6` và `ce165359`.
- [x] `reports/figures/`: có `1a_compare.png`, `1b_compare.png`, `1c_compare.png` và `dashboard.png`; đã xem ảnh cục bộ.
- [x] `AI_USAGE.md`: có Week 09, ghi rõ phần AI hỗ trợ.
- [x] `notebooks/09_midterm_chunks.ipynb`: có đủ output, không có output lỗi.
- [ ] Bạn đọc lại nhận xét và tự kiểm chứng ít nhất hai nhận định, vì mục 3.3 yêu cầu phần kiểm chứng của người học. Kiểm tra tự động của Codex đã được ghi rõ trong bài.
- Nộp bằng Commit & Push, sau đó mở GitHub kiểm tra các ảnh và output notebook. Lệnh hoặc thao tác nộp không thay đổi hạn chấm 11:50 của cô.

## Minh chứng đã kiểm tra

| Ảnh | Cặp tệp trong `data/interim/Academic_Affairs/` | Vị trí |
|---|---|---|
| `1a_compare.png` | `A231060004_學生申請期中停修課程實施要點.md` | Raw 55 và 59 bị xóa; cleaned 51–55 giữ nội dung xung quanh |
| `1b_compare.png` | `A232060013_學生抵免學分辦法.md` | Raw 344–346; cleaned 329: gộp tiêu đề biểu mẫu |
| `1c_compare.png` | `A232020018_大學部學則.md` | Raw 240–241; cleaned 222: gộp Article 2 |

Các ảnh hiện hiển thị giao diện Compare và phần thay đổi cần minh chứng. Một số dòng dài bị cắt ngang ở mép; có thể chụp lại khi bật word wrap để dễ đọc hơn nếu còn thời gian và cô chấp nhận bản cập nhật. Không dùng ảnh dựng thay thế ảnh giao diện. Script `prepare_midterm.py` chỉ ghi vào `reports/source_previews/` để bảo vệ ảnh hiện tại.

Giá trị tham khảo đã đối chiếu với ảnh cô và giữ trong `reports/figures/teacher_metrics_reference.jpg`: 270.5, 100%, 0, 5.06. Không sửa kết quả của bạn để ép khớp giá trị tham khảo.
