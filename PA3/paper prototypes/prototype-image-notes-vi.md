# Ghi chú hình prototype PA3

Đây là tài liệu tham chiếu độc lập cho sáu hình prototype đã được phê duyệt. Các phần dưới đây giữ đúng mapping của PA3; hình gốc được mô tả nhưng không bị vẽ lại hay chỉnh sửa.

## alt1scenario1.png

**Kịch bản:** Scenario 1 — FIFA.com, lập kế hoạch và quản lý vé với sự tự tin.  
**Phương án:** Alt 1 — Status Dashboard.  
**Khái niệm một câu:** Dashboard ưu tiên trạng thái cho người dùng một cái nhìn ở cấp tài khoản về trạng thái vé, sự kiện sắp tới, quick actions và hỗ trợ.  
**Pattern UI nguồn:** Global navigation desktop và pattern card vé của FIFA trong `fifa-20-tickets-hospitality-landing.png`; khung Overview / My Tickets là cấu trúc tương tác được đề xuất trong prototype.  
**Vấn đề:** Người dùng có thể biết giải đấu mình quan tâm nhưng vẫn không có câu trả lời hợp nhất rằng vé đã hợp lệ, đang chờ, đã hủy hay đang chờ họ xử lý.  
**Động lực thiết kế:** PA2 chỉ ra thiếu decision confidence hợp nhất cho ticket và nhu cầu có trust context khi đi ra ngoài FIFA. Prototype áp dụng “state before action”: giải thích trạng thái trước rồi mới đưa hành động phù hợp.  
**Mô hình tương tác:** Status-first, confidence-first. Hệ thống tóm tắt trạng thái, sau đó người dùng mở card sự kiện hoặc một task.  

**Walkthrough từ góc trên trái đến dưới phải:**

1. Browser chrome và global navigation của FIFA tạo bối cảnh desktop được đề xuất, đồng thời giữ các đích đến quen thuộc.
2. Left rail giữ Overview, My Tickets, Orders, Preferences và Help & Support cố định. Overview được chọn để báo đây là trang tổng quan.
3. Lời chào và dòng “Here’s the status of your FIFA events” đặt mục tiêu confidence lên trước. Last updated bổ sung tín hiệu freshness.
4. Bốn summary card hiển thị Confirmed, Pending, Action needed và Cancelled. Mỗi trạng thái có số lượng, giải thích ngắn và cách nhấn mạnh riêng.
5. Khu vực Upcoming Events cho mỗi sự kiện biết giải đấu, trận đấu, ngày, địa điểm, số vé, chỗ ngồi, trạng thái và hành động chính như View Tickets hoặc View Order.
6. Cột phải chứa Quick Actions, Need Help? và các điểm vào hỗ trợ / notification.
7. Dải cuối trang mời bật notification để kéo dài mô hình trạng thái theo thời gian.
8. Các annotation bên phải và phần Problems Solved / Traceability bên dưới giải thích lý do thiết kế của artifact giấy.

**Ý nghĩa các vùng UI chính:**

- **Overview rail:** Định hướng và đường quay lại.
- **State summary:** Nhận diện trạng thái của toàn bộ vé trước khi chọn task.
- **Upcoming event cards:** Chi tiết theo sự kiện và hành động trực tiếp.
- **Quick Actions:** Các task phổ biến không nên bị chôn trong nhiều trang.
- **Need Help / notifications:** Cơ chế hỗ trợ và freshness khi người dùng không chắc chắn.
- **Annotation / legend:** Rationale, traceability và ý nghĩa màu của artifact test.

**Luồng chính:** Mở Overview → đọc summary → chọn sự kiện pending hoặc confirmed → chọn View Order / View Tickets → dùng hỗ trợ hoặc notification nếu chưa rõ.  
**Luồng thay thế:** Mở My Tickets; chọn Transfer Tickets, Add to Calendar hoặc Share Itinerary; mở Help & Support; bật notification.

