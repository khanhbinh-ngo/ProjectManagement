# Tìm hiểu chung về IPv6 
## 1. Lý thuyết
v6 chỉ còn đợi v4 hết só lượng là có thê phân phói cho người dùng thì có thể thay thế đuộc iPv4 
Tuy nhiên, chúng ta cần phải biết một số thứ như thế này:
a. lý do cần thiết của IPv6:
- dưới sự ra đời của n thiết bị IooT trên toàn thế giới thì v4 không đáp ứng được yêu cầu của thiết bị
- Số lượng nhiều
b. Cấu trúc của v6:
- với v4 ta sử dụng khái niện subnetmask, nhưng với v6 thì ta sử dụng prefix là chính (- số bit của phần mạng)

nó được chia thành 2 phần là [phần network] và [phần host]
Cấu trúc gòm cố những phần sau:
    Global routing prefix (GRP)
    Subnet
    Interface IP
Tổng cộng ta có 128 bit (có các lưu ý sẽ được tính toán sau)
Từ đó ta có thê rđưa a dduwodjc cái công thức của nó như sau;
network + host = grp + subnet + Interface ID
Tất nhiên lưu ý là ta có host tương đương với inteface id: giá trị được đặt cụ thể cho thiết bị như của bên . Có thể thay đổi được giá trị. 
như thế, ta thấy được rằng phần network sẽ là 2 phần còn lại  : GRP và subnet 
    phần grp là phần khonog được phép thay đỏi , trong khi đó phần network có thể thay đôi rnhuw mộ hình cần có 4 đến 5 lớp mạng với mỗi lớp có từ 5 đến 600 IP





Tao chưa có tải phần gnss3 vm (tức là t phải ngồi cài lại từ đầu) 
