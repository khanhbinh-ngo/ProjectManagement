Hành trình vạn dặm luôn bắt đầu từ những bước chân nhỏ bé


Those are notes for business statistics (good) - Lý do nên đọc quyển sách này: ta có thể tìm hiểu được thị trường và có hướng đi phát triển trong lĩnh vực kinh doanh. Đây là một số vấn đề mà sách đề ra
    1/ hiểu biết về công cụ thống kê trong kinh doanh: đây là một công cụ quan trọng trong việc đưa ra quyết định dựa trên dữ liệu. Sẽ giúp nắm vững các phương pháp thống kê cơ bản và nâng cao, từ đố có thể áp dụng vào việc phân tích dữ liệu kinh doanh thực tế. 
    
    2/ nâng cao các kĩ năng ra quyết định: Sẽ có những phương pháp giúp phân tích dữ liệu và xác định các xu hướng, từ đó mà có thể đưa ra quyết định chiến lược một cách chính xác hơn. Đây là kĩ năng quan trọng trong bất kì vị trí nào có liên quan đến quản lý, marketing và tất cả các ngành kahcs.

    3/ Chiaanr bị cho các vai trò chuyên môn trong tương laai: Với các kiến thức được cung cấp, ta có lợi thế khi ứng tuyển vào vị trí có
    liên quan đến phân tích dữ liệu, nghiên cứu thị trường các thứ. 

    4/ Phát triển tư duy phân tích và tư duy logic: Điều nầy đưa ra các vấn đề cốt lõi trong việc giải quyết các tình huống cụ thể, đưa ra lập luận chặt chẽ và kiểm tra giả thiết trong tương lai.
    Từ đó mở ra được nhiều hướng đi mới trong và ngoài qá trình kinh doanh



Một vài vấn đề muốn lưu ý:
    1. // Chỉ cần thay mỗi môn trên một hàng cho biến monDangKy này là xong
// Lưu ý: Nếu sau này trường update website, các thẻ query không còn đúng nữa, thì bạn liên hệ messenger.com/t/loia5tqd001 để báo mình nhé

var monDangKy = `
EC222.P11
NT121.P11.1
NT402.P11.1
NT405.P11.1
NT538.P11.1
NT121.P11
NT402.P11
NT405.P11
NT538.P11
`;

var successLog = (message) => console.log('%c' + message, 'font-weight:bold; color:green;');
var errorLog = (message) => console.log('%c' + message, 'font-weight:bold; color:red;');

DangKy(monDangKy);

function DangKy(monDangKyString) {
  try {
    var listMonDangKy = monDangKyString.trim().split('\n').map((it) => it.trim())
    
    var allRows = [...document.querySelectorAll('form table tr')]

    var rowsToDangKy = allRows.filter((it) => listMonDangKy.includes(it.querySelector('td:nth-child(2)')?.textContent?.trim()))
    
    rowsToDangKy.forEach((it, index) => {
      imt.querySelector('td:first-child input[type="checkbox"]').click();
      var tenLop = it.querySelector('td:nth-child(2)')?.textContent?.trim();
      successLog(index + 1 + '.Đã chọn lớp ' + tenLop);
    })
  } catch {
    errorLog('Chọn lớp không thành công! Bạn tự chọn lớp đi nhé!');
  }
}

Xác định được một vài vấn đề sau:
1. Các hướng đi và vấn đề để có thể phát triển ĐACN và KLTN cũng như em muốn phát triển thêm các kĩ năng việc làm về sau, nên có thể sử dụng 2 môn này làm bệ phóng đấy ạ, nên các hướng giải quyết các vấn d
2. Các điều kiện tiên quyết để có kết quả tốt trong việc triển khai ĐACN và KLTN


Một vài vấn đề cần được thầy giải đáp

1. Trong kì này thì em sẽ tổng kết các môn học khác để kì sau tập trung vào phần làm đồ án chuyên ngành và khóa luận tốt nghiệp. 
2. Em muốn thực hiện đồ án chuyên ngành và từ đồ án chuyên ngành phát triển lên thành khóa luận tốt nghiệp trong học kì này và báo cáo trong học kì tới. Hiện tại thì em vẫn chưa xác định được hướng đi trong tương lai. Em mong muốn thầy có thể gợi ý một vài hướng đi và tìm hiểu các hướng đi đấy như thế nào cho hiệu quả. 
3. 