**Khác biệt với website gốc:** Capture FIFA PA2 là trang Tickets & Hospitality ưu tiên chọn giải đấu với card ticket / hospitality. Trạng thái capture không hiển thị dashboard hợp nhất cho nhiều giải đấu. Prototype đề xuất lớp trạng thái cố định nhưng vẫn giữ global navigation và bối cảnh chính thức.  
**Khác biệt với hai phương án cùng scenario:** Alt 1 tối ưu state recognition. Alt 2 tối ưu process visibility bằng timeline. Alt 3 tối ưu task execution bằng action hub. Alt 1 nhanh nhất cho câu hỏi “vé của tôi có ổn không?” nhưng ít chẩn đoán tiến trình nhất.

**Điểm mạnh:** Quét nhanh; nhận diện trạng thái rõ; phân biệt confirmed và pending; hỗ trợ và notification dễ thấy; phù hợp để triage nhiều sự kiện.  
**Điểm yếu:** Pending có thể vẫn thiếu ownership và expected resolution; View Order / View Tickets có thể khó phân biệt; state count có thể tạo cảm giác yên tâm nhưng chưa giải thích nguyên nhân.  
**Chiều usability bị tác động:** Learnability, recognition thay cho recall, visibility of system status, error prevention, perceived control và trust calibration.  
**Câu hỏi formative testing:** Người tham gia giải thích Confirmed và Pending bằng lời của mình được không? Họ chọn action nào đầu tiên? Họ biết bước tiếp theo thuộc về ai không? Họ có tìm được Help hoặc notification không?  
**Bằng chứng ủng hộ / bác bỏ giả thuyết:** Ủng hộ nếu người dùng giải thích đúng trạng thái và chọn action phù hợp mà không cần facilitator. Bác bỏ nếu họ nhầm ownership của pending, chọn sai giữa View Order và View Tickets, hoặc chỉ lặp lại label mà không biết phải làm gì.

**Gợi ý trình bày 60–90 giây:**

“Đây là FIFA Status Dashboard. Quyết định chính là đưa trạng thái lên trước hành động. Thay vì buộc người dùng mở nhiều trang giải đấu, trang bắt đầu bằng bốn trạng thái: confirmed, pending, action needed và cancelled. Card sự kiện cung cấp context và action chính. Quick actions và hỗ trợ vẫn hiện diện để người dùng đi từ confidence sang action mà không phải tìm kiếm. Lợi ích là nhận diện nhanh. Rủi ro là pending có thể chưa nói rõ ownership và expected resolution. Khi test, nhóm sẽ yêu cầu giải thích một sự kiện confirmed và một sự kiện pending, sau đó đo action đầu tiên và wrong paths. Đây là giả thuyết, không phải kết quả.”

**Exact screenshot gốc dùng để so sánh:**

- `PA2/capture-work/fifa/desktop/fifa-20-tickets-hospitality-landing.png` — bằng chứng ticket-entry chính, `F2-E09`.
- `PA2/capture-work/fifa/desktop/fifa-02-global-navigation-desktop.png` — bối cảnh global navigation khi cần.

## alt2scenario1.png

**Kịch bản:** Scenario 1 — FIFA.com, lập kế hoạch và quản lý vé với sự tự tin.  
**Phương án:** Alt 2 — Timeline Tracker.  
**Khái niệm một câu:** Bề mặt ticket ưu tiên tiến trình, cho thấy lifecycle, mốc hiện tại, freshness và official next steps.  
**Pattern UI nguồn:** Card entry Tickets & Hospitality trong `fifa-20-tickets-hospitality-landing.png`; global navigation và official-source framing là các mốc so sánh.  
**Vấn đề:** Một status label không luôn cho biết đơn hàng đang ở đâu, cập nhật có mới không, hoặc tiếp theo sẽ xảy ra gì.  
**Động lực thiết kế:** Làm tiến trình và freshness rõ ràng để thời gian chờ bình thường không bị hiểu là lỗi hay trì hoãn không giải thích được.  
**Mô hình tương tác:** Progress-first, freshness-first. Người dùng đọc lifecycle từ trái sang phải rồi mở history hoặc official next steps.  

