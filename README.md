# Bài 8 — App tra cứu thời tiết

## Mục tiêu LAB

Trong bài này, em tạo một ứng dụng nhỏ gồm:

- FastAPI nhận tên thành phố và gọi OpenWeatherMap.
- Streamlit gửi yêu cầu đến FastAPI và hiển thị nhiệt độ, độ ẩm.
- Năm vị trí `TODO` ngắn để hoàn thiện trong giờ học.

Luồng dữ liệu:

```text
Người dùng → Streamlit → FastAPI → OpenWeatherMap
```

## 1. Chuẩn bị

- Cài Python 3.11 hoặc mới hơn.
- Tạo tài khoản và API key tại <https://openweathermap.org/api>.
- Mở Terminal tại thư mục `Bai8`.

## 2. Tạo môi trường ảo

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## 3. Điền API key

Sao chép `.env.example` thành `.env`, rồi thay phần bên phải dấu `=`:

```env
OPENWEATHER_API_KEY=api_key_that_cua_em
```

Không đưa file `.env` lên GitHub và không gửi API key cho người khác.

## 4. Hoàn thành bài

Mở lần lượt:

1. `backend/main.py`: hoàn thành vị trí 1 đến 4.
2. `frontend/app.py`: hoàn thành vị trí 5.

Gợi ý: `requests.get()` nhận địa chỉ ở đối số đầu tiên; các tham số thường dùng trong bài là `params=...` và `timeout=10`.

## 5. Chạy ứng dụng

Mở hai Terminal, đều đứng tại thư mục `Bai8` và đã kích hoạt `.venv`.

Terminal 1 — backend:

```powershell
python -m uvicorn backend.main:app --reload
```

Kiểm tra <http://localhost:8000/docs>, thử endpoint `GET /weather` với `city=Hanoi`.

Terminal 2 — frontend:

```powershell
python -m streamlit run frontend/app.py
```

Mở địa chỉ Streamlit hiện trên Terminal, nhập `Hanoi`, `Hue` hoặc `Da Nang`.

## Hoàn thành khi

- Trang `/docs` trả về dữ liệu thời tiết của một thành phố.
- Giao diện hiện đúng tên, nhiệt độ, độ ẩm và mô tả.
- Thành phố không tồn tại được báo lỗi thay vì làm ứng dụng dừng.

## Yêu cầu nộp bài

Repository đã được **fork** vào tài khoản GitHub của em và **clone** về máy từ đầu buổi học. Vì vậy, em không chạy `git init` và không tạo repository mới.

1. Mở Terminal tại thư mục repository đã clone và kiểm tra remote:

   ```powershell
   git remote -v
   ```

   Địa chỉ `origin` phải là repository trong tài khoản GitHub của em.

2. Kiểm tra các file đã thay đổi:

   ```powershell
   git status
   ```

   Đảm bảo `.env`, `.venv` và các file chứa API key không xuất hiện trong danh sách chuẩn bị commit.

3. Thêm bài làm và tạo commit:

   ```powershell
   git add .
   git status
   git commit -m "Hoan thanh Bai 8"
   ```

4. Đẩy nhánh hiện tại lên repository đã fork:

   ```powershell
   git push origin HEAD
   ```

5. Mở repository của em trên GitHub, kiểm tra các file đã được cập nhật rồi nộp:

   - Đường dẫn repository GitHub đã fork.
   - Đường dẫn commit mới nhất của bài làm.
   - Ảnh chụp giao diện tra cứu thời tiết chạy thành công.

Không nộp API key, file `.env` hoặc thư mục `.venv`.
