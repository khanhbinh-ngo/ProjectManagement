# Tổng quann về lập trình hướng đối tượng

- Nói chung thì lập trình hướng đối tượng nhằm chuyên biệt hóa các vấn đề trong lập trình
- Nó là nền tảng của các design pattern hiện nay

# Cơ bản về lập trình hướng đối tượng
## Mục tiêu:
- Nhằm giúp đảm bảo được code có thể tái sử dụng
- Dễ đọc dễ nhìn dễ hiểu

## Một vài cái hàm cần (hoặc gọi là bắt buộc phải có trong một lớp)

**Hàm khởi tạo**: Constructor - có nhiệm vụ thiết lập thông tin ban đầu cho một đối tượng trong một lớp ngay khi đối tượng được khai báo
- Đặc điểm của phương thức khởi tạo:
    - Tên của phương thức chính là tên của lớp 
    - Phương thức thiết lập không có biến trả về
    - Trong một lớp có thể có nhiều phương thức khởi tạo khác nhau
- Một đối tượng chỉ có một lần khởi tạo ngay lúc ban đầu mà thoi. Đó chinnhs là khi đối tượng được khởi tạo

- Có thể phân chia hàm khởi tạo thành 3 kiểu khác nha
    - hàm tạo mặc định (default setting constructor):= Các thông tin đầu vào được quy định mặc định, ko do lập trình viên quy định
    - hàm tạo sao chép (copy constructor):= tham số đầu vào của đối tượng là tham số đầu vào của một đối tượng cùng một lớp. Các thông tin ban đầu của đối tượng B mới sẽ giống như đối tượng A được lấy làm tham số ban đầu.
    
    - hàm tạo có tham số 
# Cơ bản về lớp và đối tượng 
- Lớp là sự trừu tượng hóa của đối tượng. Những đứa nào đó có đặc tính tượng tượng nhau sẽ được tập hợp lại thành 1 lớp. 
- Mỗi đối tượng là một thực thể của một lớp

Ví dụ có lớp điện thoại, Ta có:
Điện thoại:
{
    + Thuộc tính: Màu sắc, hình dáng, kích thước màn hình, thời lượng pin
    + Phương thức: Gọi điện thoại, lướt web, chụp ảnh, nhắn tin ...  
}

+ Đối tượng của lớp này: Iphone, Samsung, Oppo ...

## 4 Tình chất của lập trình hướng đối tượng
- Một đối tượng gồm có 2 thành phần chính:
    - Thuộc tính (attributes): là những thông tin và đặc điểm của đối tượng

    - Phương thức (Methods): là những hành vi và các hành động của đối tượng

### Tính kế thừa: (Inheritance)
Đây là tính chất được sử dụng rất nhiều, nó cho phép xây dựng một lớp mới (lớp con), và kế thừa từ lớp cha các thuộc tính, tính chất và đã có những thuộc tính và tính chất của riêng lớp đó 
Các lớp con kế thừa toàn bộ thành phần của lớp cha và không cần phải định nghĩa lại. 
Lớp con có thể bổ sung và mở rộng và các thành phần khác, mới hơn và lớp cha không có.
(Bắt buộc phải nhắm đến tất cả các ván đề có trong lớp cha - lớp cơ bản và cung cấp cái nhìn tổng quan của cả dự án để kế thừa)

### Tính đa hình (Polymorphism)
Tính chất này cho phép các đối tượng khác nhau thực thi những chức năng giống nhau với các công tác thực hiện khác nhau (tùy thuộc vào đối tượng đó)
Ví dụ như là với một cái lớp smartphone có lớp con là Iphone và Samsung và có thuộc tính hệ điều hành
Nhưng hệ điều hành thì khác nhau là IOS và Android (hai hệ điều hành này khác nhau) 
### Tính đóng gói: (Encapsulation)

Cho phép chúng che dấu thông tin và những tính chất xử lý bên trong của đối tượng. Các đối tượng khác không thể tác động trực tiếp đến với tính chất xử lý bên trong của đối tượng. Các đối tượng khác cần thiết tham gia vào thay đổi trạng thái của đối tượng bắt buộc phải tham chiếu đến với các phương thức công khai do đối tượng đó cung cấp.

Tính chất này giúp tăng tính bảo mật của đối tượng và tránh tình trạng dữ liệu bị hư hỏng ngoài ý muốn.
### Tính trừu tượng: (Abstraction)
Này loại bỏ hết tất cả các thứ, các vấn đề vân vân để tâp trung vào những cái cốt lõi nhất

THuộc tính tổng quan và cơ bản của lớp là gioonngs nhau, nhưng thuộc tính khác nhau thì từng đối tượng sẽ có những thuộc tính khác nhau (sẽ được cá thể hóa từng đối tượng).

## Nghiên cứu về con trỏ


