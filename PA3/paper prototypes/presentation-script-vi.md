# Prototype giấy PA3

**Thời lượng mục tiêu:** khoảng 9 phút 12 giây  
**Tốc độ nói:** rõ ràng, khoảng 115–125 từ/phút  
**Đối tượng:** lớp CSC13112 UI/UX Design / peer review  
**Ranh giới bằng chứng:** các nhận định về giao diện gốc dùng capture PA1/PA2 đã được phê duyệt; ngôn ngữ về formative testing là kế hoạch hoặc giả thuyết, không phải kết quả.

## Slide 01 — Trang mở đầu

**Mục đích:** Giới thiệu hai kịch bản và sáu prototype song song.  
**Thời lượng:** 25 giây

**Lời nói:**

“Bài trình bày này giới thiệu các prototype giấy PA3 của nhóm cho hai nhiệm vụ. Nhiệm vụ thứ nhất là FIFA.com, nơi người dùng cần lập kế hoạch và quản lý vé với sự tự tin. Nhiệm vụ thứ hai là Chess.com, nơi người mới bắt đầu muốn xem lại một ván cờ sau khi chơi. Với mỗi kịch bản, nhóm tạo ba phương án có workflow khác nhau. Đây không phải là sáu tính năng sẽ cùng tồn tại, mà là sáu giả thuyết tương tác cần được so sánh bằng formative testing trước PA4.”

**Cue:** [Chỉ vào hai nhãn kịch bản] [Chỉ vào dấu sáu phương án]  
**Chuyển tiếp:** “Trước hết, em làm rõ không gian thiết kế.”

## Slide 02 — Không gian thiết kế PA3

**Mục đích:** Giải thích các trục để sáu phương án khác nhau về hành vi.  
**Thời lượng:** 20 giây

**Lời nói:**

“Ba phương án FIFA khác nhau ở câu hỏi mà giao diện trả lời. Alt 1 là trạng thái: hiện tại vé của tôi thế nào? Alt 2 là tiến trình: tôi đang ở bước nào? Alt 3 là hành động: bây giờ tôi có thể làm gì? Ba phương án Chess khác nhau ở người kiểm soát thứ tự review. Alt 1 là một chuỗi được hướng dẫn, Alt 2 là các thẻ để người dùng tự chọn, và Alt 3 là cuộc hội thoại bên cạnh bàn cờ. Như vậy, khác biệt nằm ở workflow chứ không chỉ ở cách trang trí.”

**Cue:** [Đi qua ba thẻ FIFA] [Đi qua ba thẻ Chess]  
**Chuyển tiếp:** “Trước khi trình bày giải pháp, chúng ta cần xác định baseline của giao diện gốc.”

## Slide 03 — Baseline Scenario 1: FIFA.com gốc

**Mục đích:** Đặt phương án FIFA trong trạng thái desktop đã được capture.  
**Thời lượng:** 30 giây

**Lời nói:**

“Đây là capture PA2 đã được phê duyệt của trang Tickets & Hospitality trên FIFA.com. Cấu trúc nhìn thấy là tournament-first: người dùng thấy logo giải đấu, sau đó là các card vé hoặc hospitality, với những hành động như đăng ký quan tâm hoặc mua ngay. Capture này hỗ trợ mô hình khám phá theo giải đấu, nhưng không cho thấy một dashboard trạng thái vé hợp nhất, một timeline vé cố định, hay tổng quan bước tiếp theo ở cấp tài khoản. Vì vậy, ba phương án của nhóm bổ sung sự rõ ràng cho quyết định; nhóm không khẳng định một trạng thái hậu mua hàng mà ảnh chụp không hiển thị.”

**Cue:** [Chỉ vào logo giải đấu] [Chỉ vào card Tickets và Hospitality] [Chỉ vào footer nguồn]  
**Chuyển tiếp:** “Phương án đầu tiên đưa trạng thái lên trước hành động.”

## Slide 04 — FIFA Alt 1: Status Dashboard

