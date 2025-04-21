
# How to install / Hướng dẫn cài đặt

Trước tiên, máy đã phải cài [Python](https://www.python.org/downloads/) (ít nhất từ bản 3.12 trở lên hoặc bản mới nhất)
=> Note: Nhớ bật chế độ "Add python to PATH environment", tránh phiền phức sau này!

Sau khi cài đặt xong python, mở `Command Prompt/Terminal` ngay thư mục gốc của project **demo_web**:
### Setup môi trường ảo (virtual environment)
> Đọc thêm tại [đây](https://flask.palletsprojects.com/en/stable/installation/#virtual-environments)

* Mở *Powershell* ngay thư mục gốc **demo_web** của project và chạy lệnh sau:
```
py -3 -m venv .venv
```

* Mở file `powershell-cmd.txt` và dán lệnh đó vào *Powershell*
* Folder `.venv` được tạo là thành công!

### Cài đặt thư viện (packages)

Tiến hành dán câu lệnh cài đặt dưới đây để tiến hành cái các thư viện:
```
pip install flask flask_sqlalchemy flask_bcrypt flask_cors flask_jwt_extended psycopg2-binary
```
hoặc:
```
pip install -r requirements.txt
```

### Sử dụng project
Tiến hành chạy app thông qua lệnh:
```
python run.py
```
Nếu trên *Powershell* trả như này là thành công:
```
(.venv) C:\....>python run.py
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 ```
URL của project sẽ nằm ở dòng `Running on`, phía sau đó là url để test

# Cấu trúc project
```
demo_web/                               # Thư mục gốc
│── app/                                # Thư mục của API
│   ├── controllers/                    # Thư mục xử lý logic
│   │   ├── user.py
│   ├── models/                         # Thư mục model cho cơ sở dữ liệu (db)
|   |   ├── user.py
│   ├── views/                          # Thư mục để hiển thị giao diện
|   |   ├── user.py
|   |── static/                         # Thư mục tài nguyên của FE (UI)
|   |── templates/                      # File html của FE
│   ├── config.py                       # File chứa cấu hình
│   ├── __init__.py                     # File khởi tạo
│── instance (xuất hiện khi chạy - database.db)
|── Procfile                            # Cáu hình khởi chạy trên Cloud (Heroku)
|── requirements.txt                    # File chứa thông tin các package/lib
│── run.py                              # File khởi chạy dự án
```
# Environment Variables / Biến môi trường

Cấu hình hiện tại của project nằm ở file `config.py`:

`SQLALCHEMY_DATABASE_URI`: Đường dẫn cơ sở dữ liệu (sqlite)

`JWT_SECRET_KEY`: Khóa bí mật cho xác thực JWT


# API Reference
Xem thêm tại [POSTMAN](https://www.postman.com/chriswalkerkun/workspace/chriswalkerkun/collection/42576408-b7960f71-3b59-4b77-9d95-531aacdacd16?action=share&creator=42576408)

### Register / Đăng ký

```http
  POST /api/auth/register
```

BODY:
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `string` | **Bắt buộc**. Tên đầy đủ |
| `email` | `string` | **Bắt buộc**. Email |
| `phoneNumber` | `string` | **Bắt buộc**. Số điện thoại |
| `address` | `string` | **Bắt buộc**. Địa chỉ |
| `type` | `string` | **Bắt buộc**. Thể loại |
| `password` | `string` | **Bắt buộc**. Mật khẩu |
| `role` | `string` | **Bắt buộc**. Vai trò |

### Login / Đăng nhập

```http
  POST /api/auth/login
```

BODY:
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `email` | `string` | **Bắt buộc**. Email |
| `password` | `string` | **Bắt buộc**. Mật khẩu |

RETURN/Trả về:
* `access_token`: Xác thực người dùng (Lưu ở localStorage)

### Profile / Thông tin người dùng

```http
  GET /api/auth/profile
```

HEADER:
| Key | Value     |
| :-------- | :------- |
| `Authorization` | `Bearer <access_token>` |

RETURN/Trả về: Thông tin người dùng


## Dev

- Xuân Trường
- [@kiyoshikuncool](https://www.github.com/kiyoshikuncool)