**Walkthrough:**

1. Browser và FIFA navigation tạo shell desktop quen thuộc.
2. Left rail highlight Timeline, tách tracking khỏi Overview và My Tickets.
3. Lời chào nêu mục tiêu track ticket với confidence. Last updated và Official FIFA source xuất hiện ở đầu vùng nội dung.
4. Card sự kiện chính gồm giải đấu, trận đấu, ngày, địa điểm, số vé, trạng thái và order ID.
5. Timeline ngang đánh dấu Order placed, Payment received, Verification, Ticket ready và Event day. Mốc hoàn tất màu xanh, hiện tại màu xanh dương và tương lai màu trung tính.
6. Status sentence dịch timeline sang ngôn ngữ đơn giản; các action mở full timeline hoặc update history.
7. Card thứ hai cho pending order dùng cùng lifecycle để người dùng so sánh phần đã xong và phần đang chờ.
8. Update history ở cuối; cột phải tách Freshness & Updates, Official Next Steps và Need Help?

**Ý nghĩa vùng chính:**

- **Timeline rail:** Cho thấy process position thay vì suy ra từ một label.
- **Current milestone:** Xác định bước cần chú ý bây giờ.
- **Freshness & Updates:** Cho phép kiểm tra thời điểm và lịch sử thay đổi.
- **Official Next Steps:** Gom hướng dẫn delivery, entry và hospitality.
- **Help:** Cho recovery mà không cần tìm toàn website.

**Luồng chính:** Mở Timeline → xác định mốc hiện tại → đọc bước tiếp theo → xem update history nếu cần → theo official guide.  
**Luồng thay thế:** Bật notification; sync calendar; mở full timeline; xem update detail; liên hệ support; kiểm tra event pending thứ hai.

**Khác biệt với website gốc:** Capture FIFA cho thấy card entry theo giải đấu, không phải lifecycle cố định của một order. Prototype thêm process model và freshness layer; không khẳng định ảnh gốc đã có dashboard này.  
**Khác biệt với hai phương án cùng scenario:** Alt 1 trả lời “status hiện tại là gì?” bằng count và event card. Alt 2 trả lời “đang ở đâu trong process?” bằng milestone và history. Alt 3 trả lời “bây giờ làm gì?” bằng task hub.

**Điểm mạnh:** Progress visibility; làm waiting bình thường dễ hiểu; có freshness và official source; hỗ trợ troubleshooting và escalation.  
**Điểm yếu:** Mật độ cao hơn Alt 1; mốc tương lai có thể bị hiểu là user task; cần nêu rõ ownership, normal duration và exception.  
**Chiều usability:** Visibility of system status, feedback, recognition, trust calibration, perceived control và cognitive load khi chờ.  
**Câu hỏi formative:** Người tham gia xác định current milestone được không? Phân biệt system-owned và user-owned step được không? Hiểu Last updated thế nào? Họ có hiểu bước tương lai là nhiệm vụ bắt buộc không?  
**Bằng chứng ủng hộ / bác bỏ:** Ủng hộ nếu họ mô tả đúng current và next step với ít wrong path. Bác bỏ nếu họ xem mọi mốc màu xám là nhiệm vụ của mình hoặc không dùng freshness / official-source cue.

**Gợi ý trình bày 60–90 giây:**

“Alt 2 là Timeline Tracker. Nó không chỉ là một status label nhiều chi tiết hơn. Model chính là progress: order placed, payment received, verification, ticket ready và event day. Mốc hiện tại được nhấn mạnh; trang cũng cho biết lần cập nhật gần nhất và nơi xem official next steps. Điều này giúp người dùng hiểu waiting bình thường và biết điều gì xảy ra tiếp theo. Rủi ro chính là ownership: mốc tương lai có thể trông như nhiệm vụ của user. Nhóm sẽ test xem người tham gia có chỉ được current step, next step và phân biệt việc của hệ thống với việc của mình không.”

**Exact screenshot gốc:**