**Mục đích:** Giới thiệu phương án FIFA ưu tiên trạng thái.  
**Thời lượng:** 28 giây

**Lời nói:**

“Alt 1 là Status Dashboard. Ý tưởng chính là status first và confidence first. Người dùng thấy bốn nhóm trạng thái, sau đó là các card sự kiện sắp tới với trạng thái hiện tại và hành động chính. Quick Actions, hỗ trợ và thông báo được đặt gần đó. So với trang gốc ưu tiên chọn giải đấu, đây là một tổng quan ở cấp tài khoản cho nhiều sự kiện. Giả thuyết là người dùng có thể nhận ra trạng thái hiện tại và hành động an toàn tiếp theo mà không cần mở nhiều trang sự kiện.”

**Cue:** [Chỉ vào bốn card trạng thái] [Chỉ vào sự kiện pending] [Chỉ vào Quick Actions]  
**Chuyển tiếp:** “Slide tiếp theo tách các vùng quan trọng và rủi ro cần kiểm tra.”

## Slide 05 — FIFA Alt 1: Giải phẫu tương tác

**Mục đích:** Giải thích workflow, điểm mạnh, điểm yếu và phép thử của Status Dashboard.  
**Thời lượng:** 27 giây

**Lời nói:**

“Crop đầu tiên là tóm tắt bốn trạng thái. Crop thứ hai là các sự kiện sắp tới với hành động chính, còn crop thứ ba giữ hỗ trợ và độ mới của thông tin trong tầm nhìn. Điểm mạnh là khả năng nhận diện nhanh: người dùng quét số lượng, nội dung xác nhận và các sự kiện trong một lượt. Rủi ro là nhãn pending vẫn có thể mơ hồ. Người dùng có thể không biết ai chịu trách nhiệm, thời gian xử lý dự kiến là gì, hoặc View Order khác View Tickets như thế nào. Khi test, nhóm sẽ yêu cầu giải thích một sự kiện confirmed và một sự kiện pending bằng lời của mình, sau đó ghi nhận hành động đầu tiên, đường đi sai và sự do dự.”

**Cue:** [Zoom vào bốn trạng thái] [Zoom vào card pending] [Chỉ vào giả thuyết test]  
**Chuyển tiếp:** “Alt 2 xử lý sự không chắc chắn bằng cách cho thấy tiến trình của đơn hàng.”

## Slide 06 — FIFA Alt 2: Timeline Tracker

**Mục đích:** Giới thiệu phương án FIFA ưu tiên tiến trình.  
**Thời lượng:** 28 giây

**Lời nói:**

“Alt 2 là Timeline Tracker. Nó trả lời một câu hỏi khác: tôi đang ở đâu trong tiến trình và tiếp theo sẽ xảy ra gì? Card sự kiện chính chứa các mốc đã hoàn thành, hiện tại và sắp tới. Panel bên phải thêm độ mới và lịch sử cập nhật; nhãn nguồn FIFA chính thức và các bước tiếp theo giúp củng cố niềm tin. So với ảnh trang ticket gốc, phương án này bổ sung lifecycle và tín hiệu provenance. Giả thuyết là người dùng có thể tìm mốc hiện tại, nói được bước tiếp theo, và đánh giá thông tin có mới và chính thức hay không.”

**Cue:** [Đi theo timeline từ trái sang phải] [Chỉ vào Last updated] [Chỉ vào Official source]  
**Chuyển tiếp:** “Giải phẫu tương tác cho thấy đây không chỉ là một status card nhiều chi tiết hơn.”

## Slide 07 — FIFA Alt 2: Giải phẫu tương tác

**Mục đích:** Phân biệt mental model của tiến trình với mental model của trạng thái.  
**Thời lượng:** 27 giây

**Lời nói:**

