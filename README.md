<h1 align="center">------------ 🔥 LibraryManagementWeb 🔥------------</h1>

<h1>Table of contents 📖</h1>

<h2>
  <a href="#introduction">I. Giới thiệu chung</a>
  <br />
  <a href="#func">II. Các chức năng</a>
  <br />
  <a href="#dtb">III. Cơ sở dữ liệu</a>
  <br />
  <a href="#develop">IV. Hướng phát triển</a>
  <br />
</h2>
<br />

## I. Giới thiệu chung <a name="introduction"></a>
### 1. Thông tin nhóm
- Tên nhóm: **Web này hơi lớn 👀**
- Lớp: INT2211 24 - Cơ sở dữ liệu
- Tên web: LibraryManagementWeb
- Thành viên 💻

| Order |          Name          |     ID     |          Email          |
| :---: |:----------------------:|:----------:|:-----------------------:|
|   1   |  Nguyễn Thị Ngọc Minh  |  21020358  |   21020385@vnu.edu.vn   |
|   2   |    Đỗ Nhữ Hoàng Nam    |  21020126  |   21020126@vnu.edu.vn   |
|   3   |      Hồ Thu Giang      |  21020309  |   21020309@vnu.edu.vn   |

### 2. Thông tin web

<p align="center"> Có ai đó đã từng khẳng định rằng: “Sách hay, cũng như bạn tốt, ít và được chọn lựa; chọn lựa càng nhiều, thưởng thức càng nhiều”. Quả thật, sách đóng vai trò quan trọng trong cuộc sống. Chính vì vậy để khuyến khích mọi người đọc sách nhóm chúng em đã quyết định làm trang web quản lý thư viện này để giúp các bạn thuận lợi hơn trong việc mượn sách,mở mang tri thức. Thay vì phải tốn nhiều tiền để mua 1 quyển sách cùng lượng tiền ấy LibraryManagementWeb giúp người dùng có thể đọc được thêm nhiều cuốn sách hơn
</p>

<p align="center">
  <a href = "https://hnpyne.pythonanywhere.com/"> <b>LINK DEMO</b> </a>
</p>

<p align="center">
  <a href = "https://youtu.be/WyQgAgDhr_8"> <b>VIDEO DEMO (mở phụ đề)</b> </a>
</p>

>**FRAMEWORK 🖼️** 
>
<img src="https://user-images.githubusercontent.com/100185884/207886555-533dc8f7-b3fc-4b66-8ab4-e29b4747e7b8.png" width="30" height="25">  [Bootstrap](https://getbootstrap.com/)


<img src="https://user-images.githubusercontent.com/100185884/207887804-fcb47903-a37c-4bd7-855e-4116a3a5a3b8.png" width="25" height="25">  [Django](https://www.djangoproject.com/)


>**CÁC TRANG 📄** 
> 

- Home
- Login
- Signin
- Thông tin người dùng
- List sách
- Thông tin sách
- Kết quả tìm kiếm
- Nội dung sách
- Giỏ hàng

>**CÁCH SỬ DỤNG 🖱️** 
>

***Đối với user 👨***
- Đăng ký tài khoản
- Chọn sách
- Tham khảo những cuốn sách ở quầy trưng bày
- Tìm kiếm sách theo tên,thể loại,mô tả
- Thêm sách cần mượn vào giỏ
- Lên thư viện đọc thông tin và lấy sách cần mượn về

***Đối với người trực thư viện 📖***
- Đăng nhập vào tài khoản Admin được cấp
- Sửa đổi cuốn sách ở quầy trưng bày
- Cập nhật,sửa đổi thông tin người dùng
- Quản lý thông tin các nhà xuất bản,tác giả
- Cập nhật, thay đổi số lượng, thông tin sách
- Check yêu cầu mượn sách

## II. Các chức năng <a name="func"></a>
- Đăng ký
- Đăng nhập
- Tìm kiếm sách
- Quầy sách đề cử
- Thêm sách vào giỏ hàng
- Mượn sách

## III. Cơ sở dữ liệu <a name="dtb"></a>
### 1.Mô hình quan hệ
![image](https://user-images.githubusercontent.com/100185884/207914433-c30d1b2f-5c5b-4d21-8c1f-5bedee0d2d86.png)



### 2. Mô tả
- Cơ sở dữ liệu gồm 7 bảng

>**Bảng unserinformation**
>

Dùng để lưu những thông tin chi tiết của người dùng (Bảng này chưa thực sự được dùng tới trong web demo)

|     Khoá     |    Tên    |       Chức năng        |
|:------------:|:---------:|:----------------------:|
|  Khoá chính  |  user_id  |    id của người dùng   |
|  Khoá ngoại  |  user_id  |   tham chiếu đến user  |


>**Bảng user**
>

Lưu trữ username, password, email (thông tin trong phần register)


|     Khoá     |    Tên    |             Chức năng             |
|:------------:|:---------:|:---------------------------------:|
|  Khoá chính  |    id     |   id của user do CSDL tự tạo ra   |
|  Khoá ngoại  |           |                                   |


>**Bảng listbook_book**
>

Quản lý sách trong thư viện

|     Khoá     |    Tên     |                           Chức năng                       |
|:------------:|:----------:|:---------------------------------------------------------:|
|  Khoá chính  |    id      |                      Do CSDL tự tạo ra                    |
|  Khoá ngoại  |  genre_id  |       Tham chiếu đến bảng category, là thể loại sách      |
|              |publisher_id|  Tham chiếu đến bảng publisher đóng vai trò nhà xuất bản  |

>**Bảng listbook_category và Bảng listbook_publisher**
>

Các bảng quản các thể loại và nhà xuất bản của thư viện

>**Bảng user_cart_cart**
>

Quản lý giỏ hàng của từng user

|     Khoá     |    Tên     |                           Chức năng                       |
|:------------:|:----------:|:---------------------------------------------------------:|
|  Khoá chính  |    id      |                      Do CSDL tự tạo ra                    |
|  Khoá ngoại  | user_id_id |                  Tham chiếu đến bảng user                 |

>**Bảng user_cart_item**
>

Quản lý mỗi sản phẩm đã có trong giỏ hàng

|     Khoá     |    Tên     |                           Chức năng                       |
|:------------:|:----------:|:---------------------------------------------------------:|
|  Khoá chính  |    id      |                      Do CSDL tự tạo ra                    |
|  Khoá ngoại  |   book_id  |                    Tham chiếu tới book                    |
|              |    cart    |                  Tham chiếu đến bảng cart                 |

## IV. Hướng phát triển <a name="develop"></a>
- Thêm trang các sách đã mượn
- Đánh giá và bình luận của người dùng với sách
- Cho phép người dùng tự thay đổi thông tin cá nhân
- Thêm top những cuốn sách được nhiều lượt đặt mua nhất
- Phát triển thêm về đặt sách và thanh toán online có tiền cọc số lượng ngày thuê và được nhận trả sách tại nhà
