## Lời cảm ơn
## Lý do chọn đề tài

    Theo báo cáo tình hình an toàn thông tin trong nước 6 tháng đầu năm 2024, tình hình an toàn thông tin toàn cầu tiếp tục diễn biến phức tạp và đáng lo ngại. Các cuộc tấn công đang gia tăng cả về mức độ số lượng và cả mức độ tinh vi, nhắm vào rất nhiều các cơ quan chính phủ, doanh nghiệp và các tổ chức cá nhân.

    VNPT ghi nhận xu hướng tấn công mã hóa dữ liệu  với mục đích tống tiền các doanh nghiệp (ransomware attack) tăng cao đáng báo động. Số lượng các cuộc tấn công trên toàn thế giới đã tăng gấp 1,3 lần so với cùng kỳ 2023, riêng khu vực Việt Nam đã tăng gần gấp 2 lần và để lại nhiều ảnh hưởng nghiêm trọng đến cả uy tín, tài sản của nhiều doanh nghiệp, tổ chức. Số lượng các cuộc tấn công mạng tại Việt Nam tăng hơn 60% so với năm 2023. Số lượng mã độc mới được phát triển đãng tăng hơn 52%, các nhóm tin tặc với mục đích tài chính có nhiều kỹ thuật và thủ đoạn mới, các chiến dịch cũng có sự đầu tư hơn tiêu biểu như các nhóm GoldFactory, Ducktail.

    Các lỗ hổng mới năm 2024 gia tăng 64,33% so với với cùng kỳ năm 2023, đặc biệt số lượng các lỗ hổng có mức độ nghiêm trọng cao cũng tăng cao. Tuy vậy số lượng lỗ hổng 0day bị khai thác ngoài tự nhiên đã giảm khoảng 50%. Trong số đó các hạ tầng thường tồn tại các lỗ hổng Security Misconfiguration ~28,05%, XSS và Broken Access Control (BAC) hơn 19%, tỉ lệ này không thay đổi nhiều so với năm 2023. [1]

    Trước những biến động khó lường của tình hình tấn công mạng cũng như sự phát triển của khoa học công nghệ đòi hỏi các tổ chức và doanh nghiệp luôn phải sẵn sàng cho việc đảm bảo an toàn thông tin nội bộ doanh nghiệp và thông tin của khách hàng. 

    Thời gian thực tập ở doanh nghiệp, em mong muốn xây dựng được một góc nhìn toàn diện và đầy đủ về tình hình triển khai một hệ thống mạng, nhằm đảm bảo đáp ứng nhu cầu sử dụng mạng và đảm bảo an toàn thông tin trong doanh nghiệp.

## Danh mục hình ảnh
## Danh mục bảng

# Chương 1. Giới thiệu chung
1. Giới thiệu chương trình thực tập

2. Giới thiệu đơn vị thực tập
2.1. Tên công ty thực tập: Công ty cổ phần giải pháp CNTT Tân Cảng (TCIS)
2.2. Giới thiệu chung: 
    Công ty Cổ phần Giải pháp CNTT Tân Cảng Tiền thân là phòng CNTT thuộc Tổng Công ty Tân Cảng Sài Gòn (Saigon Netport Coporation - SNP)
    
    Được thành lập năm 1996, trải qua 28 năm hoạt động, phòng CNTT Tân Cảng Sài Gòn đã thực hiện thành công các ứng dụng CNTT trong quản lý, điều hành của Tổng công ty. Nổi bật là việc tích hợp và triển khai thành công phần mềm điều hành và khai thác cảng TOPX (RBS Úc) kết nối với phần mềm quản lý container CMS, qua đó tự động hóa việc điều hành khai thác cảng, tăng năng suất giải phóng tàu, giảm thời gian giao nhân container. Nghiên cứu và phát triển ứng dụng thành công phần mềm quản lý kho CFS mới, áp dụng CNTT trong quản lý vật tư, quản lý tài chính, lao động, quản lý tiền lương; triển khai các ứng dụng giá trị gia tăng như tra cứu thông tin về container qua tin nhắn điện thoại di động (SMS), qua website; qua ứng dụng truyền nhận số liệu EDI với các hãng tàu ... đã không ngừng nâng cao chất lượng dịch vụ của Tổng công ty. 

    Với những kết quả đã đạt được trong ứng dụng CNTT vào hoạt động quản lý, điều hành khai thác cảng, Tổng Công ty TCSG đã là cảng tiên phong ứng dụng thành công tin học hóa trong điều hành sản xuất ở quy mô lớn, khẳng định và giữ vững uy tín thương hiệu, vị thế là nhà khai thác cảng container chuyên nghiệp, hiện đại và lớn nhất Việt Nam. Đặc biệt, thương hiệu Tân Cảng Sài Gòn trở thành Thương hiệu Quốc gia và Cảng Cát Lái  hiện đứng trongTop 40 cảng container hàng đầu thế giới.

    Nhằm đáp ứng yêu cầu nghiên cứu, ứng dụng, triển khai có hiệu quả các giải pháp CNTT trong lĩnh vực khai  thác cảng biển, ngày 15/11/2010, Tổng công ty Tân Cảng Sài Gòn đã quyết định thành lập Công ty Cổ phần Giải pháp CNTT Tân Cảng (TCIS). Với đội ngũ nhân sự chất lượng lượng cao, được đào tạo cơ bản và thường xuyên huấn luyện nâng cao từ các hãng Microsoft, Oracle, Cisco, SUN...cùng với kinh nghiệm qua 15 năm thực hiện thành công các ứng dụng và giải pháp công nghệ thông tin tại Tổng Công ty, TCIS đã và đang hướng đến mục tiêu trở thành nhà cung cấp dịch vụ, giải pháp CNTT chuyên nghiệp, chất lượng và uy tín hàng đầu trong lĩnh vực khai khác cảng biển, kho bãi, hậu cần, dây chuyền cung ứng.... 