- `PA2/capture-work/fifa/desktop/fifa-20-tickets-hospitality-landing.png` — bằng chứng ticket-entry, `F2-E09`.
- `PA2/capture-work/fifa/desktop/fifa-02-global-navigation-desktop.png` — bối cảnh navigation.

## alt3scenario1.png

**Kịch bản:** Scenario 1 — FIFA.com, lập kế hoạch và quản lý vé với sự tự tin.  
**Phương án:** Alt 3 — Action Hub.  
**Khái niệm một câu:** Hub ưu tiên task đặt các hành động ticket phổ biến, official options, hỗ trợ và trust của partner handoff vào cùng một nơi.  
**Pattern UI nguồn:** Global navigation và ticket / hospitality entry trong `fifa-20-tickets-hospitality-landing.png`; ranh giới partner trong `fifa-32-before-partner-handoff.png` và `fifa-33-partner-after-public-redirect.png`.  
**Vấn đề:** Người đã có vé thường cần làm một việc cụ thể nhanh, nhưng experience gốc được tổ chức cho discovery thay vì post-purchase actions.  
**Động lực thiết kế:** Giảm friction cho tác vụ phổ biến và báo rõ boundary trước khi rời FIFA.com.  
**Mô hình tương tác:** Tasks-first, shortcuts-first. Người dùng chọn action card thay vì đọc status hoặc timeline trước.

**Walkthrough:**

1. FIFA shell và left rail tạo orientation; Action Hub được chọn.
2. Event strip phía trên gắn các action với một ticket confirmed nhưng không để state summary chiếm ưu thế.
3. Quick Actions gồm View Tickets, Transfer Tickets, Resell Official, Add to Calendar, Share Itinerary, Venue Guide, Fan Guide và Contact Support.
4. Official Options gom hospitality, travel package và official resale marketplace; mỗi card có official / provider cue.
5. Cột phải gom Need Help?, Ticketing Updates và Your Security Matters.
6. Banner cuối trang báo một số option sẽ mở official partner service và data / security được bảo vệ.
7. Annotation bên phải giải thích shortcut, official option và handoff trust; dải dưới lưu problems solved và traceability.

**Ý nghĩa vùng chính:**

- **Event strip:** Cho biết action áp dụng cho ticket nào.
- **Quick Actions:** Shortcut cho công việc hậu mua hàng.
- **Official Options:** Dịch vụ mở rộng tách khỏi quản lý vé cốt lõi.
- **Need Help / Security:** Điểm vào hỗ trợ, policy và trust.
- **Handoff banner:** Feedforward trước outbound navigation.

**Luồng chính:** Mở Action Hub → chọn action → kiểm tra provider / destination cue → tiếp tục hoặc ở lại.  
**Luồng thay thế:** Mở venue / fan guide; contact support; bật updates; xem official options; quay về My Tickets.

**Khác biệt với website gốc:** Capture gốc ưu tiên tournament entry; các capture handoff của PA2 cho thấy ranh giới public-to-partner. Prototype đề xuất lớp task và làm ranh giới đó thấy được trước outbound navigation.  
**Khác biệt với hai phương án cùng scenario:** Alt 1 ưu tiên state recognition; Alt 2 ưu tiên process understanding; Alt 3 ưu tiên execution và trust ở boundary.

**Điểm mạnh:** Recognition thay recall; routine action dễ tìm; option tùy chọn được nhóm; support và handoff rõ.  
**Điểm yếu:** Nhiều action cùng trọng lượng tạo choice overload; package tùy chọn cạnh tranh với task cốt lõi; official label cần provenance và policy chi tiết.  
**Chiều usability:** Efficiency, recognition, user control, error prevention trước outbound, trust calibration và decision load.  
**Câu hỏi formative:** Có tìm Transfer Tickets mà không đi vào vùng không liên quan không? Có phân biệt core ticket management với optional service không? Có hiểu khi destination thay đổi không? Có biết cách quay lại không?  
**Bằng chứng ủng hộ / bác bỏ:** Ủng hộ nếu user chọn đúng task ngay và mô tả đúng provider boundary. Bác bỏ nếu chọn optional extra cho core task, không hiểu link mở gì, hoặc không nhận ra handoff cue.