“Các vùng chính là đường mốc, panel cập nhật và độ mới, các bước chính thức tiếp theo, và vị trí hiện tại của đơn pending. Điểm mạnh là việc chờ đợi bình thường được tạo hình rõ ràng. Người dùng thấy điều gì đã xảy ra và điều gì chưa xảy ra. Điểm yếu là ownership: các mốc màu xám phía trước có thể trông giống nhiệm vụ người dùng phải làm. Nhóm sẽ test xem người tham gia có phân biệt được việc của hệ thống, việc của người dùng và thời gian chờ bình thường hay không. Alt 1 hỏi ‘trạng thái hiện tại là gì?’, Alt 2 hỏi ‘tôi đang ở đâu trong quy trình?’”

**Cue:** [Zoom vào các mốc completed/current/upcoming] [Chỉ vào Official Next Steps] [So sánh nhãn Alt 1 và Alt 2]  
**Chuyển tiếp:** “Phương án FIFA thứ ba đánh đổi theo hướng thực thi tác vụ.”

## Slide 08 — FIFA Alt 3: Action Hub

**Mục đích:** Giới thiệu phương án FIFA ưu tiên tác vụ.  
**Thời lượng:** 28 giây

**Lời nói:**

“Alt 3 là Action Hub. Thay vì bắt đầu bằng dashboard hoặc timeline, nó bắt đầu bằng những tác vụ người dùng có thể cần: xem vé, chuyển vé, bán lại, thêm lịch, chia sẻ itinerary, xem hướng dẫn địa điểm, hoặc liên hệ hỗ trợ. Phương án cũng tách Official Options và có banner ‘before you leave FIFA.com’ để báo trước handoff. So với trang gốc, đây là cách sắp xếp theo doing thay vì browsing. Giả thuyết là người dùng tìm được một hành động phổ biến nhanh và phân biệt được quản lý vé cốt lõi với dịch vụ tùy chọn hoặc bên ngoài.”

**Cue:** [Chỉ vào Quick Actions] [Chỉ vào Official Options] [Chỉ vào banner handoff]  
**Chuyển tiếp:** “Vùng handoff là rủi ro quan trọng nhất cần kiểm tra.”

## Slide 09 — FIFA Alt 3: Giải phẫu tương tác

**Mục đích:** Giải thích thực thi tác vụ, trust ở handoff và rủi ro về số lượng lựa chọn.  
**Thời lượng:** 27 giây

**Lời nói:**

“Crop Quick Actions cho thấy thiết kế ưu tiên recognition hơn recall. Crop Official Options cho thấy các dịch vụ bổ sung được nhóm lại, còn crop handoff và security giải thích khi nào tác vụ rời FIFA.com. Điểm mạnh là thực hiện nhanh các tác vụ lặp lại. Rủi ro là choice overload: package tùy chọn hoặc resale có thể trông quan trọng ngang với quản lý vé. Nhóm sẽ giao một tác vụ cốt lõi và một tác vụ Official Options, sau đó ghi nhận lựa chọn đầu tiên và hỏi người dùng giải thích provider, destination và đường quay lại. Tóm lại, Alt 1 tối ưu nhận diện trạng thái, Alt 2 tối ưu hiểu tiến trình, còn Alt 3 tối ưu thực thi tác vụ.”

**Cue:** [Chỉ vào lưới shortcut] [Chỉ vào ranh giới provider] [So sánh ba nhãn FIFA]  
**Chuyển tiếp:** “Ma trận này đặt ba mental model cạnh nhau mà chưa chọn người thắng.”

## Slide 10 — So sánh các phương án FIFA

**Mục đích:** Tóm tắt trade-off của Scenario 1.  
**Thời lượng:** 30 giây

**Lời nói:**

“Trang gốc hữu ích cho việc khám phá một sự kiện, nhưng trạng thái được capture không cho thấy tổng quan sau đó mà các phương án đề xuất. Alt 1 phù hợp nhất với việc kiểm tra nhanh trạng thái. Alt 2 phù hợp với việc hiểu chờ đợi và bước tiếp theo. Alt 3 phù hợp với transfer, calendar, venue hoặc support. Mỗi phương án có một rủi ro tương ứng: pending chưa đủ chẩn đoán, ownership chưa rõ, hoặc có quá nhiều lựa chọn. Nhóm sẽ so sánh bằng cùng một bộ nhiệm vụ thay vì chọn từ hình vẽ alone.”