2.3. Hoạt động kinh doanh:
- Liên kết, hợp tác chiến lược với các đối tác để xây dựng các ứng dụng CNTT theo tiêu chuẩn quốc tế;
- Tư vấn phân tích, thiết kế và triển khai tích hợp các hệ thống thông tin quản lý doanh nghiệp và các hệ thống quản lý trong lĩnh vực cảng biển, kho bãi, hậu cần dây chuyền cung ứng…
- Cung cấp và cho thuê các thiết bị CNTT, thiết bị chuyên dụng trong lĩnh vực cảng biển, kho bãi, dây chuyền cung ứng…;
- Quản lý, vận hành hệ thống CNTT;
- Tư vấn, huấn luyện đào tạo về CNTT;
- Xử lý, cho thuê dữ liệu;
- Cung ứng nguồn nhân lực CNTT trong và ngoài nước.

2.4. Thông tin liên lạc;
- Trụ sở chính: 722 Điện Biên Phủ, P.22, Q. Bình Thạnh, TP.HCM
- Số điện thoại: (84 -24)3 747 6666
- Fax: 3512 4049  

3. Giới thiệu vị trí thực tập:
- Vị trí thực tập: nhân viên quản lý mạng máy tính
4. Kế hoạch thực tập:
    4.1. Thời gian thực tập
    - Thời gian bắt đầu: 22/7/2024
    - Thời gian kết thúc: 30/9/2024

5. Các giai đoạn thực tập:
    - Giai đoạn 1: Nghiên cứu và ôn tập kiến thức nền tảng
    Tìm hiểu và làm quen với một số platform mà doanh nghiệp sử dụng
    - Giai đoạn 2: Nghiên cứu cơ cấu mạng doanh nghiệp
    - Giai đoạn 3: Tham gia vào các hoạt động thực tế
    - Giai đoạn 4: Viết báo cáo thực tập doanh nghiệp

# Chương 2. Nghiên cứu lý thuyết
Kiến thức nền tảng: 
1. Hệ thống mạng:
1.1. Tổng quan về mạng máy tính
- **Mạng máy tính (Computer Network)**: là mạng viễn thông kĩ thuật số được sử dụng để kết nối nhiều máy tính với nhau thông qua các thết bị kết nối mạng và phương tiện truyền thông (Giao thức mạng, môi trường truyền dẫn) bằng một cấu trúc và các máy tính trong mạng có thể trao đổi thông tin với nhau.
- **Quản trị mạng máy tính (Network Administration)**: Là công việc nhuawmf quản lý, giám sát và duy trì, bảo mật và phục vụ mạng cho một tổ chức. Tuy nhiên, các nhiệm vụ và thủ tục cụ thể có thể sẽ tùy thuộc vào quy mô và mô hình của tổ chức.
- **Cacs công việc của quản trị mạng máy tính:** bao gồm giám sát mạng, duy trì chất lượng và bảo mật mạng. Giám sát là điều cần thiết để theo dõi các lưu lượng mạng truy cập bất thường, theo dõi tình trạng cơ sở hạ tầng và các thiết bị được kết nối mạng.

Bên cạnh đó, quản trị mạng có thể phát hiện sớm các hoạt động bất thường, các sự cố phát sinh để có thể ngăn ngừa, duy trì và khắc phục chất lượng, đảm bảo mạng thông suốt và liên tục. 

Quản lý mạng bao gồm nhiều chức năng quản trị, gồm lập kế hoạch, triển khai và cấu hình mạng, cụ thể như sau:
- Quy hoạch lại mạng dựa trên các yêu cầu thay đổi của tổ chức.
- Triển khai mạng để đạt hiệu quả cao
- Cáu hình các giao thức mạng và các giao thức bảo mật mạng khác nhau.
- Áp dụng các bản vá bảo mật và cập nhật chương trình cơ sở của hạ tầng mạng, chẳng hạn như bộ định tuyến, bộ tập trung, bộ chuyển mạch và tường lửa. 
- Đánh giá điểm yếu của mạng.
- Đannhs giá chất lượng và dung lượng để tăng hoặc giảm dung lượng mạng, quản lý tránh lãng phí tài nguyên.
1.2. Kiến trúc OSI/ISO