**Gợi ý trình bày 60–90 giây:**

“Alt 3 là Action Hub. Nó bắt đầu từ các task ticket holder có thể thực hiện: view, transfer, resale, calendar, itinerary, venue và support. Quyết định chính là làm các action dễ quét và tách Official Options khỏi quản lý vé cốt lõi. Banner ‘before you leave FIFA.com’ dựa trên evidence PA2 về public-to-partner boundary. Điểm mạnh là thực thi nhanh. Rủi ro là action grid lớn tạo choice problem mới. Test cần quan sát action đầu tiên, category error và cách người dùng hiểu provider / return path.”

**Exact screenshot gốc:**

- `PA2/capture-work/fifa/desktop/fifa-20-tickets-hospitality-landing.png` — ticket-entry hierarchy, `F2-E09`.
- `PA2/capture-work/fifa/desktop/fifa-32-before-partner-handoff.png` — pre-handoff context.
- `PA2/capture-work/fifa/desktop/fifa-33-partner-after-public-redirect.png` — partner destination context.

## alt1scenario2.png

**Kịch bản:** Scenario 2 — Chess.com, người mới review sau một ván cờ.  
**Phương án:** Alt 1 — Beginner Review Flow.  
**Khái niệm một câu:** Review có hướng dẫn điều khiển thứ tự từ một mistake đến better move và practice path.  
**Pattern UI nguồn:** Analysis entry trong `chess-29-analysis-board.png`; pattern Learn-to-Play trong `chess-26-learn-page.png`; prototype giữ navigation và board context của Chess.com.  
**Vấn đề:** Người mới có thể không biết chọn Analysis path nào, hiểu mistake ra sao hoặc đi tới practice thế nào.  
**Động lực thiết kế:** Đưa pattern “prompt → next step” của Learn vào review sau ván, giảm entry-choice overload và terminology load.  
**Mô hình tương tác:** Fixed linear guided review. Hệ thống chọn thứ tự, user đi theo một path tập trung.

**Walkthrough:**

1. Browser và Chess.com side navigation tạo context. Tiêu đề viết tay trong artifact ghi “SCENE 1”, nhưng mapping PA3 cố định file này là Scenario 2 vì đây là prototype Chess beginner-review.
2. Game Review header hiển thị context của ván và cho chọn Beginner Review thay vì Full Analysis.
3. Bàn cờ giữ vai trò visual reference; các ô highlight nối giải thích với position.
4. Result summary nêu kết quả, accuracy và số key mistakes.
5. Progress indicator cho biết Step 2 of 3 và phần còn lại.
6. Mistake card giải thích bằng ngôn ngữ đơn giản và có Show me on the board.
7. Better-move card giải thích nước đi an toàn hơn và có Try this move.
8. Practice card biến review thành bài tập ngắn; Back và Next mistake giữ navigation.

**Ý nghĩa vùng chính:**

- **Beginner Review / Full Analysis:** Chọn mode rõ ràng, không ép người mới vào advanced analysis.
- **Board:** Nền trực quan cho lời giải thích.
- **Progress indicator:** Thứ tự do hệ thống chọn và closure.
- **Mistake explanation:** Feedback bằng ngôn ngữ dễ hiểu.
- **Better move:** Correction có thể hành động.
- **Practice bridge:** Nối explanation với skill-building.

**Luồng chính:** Chọn Beginner Review → đọc mistake → show trên board → thử better move → start practice → sang mistake tiếp theo.  
**Luồng thay thế:** Chọn Full Analysis; dùng Previous / Next move; Back; bỏ qua mistake; quay về navigation Chess.com.