**Cue:** [Đọc dòng Primary user question] [Đọc dòng Main risk] [Chỉ vào dòng Formative focus]  
**Chuyển tiếp:** “Baseline Chess có dạng vấn đề khác: quá nhiều lựa chọn trước khi người mới biết điều gì quan trọng.”

## Slide 11 — Baseline Scenario 2: Chess.com gốc

**Mục đích:** Đặt phương án Chess trong trạng thái Analysis entry và pattern Learn đã capture.  
**Thời lượng:** 30 giây

**Lời nói:**

“Ảnh PA2 này cho thấy Analysis entry của Chess.com. Bên cạnh bàn cờ, người dùng có thể set up position, explore, search games, dùng collections, import file hoặc start analysis. Bằng chứng hỗ trợ nhận định rằng có nhiều đường đi nâng cao, nhưng không cho thấy output review hoàn chỉnh hay lời giải thích cho người mới. Ở PA2, Learn-to-Play có pattern đơn giản hơn: lộ trình tiến bộ, prompt giải thích và nút Next Lesson rõ ràng. Ba phương án Chess thử ba cách đưa pattern đó vào review sau ván cờ.”

**Cue:** [Chỉ vào các lựa chọn Analysis] [Chỉ vào bàn cờ] [Chỉ vào footer nguồn]  
**Chuyển tiếp:** “Alt 1 đưa pattern tiến bộ trực tiếp vào review.”

## Slide 12 — Chess Alt 1: Beginner Review Flow

**Mục đích:** Giới thiệu phương án Chess có hướng dẫn tuyến tính.  
**Thời lượng:** 28 giây

**Lời nói:**

“Alt 1 là Beginner Review Flow. Hệ thống kiểm soát thứ tự: chọn Beginner Review, đi qua một lỗi, đọc giải thích bằng ngôn ngữ đơn giản, xem nước đi tốt hơn, thử nước đi và chuyển sang practice. Điều này giảm số quyết định mà người mới phải đưa ra ở đầu quy trình. Bàn cờ vẫn hiển thị và luôn có bước tiếp theo. So với Analysis entry gốc, đây là một mode có giới hạn thay vì một màn hình phân tích tổng quát. Giả thuyết là người mới giải thích được một lỗi và đến practice với decision burden thấp.”

**Cue:** [Chỉ vào Beginner Review] [Đi theo Step 2 of 3] [Chỉ vào Try this move và Start practice]  
**Chuyển tiếp:** “Điểm mạnh là guidance, nhưng guidance cũng làm giảm user control.”

## Slide 13 — Chess Alt 1: Giải phẫu tương tác

**Mục đích:** Giải thích trade-off usability của flow có hướng dẫn.  
**Thời lượng:** 27 giây

**Lời nói:**

“Progress indicator làm thứ tự trở nên rõ ràng. Panel mistake giải thích vì sao nước đi có vấn đề, panel better move hỗ trợ feedback, còn practice card tạo điểm kết thúc. Lợi ích dự kiến là memory load thấp và learnability tốt hơn. Rủi ro là người có kinh nghiệm thấy flow quá chậm hoặc người mới vẫn bị cản bởi notation và từ vựng. Nhóm sẽ hỏi người tham gia giải thích lỗi mà không lặp lại label, thử nước đi tốt hơn và nói họ sẽ làm gì tiếp theo. Đây vẫn là giả thuyết, không phải kết quả.”

**Cue:** [Chỉ vào progress indicator] [Chỉ vào mistake explanation] [Chỉ vào practice bridge]  
**Chuyển tiếp:** “Alt 2 giữ nội dung học nhưng cho người dùng tự quyết định bắt đầu ở đâu.”

## Slide 14 — Chess Alt 2: Card Review Mode

