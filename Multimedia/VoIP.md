# I. Definition
- VoID (Voice over Internet protocol) prefer to receive or transfer a voice data in real time by internet protocol

# II. VoID services

## VoID structures 
- Call Server / Server
- Gateway
- IP phones or softphone 
- Non VoIP components 
- Some other protocols 
- Structures: IP something we could maintain occationally


- perfomance or Hiệu suất
    + Mỗi thành phần đều ảnh hưởng đến hiệu suất chung.
    + vấn đề với mỗi lần nhận gửi gói tin -> thế nên tôi phải đưa ra một phương án là dùng một bộ đệm để có thể maintain được (đảm bảo realtime)
    + vấn đề mất gói tin: tùy vào chất lượng đường truyền để có thể cover được yêu cầu của mỗi cuộc gọi.

- Các hoạt động cơ bản của một phiên làm việc của VoIP 
1. Digitalization: lấy mẫu đồ  
2. Compression: nén gói tin lại
3. Packetization/Encapsulation: Đóng gói mấy cái gói tin vào trong
4. IP network transmission: truyền tải quâ mạng
5. Decapsulation: Mở gói tin đồ đàng hoàng
6. Decompression: giải nén các gói tin đã được mở
7. Digital to analog: chuyển đổi số sang analog



## Do we have some trouble with that shit?
- yeah, so how do we support with all the thing like that? 
- Basically, we confuse about DHCP and TFTP 
- Next step, we could set up our phone with 2 small step:
    + Phone registration
    + Phone setup
- call setup and connection
- RTP conversation
- Call termination

Let's have a closer view:
###     Dynamic host configuration protocol
- được dùng để cung cấp địa chỉ IP của TFTP cho VoID phone
kiểu ta sẽ đăng ký điện thoại
thiết lập điện thoại
thiết lập cuộc gọi và kết nối


### Các giao thức có trogn VoID
- SIP (section initiation protocol)
GỒM CÓ CÁC KIỂU SAU:
a. mục đích: giao thức báo hiệu, quản lý và điều phối các cuộc gọi
b. cơ chế hoạt ddoonjgL tương đồng với http và smtp 
- RTP (realtime transport protocoa): truyền theo thời gian thực
a. mục đích: giao thức truyền tải dữ liệu theo thời gian thực
b. cơ chế hoạt động: gán nhãn dữ liệu , đồng bộ theo thời gian (thông tin thoại hay gì đó)

- Dialplan
a. Context: ngữ cảnh - thuwognf đặt trong ngoặc vuuong
b. extension: exten đồ các thứ
c. priority: mức độ ưu tiêâ
d. Application: ứng dụng các thứ




# Advantage and Disadvantage 
- We move tho the next steps


# PSTN: public switch telephone network
- kiểu chuyển mạch di động sớm nhất trên thê giới và được deploy theo hướng mạch (circuit mode và dduwuojec kết nối theo phương thức scos hướng (connection oriented))
# POTS: Plain old telephone Service

## 3333333333333333333333333333333333333333333333333333333333333333333333333333333333333 ## 

Mục tiêu: triển khai một hệ thống thoại IP open source có khả năng:
    + gọi nội bộ
        + tạo và cấu hình các số nội bộ (extension) theo SIP và IAX2 như trên hình
            + phòng giám đốc: EXT 1061 (SIP) với mật khẩu là 123406
                + Rung chuông tối đa 15s. Sau đó tự động ngắt cuộc gọi điện thoại 
            + phòng bán hàng: EXT 1062 (IAX2)
                + Rung chuông tối đa 20s. Sau đó cho phép gửi hộp thư thoại
            + phòng nhân sự: EXT 1063 (SIP)
                + Rung chuông tối đa 10s. Sau đó tự ngắt cuộc gọi
            + Phòng kỹ thuật: EXT 1064 (IAX2)

    + gọi liên tổng đài
        + cấu hình cho phép các số EXT giữa 2 tổng đài có thể giao tiếp với nhau
    + Gọi thông qua số public
        + kiểu mỗi tổng đài có một số public (hotline cho nosd ễ hiểu) - người ngoài muốn gọi vào thì cần phải thông qua việc gọi vào số này mới được. 
            + Tổng đài A: 0952011060
            + TỔng đài B: 0951012060
    + cài đặt các tính nawg nâng cao cho thiết lập từ tổng đài như nhạc chờ, ghi âm hay gọi nhóm các thứ:
        + làm được đoạn trên thì làm đoạn dưới sau cũng được:
            a. Viết Dialplan đơn giản
                - Cấu hình cho EXT phòng giám đốc: Rung chuông 15s + tự tắt máy
                - Cấu hình EXT phòng bán hàng: Rung chuông 20s + gửi nhắn thoại + ngắt cuộc gọi
                - Cấu hình EXT phòng kỹ thuật: đợi 5s + phát câu "hello-world" + tự động ngắt cuộc họp
            b. gọi đến số public: phát đoạn âm thanh chào mừng "hello-customer" + đợi nhấn phím
                - Nhấn phím sẽ được thay đổi như sau (từ 1 đến 4):
                    1. phát đoạn âm thanh chào mừng đến phòng bán hàng
                    2. gọi đến phòng kỹ thuật
                    3. để lại lời nhắn cho phòng giám đốc
                    4. Ngắt cuộc gọi
            c. Họp nội bộ (meetme)
                - gọi đến 4064 khi cần họp toàn công ty
                - Password:
                    + QUản lý: 123456
                    + Gia nhập: 654321
                    