# HEAR ME OUT: WE ARE GOING TO LEARN ABOUT LAYOUT TODAY
## Types of standard layout
1. Framelayout
Đơn giản là một vùng layout nào đó để hiển thị nội dung cụ thể nào đó
Chứa trong nó là một thành phần view như là hình ảnh, một nút nhấn, một nhãn nào đó
- **Phần tử con mặc định được đặt ở góc bên trái cùng**
- **Các phần tử con sau được xếp chồng lên các phần tử con trước**
(layer được đánh dấu là trước sau theo thứ tự trong tập tin xml)

So, how we can do soemthing great for them at that point?



2. Linear layout
Layout này được sử dụng nhiều nhất khi ta muốn một thứ gì đó thật là bùng nổ - tất nhiên là trong khi làm ứng dụng rồi.
Nói đơn giản thì kiểu layout này cho phép chúng ta sắp xếp các phần tử trong nó theo dạng danh sách dọc hoặc danh sách ngang. Để chỉ linear này đang là sử dụng danh sách dọc hay danh sách ngang, ta sử dụng thuộc tính android:orientation, với 2 thuộc tính là 
    vertical (nằm dọc)
    Horizontal (nằm ngang)

Để các phẩn tử con nằm trong linear layout này có độ rộng tương đối với nhau thì ta sử dụng thuộc tính android:layout_weight

*ví dụ*: tạo ra 4 hàng và 4 cột có độ rộng bằng same same nhau trên một màn hình

Chúng ta có thể lồng 2 **linear layer** vào với nhau để tạo ra một giao diện phức tạp hơn

3. Table layout
Kết hợp với thẻ tableRow để tạo ra các hàng các cột cho layout. Cách sử dụng nó cũng khá là đơn giản:
Khi sử dụng, nó sẽ tạo ra các viền xung quanh các ô. Các ô có thể chứa nội dung bất kì thành phần view khác (có thể chứa cả các layout khác như là **linear layout** hoặc là **Frame layout** hoặc là một **Table layout** nào đó khác)
Mỗi thẻ **table layout** nằm trong thẻ **table layout** tạo ra một hàng. THẻ này sẽ thực sự chứa đựng một thành phần view khác

*Ví dụ:* Tạo ra một cái cửa sổ popup từ mấy cái này như thế nào nhỉ


4. Relative layout
Đây là loại layout cho phép chúng ta setup các thiết lập là các mối quan hệ giữa các thành phần con với nhau.
Nói cách khác, một thành phần con có thể được định vị vị trí của nó so với thành phần chứa nó hoặc các thành phần cạnh nó

*Ví dụ:* sử dụng một thuộc tính xml để canh một nút nhấn sang bên phải thành phần đang chứa nó

5. Constraint Layout
Đây là một layout mạnh, khuyến khích sử dụng vì nó có thể tạo các giao diện phức tạp, mềm dẻo (kiểu nó có thể hạn chế việc sử dụng nhiều layout lồng nhau gây mất cân đối cũng như phức tạp hóa về sau này).
Nói chung nó có thể định vị và sắp xếp các view lại với nhau, dựa trên sự ràng buộc của các **view cha** với **view con**: Tạo các ràng buộc giữa các view con (kiểu xích chúng lại với nhau hay dùng sự trợ giúp của Guideline )

## Exercisess
so, let's get started



# Android Project folder structure

We neeed to create a new project for each sample application and we should understand the folder structure, where it looks like that

The android project contains different types of app modules, source code files, we'll explore all the folders and files in the android app

> 1. Manifests Folder
> 2. Java Folder
> 3. res Folder
>> Drawable Folder
>> Layout Folder
>> Mipmap folder
>> Values Folder
> 4. Gradle Scripts

1. Manifests Folder [Example](#example-for-xml-file-from-manifests)

This folder contains AndroidManifest.xml for creating our android application.
This filee contains information about our application such as the android version, metadata, states package for Kotlin file, and other application components.
It acts as an intermediator between android OS and our application.

2. Java Folder
The java folder contains all the java and kotlin source code (.java) files that we create during the app development, include other Test files
If we create any new project using Kotlin, by default the class file MainActivity.kt file will create automatically under the package name 
"com.geeksforgeeks.myfirstkotlinapp" (somehow like change in name)

- We have here 2 files: MainaActivity.kt and MainActivity.java  
(Also, I coiuld find out some thign different from that stuff)

3. Resource (res) folder
This kind of folder is the most important folder because it contains all the non-code sources like images, xml layout, and UI strings for android application
(here I can smell like there are 4 types of files: 
**drawable:**
    This contains different types of images used for the development of the application
    We need to add all the image in a drawable folder for the application development

**layout:**
    This contains all xml layout files which we used to define the user interface of our application. It also contains *activity_main.xml* 
    Some how we can do [this](#example-for-xml-file-from-reslayout)
**values:**
**xml:**
)




### Example for .xml file from res/layout
<?xml version="1.0" encoding="uft-8?> 
<androidx.constraintlayout.widget.ConstraintLayout

    
>
</androidx.constraintlayout.widget.ConstraintLayout>


### Example For .xml file from Manifests
<?xml version="1.0" encoding="utf-8"?>
<manifests xmlms:android="http://schemas.android.com/apk/res/android"
package="com.geeksforgeeks.myapplication">
    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/AppTheme"
        > 
        <activity android:name=".MainActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category anroid:name="android.intent.category.LAUNCHER" /> 
            </intent-filter>
        </activity>
    </application>
</manifests>