# Thao tác với đối tượng 
Trong lập trình có các thành phần cơ bản:
- Khai báo lớp 
    - Lớp gồm 2 thành phần
        - THuộc tính (private - public)
        - phương thức (private - public)
- Có thể thay đổi thông tin của từng đối tượng 1 (tính đa hình)
- Thay đổi phương thức của từng đối tượng 1
- Các đối tượng có thể có các thuộc tính và phương thức riêng

## Đối tượng là thành phần thuộc lớp
Nói chung thao tác là có một đối tượng thuộc một lớp khác như thế này:

``` 
class Engine {
    public:
        void start(){
            std::count << "Engine started";
        }
    // this is the method of class Engine
}; 

class Car {
    private:
        Engine engine;
        // Create an object belongs to class Engine
    
    public:
        void startCar(){
            engine.start();
            // call back to the engine's method (to start the car)
        }
}

```
**Note** khi đối tượng chứa lớp bị hủy, các thành phần đối tượng cũng bị hủy theo (tức là với car bị hủy thì cái bên trong cũng bị hủy theo, không ảnh hưởng đến vấn đề của cái lớp bên trong)
- khi một đối tượng Car được khởi tạo thì một đối tượng Engine cugnx được khởi tạo theo, khi đối tượng Car bị hủy thì đối tượng Engine trong đối tượng Car cũng theo đó mà hủy luôn

## Đối tượng là thành phần thuộc bảng
## Đối tượng là thành phần được cấp phát động

**note**
- Đối với 2 cái cách còn lại vẫn được sử dụng thoải mái, không phải lo về vấn đề linh tinh nào khác cả
- Tùy vào ngữ cảnh mà gọi đối tượng như thế nào cho phải và chio hợp lý 

# Các hàm
## Hàm bạn 
- Hàm bạn (Friend function) là một vài hàm cho phép có thể truy cập vào các thành phần thuộc tính riêng tu và được bảo vệ của một lớp mà trong đó chủ thể gọi hàm không phải là một thành phần trong lớp đó (Được sử dụng khi cần một hàm có quyền truy cập vào các thành phiên dữ liệu của lớp nhưng không muốn đưa nó vào như một phương thức của một lớp)

## Lớp bạn
- Lớp bạn nói chung giống như hàm bạn, nó được coi là mỗi thành viên của lớp a có thể truy cập vào các thành iveen của lớp b, nếu 2 lớp này có quan hệ mật thiết với nhau và đảm bảo cần phải làm như thế (vì nếu để lớp bạn nhiều sẽ dẫn đến mất an toàn thông tin của lớp )
## Một số nguyên tắc xây dựng lớp
> Được tổng hợp từ một vài nguồn không uy tín lắm á

- Tổng quan là phải đảm bảo được code dễ review, dễ bảo trì, dễ mở rộng và tính ổn định cao

### Tính đóng gói (Encapsulation)
- Sử dụng thuần thục dữa private và protected cũng như 
- public thì sử dụng getter và setter

### Tính kế thừa (Inheritance)
- Tái sử dụng từ các lớp có sẵn, các lớp base và đảm bảo 1 điểm lỗi
- Thiết lập mối quan hệ phân cấp giữa các lớp

### Tính đa hình (Polymorphist)
- Cố gắng sử đa dạng các phương thức trong đa dạng các ngữ cảnh mà phương thức đó được gọi tới

### Nguyên tắc trách nhiệm duy nhất (Single Responsibility Principle - SRP)
- Đây được hiểu là mỗi lớp chỉ nên có một lý do duy nhất để thay đổi, tức là chỉ nên có một nhiệm vụ hoặc chức năng cụ thể, trong mọi tình huống việc thay đổi chức năng chính của một lớp không bị ràng buộc với chức năng của lớp khác. 

### Nguyên tắc đóng - mở (Open/ Close Principle - OCP)
- NGuyên tắc này đòi hỏi phải hiểu được một điều đó chính là các lớp nên đóng lại việc sửa đổi và để mở cho việc mở rộng
- Tức là trên lý thuyết, các lớp không nên bị sửa đổi mã nguồn gốc quá nhiều, khuyenes khích sử dụng tính đa hình và kế thừa để có thể mở rộng chức năng của lớp (tất nhiên không cần thiết phải sửa đổi mã nguồn một cách nhiều lần là điều kiện tiên quyết)

### Nguyên tắc tách giao diện (Interface Segresgation Principle - ISP)
- NGuyên tắc này đối phó với việc một lớp không nên triển khai với những giao diện không cần thiết.
- Kiểu như có thể không cần và không phải triển khai với các giao diện không cần thiết nhằm giảm thiểu tối đa các giao diện không cần thiết cùng với giảm độ phức tạp trong triển khai một thành phần trong lúc code 
- Nói chung cách thức thực hiện đó là thiết kế các interface nhỏ gọn, mỗi giao diện chỉ có các phương thức hoặc một nhóm chức năng cụ thể