**Khác biệt với website gốc:** Analysis capture PA2 cho thấy nhiều setup và analysis path nhưng không cho thấy completed beginner review. Prototype tạo bridge có hướng dẫn dựa trên progression của Learn-to-Play.  
**Khác biệt với hai phương án cùng scenario:** Alt 1 là phương án duy nhất có system-selected sequence. Alt 2 cho chọn review card. Alt 3 cho chọn câu hỏi trong conversation.

**Điểm mạnh:** Decision burden thấp; progress rõ; mỗi lần một mistake; feedback và practice liền nhau; closure tốt.  
**Điểm yếu:** Ít linh hoạt cho người có kinh nghiệm; thứ tự cố định có thể không trùng ưu tiên; notation / vocabulary vẫn là barrier; practice có thể làm mất review context.  
**Chiều usability:** Learnability, feedback, memory load, recognition, user control, comprehension và practice continuity.  
**Câu hỏi formative:** Người mới giải thích mistake mà không lặp label được không? Xác định và thử better move được không? Hiểu practice có liên quan vì sao không? Quay lại review được không?  
**Bằng chứng ủng hộ / bác bỏ:** Ủng hộ nếu giải thích mistake và next step mạch lạc với ít trợ giúp. Bác bỏ nếu user nhầm progress, chỉ nhớ “Qe2” mà không hiểu principle, hoặc mất context khi practice bắt đầu.

**Gợi ý trình bày 60–90 giây:**

“Đây là Beginner Review Flow. Vấn đề bắt đầu từ Analysis entry: Chess.com đưa ra nhiều lựa chọn nhưng người mới chưa biết bắt đầu ở đâu. Người dùng chọn Beginner Review, sau đó hệ thống hướng dẫn qua một mistake, explanation đơn giản, better move và practice. Bàn cờ vẫn hiện để lời giải thích có context. Điểm mạnh là decision burden thấp và next step rõ. Rủi ro là ít linh hoạt và vẫn còn notation load. Nhóm sẽ hỏi người tham gia giải thích mistake, thử better move và đến practice.”

**Exact screenshot gốc:**

- `PA2/capture-work/chess/desktop/chess-29-analysis-board.png` — Analysis entry, `C2-E10`.
- `PA2/capture-work/chess/desktop/chess-26-learn-page.png` — progression của Learn-to-Play, `C2-E08`.

## alt2scenario2.png

**Kịch bản:** Scenario 2 — Chess.com, người mới review sau một ván cờ.  
**Phương án:** Alt 2 — Card Review Mode / Visual Card Dashboard.  
**Khái niệm một câu:** Dashboard review phi tuyến cho người dùng duyệt key moments, chọn card và đi thẳng đến explanation hoặc practice.  
**Pattern UI nguồn:** Analysis board trong `chess-29-analysis-board.png`; Learn-to-Play trong `chess-26-learn-page.png`; card và mini-board là review model được đề xuất.  
**Vấn đề:** Một sequence cố định có thể che mất learning priority của user khi ván cờ có nhiều mistake hoặc concept đáng xem lại.  
**Động lực thiết kế:** Giảm recall bằng cách làm moment dễ nhận ra, nhưng vẫn giữ quyền chọn bắt đầu ở đâu.  
**Mô hình tương tác:** Non-linear visual dashboard. User điều khiển selection và order qua card.

**Walkthrough:**

1. Chess.com navigation và board tạo frame ổn định.
2. Banner kết quả đưa ra summary với accuracy và prompt review key moments.
3. Summary chips hiển thị Good Moves, Mistakes, Blunders, Opening và Endgame như một visual index.
4. Key-moment grid gồm mini-board, tên, move number, mô tả và selection control.
5. Card mở rộng giải thích moment, better move và các action Review, Try this move hoặc Go to puzzle.
6. Back to dashboard và Choose another card giữ mô hình phi tuyến; Open in Analysis Board là depth tùy chọn.

**Ý nghĩa vùng chính:**

- **Summary chips:** Overview ưu tiên recognition.
- **Card grid:** Tập hợp learning moment có thể duyệt.
- **Mini-board:** Nhận ra position bằng hình ảnh, giảm phụ thuộc notation.
- **Expanded explanation:** Chỉ mở depth sau khi user chọn.
- **Practice actions:** Nối selected review với bài tập phù hợp.
- **Analysis link:** Depth nâng cao tùy chọn.