**Mục đích:** Giới thiệu phương án card phi tuyến.  
**Thời lượng:** 28 giây

**Lời nói:**

“Alt 2 là Card Review Mode. Nó bắt đầu bằng các chip tóm tắt hiệu suất và một lưới key moments. Mỗi card có mini-board và mô tả ngắn. Người dùng chọn một card, mở rộng giải thích, thử nước đi hoặc đi thẳng đến puzzle. Đây không phải là một wizard đổi tên. Khác biệt cốt lõi là người dùng chọn nội dung và thứ tự. So với Analysis entry gốc, giao diện bắt đầu từ những khoảnh khắc dễ nhận ra trong ván cờ thay vì các lệnh setup. Giả thuyết là người dùng duyệt và chọn được moment có ý nghĩa mà không cần nhớ thuật ngữ phân tích.”

**Cue:** [Chỉ vào summary chips] [Chỉ vào card grid] [Chỉ vào selected card]  
**Chuyển tiếp:** “Lợi ích là choice và scanability; rủi ro là decision surface lớn hơn.”

## Slide 15 — Chess Alt 2: Giải phẫu tương tác

**Mục đích:** Giải thích card selection, choice load và practice continuation.  
**Thời lượng:** 27 giây

**Lời nói:**

“Card grid hỗ trợ recognition nhờ mini-board, label và màu trạng thái. Card được chọn mở rộng thành explanation với các hành động review, better move và puzzle. Điểm mạnh là scanability và user control. Điểm yếu là người mới có thể chọn lỗi nổi bật nhất thay vì khoảnh khắc có tính học tập cao nhất, hoặc thấy quá nhiều lựa chọn cùng lúc. Nhóm sẽ ghi nhận card đầu tiên, hỏi lý do lựa chọn và kiểm tra xem participant có hiểu practice connection hay không. Alt 1 để hệ thống chọn thứ tự; Alt 2 để người dùng chọn nội dung.”

**Cue:** [Chỉ vào card grid] [Chỉ vào selected card] [So sánh Alt 1 và Alt 2]  
**Chuyển tiếp:** “Alt 3 đổi unit of control một lần nữa: người dùng kiểm soát câu hỏi.”

## Slide 16 — Chess Alt 3: Side-by-Side Assistant

**Mục đích:** Giới thiệu phương án hội thoại.  
**Thời lượng:** 28 giây

**Lời nói:**

“Alt 3 là Side-by-Side Assistant. Bàn cờ và assistant luôn hiển thị cùng nhau. Người dùng có thể hỏi vì sao một nước đi là mistake, hỏi nước đi tốt hơn và dùng suggested questions để tiếp tục. Câu trả lời có contextual board highlights và key moments. So với Analysis entry gốc, người dùng không cần biết trước phải chọn command nào. Họ bắt đầu bằng câu hỏi tự nhiên nhưng vẫn giữ context của bàn cờ. Giả thuyết là contextual answer giúp giảm chuyển đổi và hỗ trợ khám phá tiếp.”

**Cue:** [Chỉ vào bàn cờ] [Chỉ vào câu hỏi của người dùng] [Chỉ vào response có highlight]  
**Chuyển tiếp:** “Tính linh hoạt này đi kèm rủi ro về trust và consistency.”

## Slide 17 — Chess Alt 3: Giải phẫu tương tác

**Mục đích:** Giải thích điểm mạnh, rủi ro và phép thử của assistant.  
**Thời lượng:** 27 giây

**Lời nói:**

“Crop bàn cờ cho thấy position và key moments. Crop assistant cho thấy câu hỏi và câu trả lời bằng ngôn ngữ đơn giản, còn crop follow-up giữ cho việc khám phá tiếp tục. Điểm mạnh là giải thích có context mà không rời bàn cờ. Rủi ro là câu trả lời mở có thể không nhất quán hoặc bị tin tưởng quá mức. Nhóm sẽ dùng một câu hỏi bình thường và một follow-up mơ hồ. Nhóm quan sát cách người dùng đặt câu hỏi, hiểu câu trả lời, nhận ra uncertainty và recovery. Alt 1 kiểm soát sequence, Alt 2 kiểm soát card, còn Alt 3 kiểm soát question.”

