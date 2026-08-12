# Audit bằng chứng cho bản trình bày PA3

## Phạm vi và ranh giới bằng chứng

- Root repository: `C:\Users\Administrator\Documents\MEGA\tkgd\PA`
- PA1 và PA2 được giữ read-only; sáu PNG prototype gốc không bị chỉnh sửa.
- Các claim về giao diện gốc lấy từ PA2 evidence index, traceability matrix, evidence validation và các screenshot cục bộ đã được phê duyệt.
- Không dùng kết quả người tham gia, thời gian, quote, preference claim hay usability score chưa được chứng minh.
- Không capture thêm screenshot public-site mới vì evidence PA2 đã đủ.

## Kết luận hiện trạng

### Scenario 1 — FIFA.com

Capture `F2-E09` cho thấy trang Tickets & Hospitality tổ chức theo logo giải đấu và card ticket / hospitality với các action như register interest hoặc buy now. Evidence index giới hạn claim: trạng thái capture không cho thấy dashboard hợp nhất cho nhiều giải đấu, seat map, waiting room, resale dashboard hay last-updated dashboard. Traceability matrix ghi nhận ticket action thiếu decision confidence hợp nhất và outbound route cần trust context. Vì vậy bản trình bày so sánh các phương án với bằng chứng ticket-entry và handoff, không phát minh một account state hậu mua hàng.

### Scenario 2 — Chess.com

Capture `C2-E10` cho thấy Analysis entry có Set Up Position, Explore, Game Search, Game Collections, import / upload và Start Analysis. Evidence validation chỉ cho phép dùng ảnh này cho analysis-entry choices; ảnh không cho thấy completed review, engine lines, classification hay beginner explanation. `C2-E08` cho thấy Learn-to-Play có progressive lesson path, explanatory prompt và Next Lesson rõ ràng. Vì vậy ba phương án Chess được trình bày như ba bridge khác nhau từ analysis entry nâng cao sang review cho người mới.

## Phân biệt sáu prototype

- **FIFA Alt 1:** Status Dashboard — “Trạng thái hiện tại là gì?”
- **FIFA Alt 2:** Timeline Tracker — “Tôi đang ở đâu trong tiến trình và tiếp theo là gì?”
- **FIFA Alt 3:** Action Hub — “Bây giờ tôi có thể làm gì?”
- **Chess Alt 1:** Beginner Review Flow — system-selected order, flow tuyến tính có hướng dẫn.
- **Chess Alt 2:** Card Review Mode — user-selected content, dashboard card phi tuyến.
- **Chess Alt 3:** Side-by-Side Assistant — user-selected question, khám phá hội thoại cạnh bàn cờ.

## Bảng mapping bằng chứng

| Scenario | Phương án | Prototype | Screenshot gốc | Finding PA1/PA2 | Vấn đề | Mô hình | Delta chính | Traceability đã xác minh |
|---|---|---|---|---|---|---|---|---|
| FIFA ticket planning | Alt 1 — Status Dashboard | `alt1scenario1.png` | `fifa-20-tickets-hospitality-landing.png` | Thiếu consolidated decision confidence | Cần biết vé đang ở trạng thái nào | Status-first | Thêm account-level status view | `F-A1`; `F-UC02/F-UC03/F-UC06` |
| FIFA ticket planning | Alt 2 — Timeline Tracker | `alt2scenario1.png` | `fifa-20-tickets-hospitality-landing.png` | Cần rõ progress, freshness và next step | Cần biết order đang ở đâu | Progress-first | Thêm lifecycle, history và official source | Tên mô tả; `F-UC02/F-UC04/F-UC06` |
| FIFA ticket planning | Alt 3 — Action Hub | `alt3scenario1.png` | `fifa-20-tickets-hospitality-landing.png`; handoff captures | Cần tìm task và hiểu partner boundary | Cần thực hiện action phổ biến | Tasks-first | Thêm shortcut và handoff trust | Tên mô tả; `F-UC02/F-UC04/F-UC05/F-UC06` |
| Chess beginner review | Alt 1 — Beginner Review Flow | `alt1scenario2.png` | `chess-29-analysis-board.png`; `chess-26-learn-page.png` | Analysis entry có recall demand cao; thiếu beginner bridge | Cần một path rõ từ mistake đến practice | Guided sequence | Thêm Beginner Review có thứ tự cố định | `C-A1`; `C-UC02/C-UC03/C-UC04/C-UC05/C-UC06` |
| Chess beginner review | Alt 2 — Card Review Mode | `alt2scenario2.png` | `chess-29-analysis-board.png`; `chess-26-learn-page.png` | Cần recognition và lựa chọn learning moment | Cần tự chọn moment quan trọng | Non-linear cards | Thêm dashboard card và practice bridge | Tên mô tả; `C-UC03/C-UC04/C-UC05/C-UC06` |
| Chess beginner review | Alt 3 — Side-by-Side Assistant | `alt3scenario2.png` | `chess-29-analysis-board.png`; `chess-26-learn-page.png` | Cần explanation bằng ngôn ngữ đơn giản ngay cạnh board | Cần hỏi mà không rời context | Conversation | Thêm question-led explanation layer | Tên mô tả; `C-UC03/C-UC04/C-UC05/C-UC06` |

## Quyết định

Evidence trong repository là đủ; chỉ dùng evidence trong repository. Không capture thêm trạng thái public-site và không chọn prototype thắng trước formative testing với người tham gia thật.