1.3. Tìm hiểu về mạng LAN
**Giới thiệu mạng cục bộ**: LAN (Local Area Network) là một hệ thống mạng máy tính cho phép các thiết bị kết nối và giao tiếp với nhau nhằm chia sẻ dữ liệu. 

**Kết nối trong mạng LAN**
Kết nối trong mạng LAN thường được thiết lập thông qua cáp mạng hoặc kết nối không dây, trong một khu vực giới hạn nhất định, đó có thể là văn phòng, nhà riêng hoặc trường học.

- LAN cho phép các thiết bị trao đổi thông tin và tài nguyên như tệp tin, máy in, và ứng dụng, tạo điều kiện cho sự hợp tác và chia sẻ trong một mội trường cục bộ.

- Phạn vi sử dụng LAN: LAN có phạm vi sử dụng hạn chế trong một khu vực như văn phòng, nhà riêng, trường học, phòng game, hoặc doanh nghiệp. Thông thường phạm vi của mạng LAN không vượt quá 100m

- Các kiểu (các kiến trúc) trong LAN
// Bảng biểu gì đó // 

**Các tiêu chuẩn của mạng LAN**:
Các tiêu chuẩn của LAN Ethernet chỉ định hệ thống cáp và tín hiệu cả lớp liên kết vật lý và dữ liệu của mô hình tham chiếu OSI: 

// Hình ảnh //

-	IEEE chia lớp liên kết dữ liệu OSI thành 2 lớp con riêng biệt:
o	ĐIều khiển liên kết logic (LLC): Chuyển tiếp lên lớp mạng
Cho phép một phần của lớp liên kết dữ liệu (Data Link) hoạt động độc lập với cấc công nghệ hiện có Lớp này cung cấp tính linh hoạt trong các dịch vụ cho các giao thức lớp mạng ở trên nó, đồng thời giao tiếp hiệu quả với nhiều loại công nghệ MAC và Lớp 1 bên dưới nó. LLC, với tư cách là một lớp con, tham gia vào quá trình đóng gói.
            Một LLC header cho lớp liên kết dữ liệu biết phải làm gì với một gói khi nó nhận được một khung. Ví dụ, một máy chủ nhận một khung và sau đó nhìn vào LLC header để hiểu rằng gói được dành cho giao thức IP ở lớp mạng.
            Ethernet header ban đầu (trước IEEE 802.2 và 802.3) không sử dụng LLC header. Thay vào đó, nó sử dụng một trường loại trong Ethernet header để xác định giao thức Lớp 3 đang được mang trong khung Ethernet.

o	MAC: Chuyển xuống lớp vật lý
 MAC Sublayer xử lý quyền truy cập phương tiện vật lý. Đặc tả MAC của IEEE 802.3 xác định địa chỉ MAC, địa chỉ này nhận dạng duy nhất nhiều thiết bị ở lớp liên kết dữ liệu. Lớp con MAC duy trì một bảng địa chỉ MAC (địa chỉ vật lý) của các thiết bị. Để tham gia vào mạng, mỗi thiết bị phải có một địa chỉ MAC duy nhất.



**Các kiểu (Topology) của mạng LAN

// Bảng biến dị của mạng LAN


// Chú thích cho bảng biến dị 

1.3.2. Các thiết bị mạng
-	Được chia thành các lớp và các thiết bị tiêu biểu cho các lớp đó được thể hiện dưới đây:
-	Thiết bị truyền dẫn trong mạng máy tính là các thiết bị có khả năng truyền dẫn dữ liệu từ các thiết bị này đến các thiết bị khác trong mạng. Các thết bị truyền dẫn trong mạng có thể phân loại theo nhiều tiêu chí khác nhau, trong đó tiêu chí phổ biến nhất đó chính là phân loại theo các lớp trong mô hình OSI.
-	Theo các lớp trong mô hình OSI, các thiết bị mạng có thể được phân loại như sau:
-	• Lớp 1 (Physical Layer): Các thiết bị truyền dẫn ở lớp 1 có chức năng truyền dẫn dữ
-	liệu ở dạng vật lý, bao gồm các loại cáp, đầu nối, bộ chuyển đổi tín hiệu,...
-	• Lớp 2 (Data Link Layer): Các thiết bị truyền dẫn ở lớp 2 có chức năng truyền dẫn dữ
-	liệu ở dạng frame, bao gồm các loại hub, repeater, bridge,...
-	• Lớp 3 (Network Layer): Các thiết bị truyền dẫn ở lớp 3 có chức năng truyền dẫn dữ liệu giữa các mạng khác nhau, bao gồm các loại router, gateway,...
-	Một số thiết bị truyền dẫn trong mạng máy tính bao gồm:
-	• Card mạng (Network Card): Là thiết bị được gắn vào máy tính để tạo khả năng kết nối
-	mạng cho máy tính.
-	• Modem (Modulator/Demodulator): Là thiết bị biến đổi tín hiệu số thành tín hiệu tương tự và ngược lại, được sử dụng để kết nối máy tính với mạng Internet.
-	• Router (Bộ định tuyến): Là thiết bị chuyển tiếp dữ liệu giữa các mạng khác nhau.
-	• Switch (Bộ chuyển mạch): Là thiết bị kết nối nhiều máy tính với nhau trong cùng một mạng.
-	• Access Point (Thiết bị phát sóng WiFi): Là thiết bị tạo ra mạng WiFi để các thiết bị không dây có thể kết nối với nhau.
-	 Các thiết bị truyền dẫn đóng vai trò rất quan trọng trong việc xây dựng và vận hành mạng máy tính. Giúp các thiết bị trong mạng có thể giao tiếp được với nhau và trao đổi dữ liệu một cách hiệu quả. 