**Luồng chính:** Quét summary → chọn card → đọc explanation → thử better move hoặc mở puzzle → quay dashboard / chọn card khác.  
**Luồng thay thế:** Filter card; chọn opening / endgame; mở Analysis Board; chọn card khác; quay dashboard mà chưa practice.

**Khác biệt với website gốc:** Analysis entry gốc bắt đầu bằng setup và command khi người mới chưa biết điều gì quan trọng. Prototype bắt đầu bằng những moment dễ nhận ra trong ván đã chơi rồi mới mở depth.  
**Khác biệt với hai phương án cùng scenario:** Alt 1 có guidance và system-selected order mạnh nhất. Alt 2 cho user chọn content bằng card. Alt 3 cho user chọn question trong conversation.

**Điểm mạnh:** Scanability; recognition; comparison; user control; practice bridge; dễ quay lại nhiều moment.  
**Điểm yếu:** Nhiều lựa chọn làm tăng decision load; màu severity có thể chi phối lựa chọn; user có thể bỏ qua moment quan trọng; taxonomy card có thể tạo vocabulary load.  
**Chiều usability:** Recognition, choice, perceived control, information density, comparison, decision load và practice continuity.  
**Câu hỏi formative:** Card nào được chọn trước và vì sao? Có tóm tắt selected moment được không? Hiểu Review, Try this move và Go to puzzle khác nhau thế nào? Có quay dashboard được không?  
**Bằng chứng ủng hộ / bác bỏ:** Ủng hộ nếu lựa chọn có lý do, mini-board dễ nhận ra và practice tiếp tục đúng. Bác bỏ nếu user chọn ngẫu nhiên hoặc chỉ dựa trên severity, không giải thích được moment, hoặc bỏ practice vì next action không rõ.

**Gợi ý trình bày 60–90 giây:**

“Alt 2 thay đổi control model. Thay vì ép bắt đầu từ một mistake cố định, user thấy dashboard trực quan của các key moments. Summary chips hỗ trợ scan, card có mini-board, selected card mở rộng explanation và practice action. Điểm mạnh là recognition và choice. Rủi ro là decision load. Một blunder nổi bật có thể thu hút user dù một moment khác học được nhiều hơn. Khi test, nhóm quan sát card đầu tiên, hỏi lý do và kiểm tra practice bridge.”

**Exact screenshot gốc:**

- `PA2/capture-work/chess/desktop/chess-29-analysis-board.png` — Analysis entry, `C2-E10`.
- `PA2/capture-work/chess/desktop/chess-26-learn-page.png` — progression pattern, `C2-E08`.

## alt3scenario2.png

**Kịch bản:** Scenario 2 — Chess.com, người mới review sau một ván cờ.  
**Phương án:** Alt 3 — Side-by-Side Assistant.  
**Khái niệm một câu:** Assistant review hội thoại nằm cạnh bàn cờ, trả lời câu hỏi tự nhiên, highlight ô liên quan và gợi ý follow-up.  
**Pattern UI nguồn:** Analysis board và persistent navigation trong `chess-29-analysis-board.png`; progressive explanation trong `chess-26-learn-page.png`; assistant behavior là đề xuất lo-fi.  
**Vấn đề:** Người mới không biết chọn control phân tích nào hoặc chuyển output kiểu engine thành câu hỏi đơn giản về bàn cờ ra sao.  
**Động lực thiết kế:** Giữ board context trong tầm nhìn và cho user hỏi điều họ cần, đồng thời dùng suggested prompt để tránh trạng thái chat trống.  
**Mô hình tương tác:** Conversational, user-directed exploration bên cạnh board.

**Walkthrough:**

