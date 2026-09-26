"""Giao diện Streamlit cho Bài 8."""

import requests
import streamlit as st


API_URL = "http://localhost:8000"

st.set_page_config(page_title="Thời tiết", page_icon="🌦️")
st.title("🌦️ Tra cứu thời tiết")
st.write("Nhập tên thành phố để xem thời tiết hiện tại.")

city = st.text_input("Tên thành phố", placeholder="Ví dụ: Hanoi")

if st.button("Xem thời tiết", type="primary"):
    if not city.strip():
        st.warning("Em hãy nhập tên thành phố.")
    else:
        try:
            # TODO 5/5: Gửi GET request tới /weather, truyền city bằng params và timeout=10.
            response = requests.get(f'{API_URL}/weather',params={'city':city.strip()},timeout=10)

            if response is not None and response.status_code == 200:
                data = response.json()
                st.success(data["city"])
                col1, col2 = st.columns(2)
                col1.metric("Nhiệt độ", f"{data['temp']} °C")
                col2.metric("Độ ẩm", f"{data['humidity']} %")
                st.write(data["description"].capitalize())
                icon_url = f"https://openweathermap.org/img/wn/{data['icon']}@2x.png"
                st.image(icon_url, width=100)
            else:
                st.error("Không tìm thấy thành phố.")
        except requests.RequestException:
            st.error("Không kết nối được tới backend. Em hãy kiểm tra cửa sổ chạy FastAPI.")