1.3.3 Wireless Network

**Giới thiệu mạng không dây**: Công nghệ wireless LAN
Trong những năm gần đây, wireless LANs đã chiếm một vị trí cực kì quan trọng trong thị trường mạng LAN, ngày càng có nhiều tổ chức tin rằng mạng không dây là một bổ sung không thể thiếu cho mạng LAN có dây truyền thống. Để đáp ứng các yêu cầu về tính di động, dễ dàng thay đổi vị trí, mạng Ad-Hoc và khả năng phủ sóng ở những nơi rất khó để kéo dây tới.
-	Chúng ta có thể xem xét ba loại mạng LAN chính, được phân loại theo công nghệ truyền dẫn thông tin như sau: Hồng ngoại, 
-	Từ cách đặt tên, mạng wireless LANs được sử dụng trong một môi trường truyền dẫn không dây. Đến gần đây, sau khi đã có thể giải quyết được những vấn đề tồn tại của nó như khả năng truyền tải kém, giá thành cao và lo ngại các vấn đề về bảo mật thông tin cũng như cần thiết các hạ tầng phù hợp... thì mạng LAN đã phát triển và trở thành một phần không thể thiếu của doanh nghiệp. 
-	Giới thiệu về Wifi: WiFi (Wireless Fidenlity, là công nghệ cho phép người dùng có thể truy cập vào Internet dựa trên sóng vô tuyến không dây mà không cần thông qua các kết nối vật lý như dây mạng. Nói cách khác, wifi phát ra các loại sóng tương tự như sóng điện thoại hay sóng radio để truyền tín hiệu tới các thiết bị điện tử như TV, điện thoại, hay máy tính bảng và các thiết bị có thể kết nối tới sóng wifi.


// Bảng các chuẩn wifi được sử dụng phổ biến hiện nay

1.4. Tìm hiểu về mạng WAN

Mạng diện rộng (Wide Area Network) là công nghệ kết nối các văn phòng, các trung ttâm dữ liệu, ứng dụng đám mấy của bạn với nhau, Nó được gội là mạng diện rộng vì không chỉ nằm trong phạm vi một tòa nhà hoặc một khuôn viên rộng lớn mà còn mở rộng ra nhiều vị trí trải dài trên một khu vực địa lý cụ thể, hoặc thậm chí là trên toàn thế giới

Ví dụ các doanh nghiệp có nhiều văn phòng chi nhánh quoocs tế sử dụng mạng WAN để kết nối với các văn phồng lại với nhau. 

Mạng WAN lớn nhất thế giới là Internet vì nó là tập hợp của nhiều mạng quốc tế kết nối với nhau.

**Mục đích của kết nối mạng WAN**
Mạng diện rộng (WAN) là xương sống của doanh nghiệp hiện nayu. Với việc số hóa tài ngjuyeen các công ty sử dụng mạng WAN để thực hiện những việc sau:

- Giao tiếp bằng giọng nói và video
- Chia sẻ tài nguyên giữa nhân viên và khách hàng
- Truy cập kho dữ liệu và sao lưu dữ liệu từ xa
- Kết nối với các ứng dụng chạy trên nền tảng đám mây
- Chạy và lưu trữ các ứng dụng nội bộ

Cải tiến công nghệ WAN giúp các tổ chức truy câp thông tin một cách an toàn, nhanh chóng và đáng tin cậy. Mạng WAN rất quan trọng đối với năng suất và tính liên tục của doanh nghiệp. 

**Kiến trúc mạng WAN**
Kiến trúc mạng diện rộng dựa trên mô hình Kết nối hệ thống mở (Open System interconnection – OSI). Mô hình này định nghĩa và tiêu chuẩn hóa tất cả các phương tiện viễn thông về mặt khái niệm. Mô hình OSI hình dung bất kì mạng máy tính nào hoạt động trên 7 lớp. Các công nghệ mạng khác nhau hoạt động dựa trên mỗi lớp khác nhau nhằm tạo nên một mạng WAN hoạt động hiệu quả. Dưới đây là mô hình tổng quan: 

Lớp 7 – Lớp ứng dụng (Application Layer)
Lớp ứng dụng là lớp gần với người dùng nhất và xác dịnh cách nguồi dùng tương tác với mạng. Nó chứa các logic ứng dụng và không biết đến việc triển khai mạng. Ví dụ các doanh nghiệp có hệ thống đặt lịch, lớp này quản lý logic đặt trước như gửi lời mời chuyển đổi múi giờ, v.v. 

Lớp 6 – Lớp trình bày (Present Layer)
Lớp này chuẩn bị dữ liệu để truyền trên mạng. Ví dụ: Tăng cường mã hóa để tội phạm mạng theo dõi WAN không thể đánh cắp thông tin các cuộc họp nhạy cảm.

Lớp 5 – Lớp phiên (Session Layer)
Lớp phiên quản lý các kết nối hoặc phiên giữa các ứng dụng cục bộ và từ xa. Nó có thể mở, đóng hoặc ngắt kết nối giữa 2 thiết bị. Ví dụ như hệ thống đặt trước được đặt trên máy chủ web ở văn phòng trung tâm và người dùng đang làm việc tại nhà. Lớp phiên mở kết nối giữa máy tính của người dùng và máy chủ web sau khi đã xác thực. Kết nối này là kết nối logic, khonong phải là kết nối vật lý thực tế. 

Lớp 4 – Lớp truyền tải (Transport Layer) 
Lớp này xác định các chức năng và quy trình để truyền tải dữ liệu. Nó phân loại và gửi dữ liệu để chuyển đi. Lps này cũng đóng gói dữ liệu thành các gói dữ liệu. Ví dụ khi người dùng truy cập vào trang web. Giao thức TCP quản lý thông tin liên lạc bằng cách sắp xếp thành các gói tin request và response.

Lớp 3 – Lớp mạng (Network Layer) 
Lớp mạng quản lý các gói tin dữ liệu qua mạng. Nó có nhiệm vụ xác định các quy tắc định tuyến gói tin, cân bằng tải và mất mát gói tin.

Lớp 2 – Lớp liên kết dữ liệu (Datalink Layer)
Lớp liên kết dữ liệu chịu trách nhiêm thiết lập các quy tắc hoặc giao thức truyền thông trên các hoạt động của lớp vật lý. Ví dụ như xác định thời điểm bắt đầu hoặc chấm dứt kết nối trực tiếp. Chức năng này chuyển tiếp các gói tin từ thiết bị này sang thiết bị khác cho đến khi các gói tin đến được đúng đích. 

Lớp 1 – Lớp vật lý (Physic Layer)
Lớp vật lý quản lý việc chuyển dữ liệu thô dưới dạng bit kĩ thuật số, tín hiệu quang hoặc sóng điện tử trên các phương tiện truyền dẫn khác nhau, chẳng hạn như sợi quang và công nghệ không dây. 

**WAN hoạt động như thế nào**
- Doanh nghiệp có tài nguyên chạy trong nhiều trung tâm dữ liệu tại chỗ, văn phòng chi nhánh và các đám mây riêng ảo (VPC). Để kết nối các tài nguyên này, doanh nghiệp sử dụng nhiều kết nối mạng và dịch vụ Internet. Vì các công ty không thể xây dựng cơ sở hạ tầng mạng của riêng họ trên nhiều ranh giới địa lý, vì thế nên họ thường sẽ thuê từ nhà cung cấp dịch vụ bên thứ ba.
- Sau đây là một số kiểu kết nối phổ biến
    - Đường dây thuê
    Đây là một kết nối mạng trực tiếp mà bạn có thể thuê từ một nhà cung cấp mạng lớn (ví dụ như IPS ). Nó có thể kết nối hai điểm đầu cuối LAN với nhau. ĐƯờng dây thuê không nhất thiết phải là đường truyền vật lý. ĐÓ có thể là các kết nối ảo mà nhà cung cấp dịch vụ thực hiện trên cơ sở hạ tầng mạng khác. 

    - Truyền liên mạng
    Đây là một cách để mã hóa các dữ liệu khi chúng di chuyển qua Internet ccoong cộng. Trong quá trình truyền liên mạng, bạn sử dụng kết nối Internet để truy cập vaiof máy chủ của doanh nghiệp của quốc gia khác. Tuy nhiên bạn giửu các gói dữ liệu dưới dạng gói tin được đóng gói, tạo thành các mạng ảo (VPN)

    - Chuyển đổi nhãn đa giao thức
    Chuyển mạch nhãn đa giao thức (MultiProtocol Label Switching - MPLS) là một kĩ thuật định tuyến lưu lượng dữ liệu dựa trên các nhãn được xác định trước, kĩ thuật này cố gắng định tuyến lưu lượng dữ liệu quan trọng qua các đường dẫn mạng ngắn hơn hoặc nhanh hơn, quia đó cải thiện hiệu suất mạng. Nó hoạt động giữa lớp 2 và lớp 3 của kiến trúc OSI. Bạn có thể sử dụng kĩ thuật này để tạo một mạng hợp nhất trên các cơ sở hạ tầng mạng hiện có, ví dụ như IPv6, chuiyeenr tiếp khung, ATM hoặc Ethernet. Bạn có thể sử dụng đường dây thuê MPLS hoặc MPLS với VPN để tạo ra một mạng hiệu quả và an toàn

1.5. Tìm hiểu về SD - WAN

    Mạng diện rộng do phần mềm xác định (Software-defined Wide Area Network – SD – WAN) là bước tiến xa hơn của công nghệ MPLS. Công nghệ này giúp tóm tắt các chức năng của MPLS thành một phần mềm. Vì hoạt đọng trên các kết nối Broadband Internet (Internet băng thông rộng), nên SD – WAN thường có thể giúp giảm chi phí mạng và mang lại tính linh hoạt cao hơn so với kết nối cố định. 

    - MPLS so sánh với SD – WAN
    MPLS có thể làm chậm quá trình tích hợp công nghệ Cloud vì nó định tuyến lưu lượng truy cập qua các trụ sở công ty, đóng vai trò như các điểm nghẽn trung tâm. Trái lại SD – WAN nhận biết được hệ thống đám mây và tích hợp hiệu quả hơn so với cơ sở hạ tầng đám mây hiện đại. SD – WAN cũng tiết kiệm được chi phí. Nó hoạt động được qua MPLS để bạn có thể sử dụng băng thông hiệu quả hơn trên các đường dây thuê MPLS đắt tiền.

    - Tối ưu hóa mạng diện rộng
    Tối ưu hóa mạng diện rộng (WAN) là một tập hợp các kĩ thuật cải thiện các chỉ số hiệu suất của mạng WAN như thông lượng, tắc nghẽn và độ trễ. Thiết kết mạng WAN, lựa chọn công nghệ và bố trí luồng lưu lượng đều là những hoạt động ảnh hưởng đến hiệu suất của mạng WAN. Sau đây là một số kĩ thuật phổ biến để tối ưu hóa mạng WAN.
    
    - Quản lý luồng lưu lượng (Flow Control)
    Quản lý luồng lưu lượng bao gồm các kỹ thuật giảm thiểu lưu lượng dữ liệu được  gửi qua mạng. Ví dụ như:
    
    - Bộ nhớ đêm được lưu trữ thường xuyên trên các Local Server.

    - Xác định và loại bỏ các bản sao dữ liệu dư thừa cho các ứng dụng sao lưu và phục hồi dữ liệu sau sự cố.

    - Nén hoặc tạo tệp dữ liệu ở định dạng zip.

    - Tăng tốc giao thức
    Một số giao thức WAN có tính chất là một cuộc “trò chuyên” – conversation – nghĩa là chúng có thể yêu cầu nhiều hoạt động truyền dữ liệu qua lại cho một yêu cầu kết nối duy nhất. Ví dụ: các máy Client và Server đều có thể gửi lại dữ liệu xác nhận rằng họ đã nhận được dữ liệu. Quá trình tăng tốc cho giao thức giao tiếp sẽ kết hợp các thông tin liên lạc qua các giao thức giao tiếp để giảm số lượng gói tin cần truyền qua mạng, qua đó tăng tốc độ của kết nối.

    - Tốc độ và giới hạn kết nối
    Các nhà quản trị mạng có thể giới hạn số lượng liên kết truy cập Internet đang mở, số lượng người dùng và lượng băng thông mỗi người dùng có thể truy cập tại mỗi thời điểm. Ví dụ, các nhà quản trị mạng có thể đặt ra các quy tắc để ngăn chặn nhân viên phát tán các thông tin trên mạng WAN của doanh nghiệp
    
    - Phân đoạn mạng
    Quá trình định hình lưu lượng sẽ kiểm soát luồng dữ liệu cho các ứng dụng cụ thể, giúp phân chia băng thông mạng một cách tối ưu giữa các ứng dụng. Nhà mạng có thể chọn ưu tiên một số ứng dụng quan trọng để cải thiện hiệu suất của chúng.

1.6. Kiến trúc mạng trong doanh nghiệp.
1.6.1 Mô hình mạng trong doanh nghiệp
1.6.2. Giao thức được sử dụng trong mô hình mạng

1.7. Đảm bảo hệ thống mạng trong doanh nghiệp.
1.7.1. High Availability (HA)
1.7.1.1. Giới thiệu về HA và hoạt động trong doanh nghiệp

    High Availability (HA) hay “tính sẵn sàng cao” với khả năng để thiết bị, server hoạt đọng liên tuc, không lỗi trong một khoảng thời gian nhất định. Hiểu một cách đơn giản thì HA hoạt động nhằm đảm bảo hệ thống đáp ứng tốt yêu cầu và luôn trong tư thế sẵn sàng đến 99,99 %.

    HA được áp dụng ở nhiều lĩnh vực khác nhau, từ quân sự, chăm sóc sức khỏe và các ngành công nghiệp... Cuộc sống con người ngày càng phụ thuộc vào các hệ thống đó. Nếu HA được thiết kế bài bản và kiểm tra theo đúng quy trình, đảm bảo kiểm tra kĩ lưỡng trước khi đưa vào sử dụng để luôn đáp ứng tính khả dụng mà các nhà lưu trữ cũng như chuyển đổi dự phòng của hệ thống HA.

1.7.1.2. HA hoạt động như thế nào

    Trong thực tế, không phải bất cứ hệ thống nào cũng luôn đảm bảo hoạt động 100%, do đó với những hệ thống có tính sẵn sàng cao sẽ được hoạt động với hiệu suất tối đa nhằm đảm bảo tính liên tục và bền bỉ cho hệ thống. Một khi thiết kế hệ thống đáp ứng được HA, chúng ta phải tuân thủ theo 3 nguyên tắc sau: 

    Nguyên tắc 1: **điểm lỗi duy nhất (SPOF)**: Toàn bộ hệ thống có thể bị lỗi mà nguyên nhân xuất phát là do lỗi từ một điểm duy nhất. Chẳng hạn như một Server chạy một ứng dụng thì Server này chính là điểm lỗi duy nhất tác động đến tính khả dụng của ứng dụng khi nó bị lỗi. 

    Nguyên tắc 2: Xây dựng đường dự phòng. Với hệ thống HA thì việc xây dựng một đường dự phòng là rất quan trọng trong việc thay thế khi một thành phần nào đó trong hệ thống bị lỗi. Hoạt động này sẽ đảm bảo chuyển đổi từ X sang Y, đảm bảo được hiệu suất và dữ liệu an toàn.

    Nguyên tắc 3: Khả năng phát hiện lỗi: KHi thiết kế một hệ thống trong một thời diểm thì việc cân bằng tải là cực kì quan tr ọng để đảm bảo được tính sẵn sàng cao. Khối lượng công việc sẽ được cân bằng tải sắp xếp và phân bố để không một tài nguyên nào bị quá tải.

1.7.1.4. Làm thế nào để có thể đạt được HA trong môi trường doanh nghiệp? 

    Để đáp ứng được các yêu cầu từ bộ cân bằng tải, các Server trong hệ thống HA được phân bố trong các cụm và được tổ chức theo kiến trúc tầng. Trong trường hợp một Server thuộc một cụm nào đó bị lỗi thì sẽ dược chuyển tới một Server khác thay thế và sẵn sàng tiếp quản công việc. Nếu trong một hệ thống phức tạp thì tính sẵn sàng cao khó lòng được đảm bảo vì sẽ xuất hiện nhiều điểm lỗi hơn so với hệ thống mạng đơn giản hơn.

1.7.1.5. Các nguyên tắc để thiết kế và duy trì một hệ thống HA hoàn thiện:

1.7.1.6. Vì sao áp dụng HA lại quan trọng trong hệ thống:
    Hệ thống HA thường là những hệ thống ảnh hưởng và tác động sâu rộng với đời sống của con người về những mặt như sức khỏe, kinh tế và phúc lợi xã hội và tiếp tế thực phẩm,.... nếu vì một nguyên nhân nào đó khiến các hệ thống trên giảm hiệu suất hoạt động thì doanh nghiệp và cuộc sống của người dân sẽ gặp rất nhiều khó khăn.

1.7.1.7. HA được đo lường và đánh giá như thế nào? 
    Tính sẵn sàng của một hệ thống được đo tương ứng khi hệ thống đó không bao giờ bị lỗi và hoạt động 100%. Tỉ lệ % sẵn sàng được tính bằng công thức: Tính sẵn sàng = (Số phút tính trong một tháng - số phút ngừng hoạt động) * 100 / Phút trong một tháng. Dưới đây là các loại số liệu được dùng để đo tính sẵn sàng:
    
    - Thời gian trung bình giữa các lần hỏng hóc ( - MTBF): Tức là trong một hệ thống khoảng thời gian giữa hai lần xảy ra sự cố là bao lâu.
    - Thời gian chết trung bình (MDT): Tức là thời gian trung bình trong tình huống hệ thống ngừng phản hồi
    - Mục tiêu thời gian phục hồi (RTO): Đây là khoảng thời gian dự kiến được dành để phục hồi hệ thống sau sự cố. 

    Các hệ thống nội bộ hoặc nhà cung cấp dịch vụ sẽ sử dụng những số liệu nói trên để thực hiện cam kết với khác hàng như trong thỏa thuận mức độ dịch vụ (SLA). SLA là các hợp đồng trong đó nhà cung cấp dịch vụ đưa ra tỉ lệ phần trăm sẵn sàng của hệ thống cho khách hàng tham khảo.

1.7.1.8. Làm thế nào để hệ thống được coi là đạt được HA?
    Tính sẵn sàng cao được coi là đạt được nếu thực hiện các bước sau:
    - Thiết kế hệ thống HA đơn giản, chi phí thấp và tuân thủ đầy đủ các quy ước. Cần hạn chế các điểm lỗi và tốt nhất là có chính sách dự phòng khi cần thiết.
    - Xác ddinhj được mức độ sẵn sàng mà hệ thống có thể đáp ứng và chỉ số để áp dụng mức độ đo lường đó.
    - Triển khai phần cứng một cách linh hoạt, hiệu quả và chất lượng.
    - Đảm bảo hệ thống chuyển sang hệ thống dự phòng luôn trong trạng thái sẵn sàng để khi xảy ra lỗi có thể thay thế hoặc tiến hành tiếp quản nhanh chóng.
    - Sử đụg số liệu và quan sát để theo đõi hiệu suất của hệ thống, nếu có bất kì vấn đề bất thường trong khi vận hành có thể điều chỉnh cho phù hợp.

    Tìm cách cải thiện hệ thống dựa trên những dữ liệu đã quan sát, thu nạp được để đảm bảo hệ thống luôn phát triển và đáp ứng tốt trong mọi điều kiện.

1.8. Các thiết bị truyền dẫn trong mạng: Có 2 kiểu truyền dẫn trong mạng: 
Kiểu 1: Đơn công (simplex): trong kiểu truyền dẫn này, thiết bị phát tín hiệu và thiết bị nhận tín hiệu được phân biệt rõ ràng, thiết bị phát chỉ dảm nhiệm vai trò phát tín hiệu, thiết bị thu chỉ dảm nhận vai trò nhận tín hiệu. Truyền hình là một ví dụ của kiểu truyền dẫn này. 
Kiểu 2: Bán song công (Half - Duplex): ttrong kiểu truyền dẫn nayfy, thiết bị có thể là thiết bị phát, có thể vừa là thiết bị thu. Tuy nhiên,, tại một thời diểm thì chỉ có thể ở một trạng thái (phát hoặc thu). Bộ dđàm là thiết bị điển hình cho kiểu truyền dẫn này.
Kiểu 3: Song công (Full - Duplex): Trong kiểu truyền dẫn này, tại cùng một thời điểm, thiết bị vừa có thể là thiiết bị phát vừa có thể là thiết bị thu. Điện thoại di động là một ví dụ điển hình cho kiểu truyền dẫn này.
Nghiên cứu một số các loại thiết bị truyền dẫn trong mạng ở công ty cho phép sinh viên có cái nhìn tổng quan hơn về các thiết bị này. 

Một vài thiết bị truyền dẫn trong mạng
1.8.1. Converter

2. An toàn mạng trong doanh nghiệp.


2.1. Vấn đề an toàn mạng trong doanh nghiệp.

2.2. Các công nghệ được sử dụng.

3. Nghiên cứu hệ thống mạng doanh nghiệp.

3.1. Kiến trúc mạng của doanh nghiệp.

3.2. Kiến trúc phù hợp với tình hình và nhu cầu của doanh nghiệp.

3.3. Các công nghệ được tiếp xúc trong thời gian thực tập
3.3.1. GNS3
3.3.1.1. Giới thiệu về GNS3

3.3.2. Giám sát quản lý hệ thống mạng 24/7: Solarwin

3.3.3 Phần mềm bổ trợ quản lý hệ thống: PmP 

4. Hướng giải quyết của doanh nghiệp.

4.1. Giải pháp kiểm soát mạng an toàn.

4.2. Chính sách quản lý hệ thống mạng
4.2.1. PHân chia phòng/ban trong mạng quản trị dữ liệu
4.2.2. Gateway trong từng phòng ban 
4.2.3. CHính sách kết nối từ hệ thống ra bên ngoài Internet
4.2.4. CHính sách kết nối từ Internet vào trong hệ thống mạng 
4.2.5. Chính sách định danh người dùng trong hệ thống
4.2.6. Quản trị hệ thống và quản trị cấu hình mạng
4.2.7. Các giao thức được sử dụng
5. Công nghệ được sử dụng

5.1. Công nghệ theo dõi và báo lỗi hệ thống mạng

5.2. Đảm bảo hệ thống luôn vận hành ổn định - High Availability (HA)

# Chương 3. Kinh nghiệm tại vị trí thực tập 
1. Kinh nghiệm thực tế
1.1.
    
2. Kĩ năng học được trong quá trình thực tập

# Chương 4. Tài liệu tham khảo
[1]. Báo cáo tình hình ATTT (6 tháng đầu năm 2024) - VNPT Cyber Immunity.
[2]. 
[3].
[4].
[5].