1. Left navigation của Chess.com giữ Play, Puzzles, Learn, Train, Watch, News, Social và More; top bar giữ account / search context.
2. Game summary nêu result, accuracy, mistakes và blunders trước khi user hỏi.
3. Board giữ vị trí trung tâm, move hiện tại và highlight cho context không gian.
4. Assistant tab đứng cạnh Analysis, Review, Details và Openings; đây là bounded assistant mode.
5. Conversation gồm user question, plain-language response, mini-board explanation và câu hỏi về better move.
6. Key Moments liệt kê move có dấu hiệu tốt, warning hoặc mistake. Game Summary gom category.
7. Suggested follow-up như Show variations, Why is ...Bxc3 good? và Any similar ideas? tạo hướng đi.
8. Input field cho hỏi tiếp; Share review và các vùng cố định vẫn hiện diện.

**Ý nghĩa vùng chính:**

- **Game summary:** Đặt context trước conversation.
- **Board:** Visual anchor và vị trí của highlight.
- **Assistant conversation:** Giải thích bằng ngôn ngữ dễ hiểu và nhận câu hỏi.
- **Key Moments:** Index review gắn conversation với ván cờ.
- **Suggested follow-ups:** Next step có giới hạn, tránh blank chat.
- **Input field:** User control đối với câu hỏi tiếp theo.

**Luồng chính:** Chọn Assistant → hỏi vì sao move là mistake → đọc response và board highlight → hỏi better move → chọn follow-up → đi đến practice hoặc key moment khác.  
**Luồng thay thế:** Mở Review, Details hoặc Openings; chọn key moment trực tiếp; hỏi variation; share review; quay game archive.

**Khác biệt với website gốc:** Analysis entry capture cho thấy nhiều route nâng cao nhưng không cho thấy lớp giải thích hội thoại cho người mới. Prototype giữ board và key moments trong tầm nhìn rồi thêm explanation layer theo câu hỏi. Không có claim về chất lượng AI response từ capture.  
**Khác biệt với hai phương án cùng scenario:** Alt 1 điều khiển sequence; Alt 2 cho user chọn card; Alt 3 cho user chọn question. Đây là phương án linh hoạt nhất và cũng có rủi ro lớn nhất về response predictability và trust.

**Điểm mạnh:** Contextual explanation; ít chuyển đổi; câu hỏi tự nhiên; board highlight; follow-up; khám phá linh hoạt.  
**Điểm yếu:** Open-ended answer có thể không nhất quán; user có thể tin quá mức; prompt rộng có thể cho câu trả lời nông hoặc mâu thuẫn; practice không tự nhiên nếu không có bridge rõ.  
**Chiều usability:** Learnability, user control, conversational clarity, trust calibration, feedback, context retention và recovery.  
**Câu hỏi formative:** User đặt được câu hỏi hữu ích không? Hiểu answer và board highlight không? Có nhận ra uncertainty hoặc biết hỏi lại không? Có đi đến practice phù hợp không? Ambiguous follow-up gây ra điều gì?  
**Bằng chứng ủng hộ / bác bỏ:** Ủng hộ nếu question-answer cycle dễ hiểu, highlight được diễn giải đúng và next step tự tin nhưng có calibration. Bác bỏ nếu cần moderator prompt liên tục, tin response không rõ hoặc mất review context.

**Gợi ý trình bày 60–90 giây:**

“Alt 3 là Side-by-Side Assistant. User hỏi vì sao một move là mistake hoặc better move là gì, trong khi board và key moments vẫn nhìn thấy. Assistant trả lời bằng ngôn ngữ đơn giản và highlight position liên quan. Suggested follow-up giúp interaction có giới hạn thay vì rơi vào chat trống. Lợi ích là flexibility có context. Rủi ro là chất lượng và trust của answer. Test nên có một câu hỏi bình thường và một follow-up mơ hồ, rồi kiểm tra comprehension, confidence và recovery.”

**Exact screenshot gốc:**

- `PA2/capture-work/chess/desktop/chess-29-analysis-board.png` — Analysis entry và board context, `C2-E10`.
- `PA2/capture-work/chess/desktop/chess-26-learn-page.png` — progressive explanation pattern, `C2-E08`.