**Cue:** [Chỉ vào key moment màu đỏ] [Chỉ vào response] [Chỉ vào suggested follow-ups]  
**Chuyển tiếp:** “Ma trận Chess làm rõ ba mô hình kiểm soát đó.”

## Slide 18 — So sánh các phương án Chess

**Mục đích:** Tóm tắt trade-off của Scenario 2.  
**Thời lượng:** 30 giây

**Lời nói:**

“Analysis entry gốc cho phép đi sâu linh hoạt, nhưng đặt nhiều quyết định ở đầu quy trình. Alt 1 có guidance cao nhất và closure rõ nhất, đổi lại ít linh hoạt. Alt 2 làm các moment dễ nhận ra và dễ chọn, nhưng tạo thêm choice. Alt 3 giữ context và tính linh hoạt, nhưng phụ thuộc vào chất lượng và tính dự đoán được của hội thoại. Vì vậy, focus của formative testing cũng khác nhau: Alt 1 kiểm tra hiểu mistake, Alt 2 kiểm tra choice và practice, Alt 3 kiểm tra chất lượng câu hỏi và trust.”

**Cue:** [Đọc Who controls sequence?] [Đọc Main risk] [Chỉ vào Formative focus]  
**Chuyển tiếp:** “Vì đây là giả thuyết, bước tiếp theo phải là một protocol chung.”

## Slide 19 — Formative Testing: Cần chứng minh điều gì?

**Mục đích:** Nêu các phép đo formative an toàn về bằng chứng.  
**Thời lượng:** 32 giây

**Lời nói:**

“PA3 yêu cầu thực hiện các session với hai đến ba người tham gia chưa biết prototype trước đó. Với FIFA, nhiệm vụ là xác định trạng thái vé, tìm điều xảy ra tiếp theo, tìm một tác vụ phổ biến và đánh giá thông tin có mới và chính thức hay không. Với Chess, nhiệm vụ là tìm nơi bắt đầu review, giải thích một lỗi, xác định và thử nước đi tốt hơn, rồi đến practice phù hợp. Nhóm ghi nhận completion, comprehension bằng lời của người dùng, đường đi sai, hesitation, perceived control và handoff hoặc practice continuation. Đây là planned measures; project hiện chưa có evidence của real participant results.”

**Cue:** [Chỉ vào FIFA tasks] [Chỉ vào Chess tasks] [Chỉ vào “not results”]  
**Chuyển tiếp:** “Vì vậy PA3 không thể quyết định chỉ từ bản vẽ.”

## Slide 20 — PA3 quyết định gì cho PA4?

**Mục đích:** Kết thúc bằng quyết định dựa trên bằng chứng và bước bàn giao PA4.  
**Thời lượng:** 25 giây

**Lời nói:**

“Sáu sketch đại diện cho sáu giả thuyết tương tác khác nhau. Formative testing sẽ cho biết mô hình FIFA nào tạo ticket confidence tốt hơn, mô hình Chess nào hỗ trợ người mới hiểu ván cờ với decision load chấp nhận được, điểm yếu nào cần sửa, và phương án lo-fi nào nên đi tiếp sang PA4 hi-fi. Bước tiếp theo là chạy cùng một bộ nhiệm vụ trung lập với người tham gia thật, tách observed behavior khỏi interpretation, rồi chọn hướng dựa trên evidence. Em xin cảm ơn.”

**Cue:** [Đi qua dải sáu prototype] [Chỉ vào PA1 → PA2 → PA3 → PA4]  
**Chuyển tiếp:** “Kết thúc.”

## Kiểm tra thời lượng

Tổng thời lượng ước tính là **552 giây / 9 phút 12 giây**, nằm trong yêu cầu PA3 5–10 phút và mục tiêu 9–10 phút.
