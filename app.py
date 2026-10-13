import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# 1. Hiển thị tiêu đề ứng dụng (Yêu cầu đầu tiên)
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")
# 2. Tạo DataFrame chứa thông tin 10 sinh viên
data = {
    "Họ và tên": [
        "Nguyễn Hải Long",
        "Phạm Nguyễn Hoàng Hải",
        "Phạm Thành Đạt",
        "Nguyễn Tiến Đạt",
        "Lê Viết Hoàng",
        "Đào Thị Vân Anh",
        "Trương Yến Bảo Nhi",
        "Nguyễn Duy Minh Phương",
        "Lưu Thị Thanh Thảo",
        "Lê Quỳnh Anh"],
    "Điểm chuyên cần": [10.0, 8.0, 7.0, 9.0, 8.5, 10.0, 9.0, 5.0, 8.0, 7.5],
    "Điểm giữa kỳ":   [8.0, 7.5, 9.0, 6.5, 8.0, 5.5, 7.0, 4.5, 6.5, 8.0],
    "Điểm cuối kỳ":   [8.5, 8.0, 9.5, 6.0, 7.5, 4.5, 7.0, 4.0, 7.0, 8.5]}

df = pd.DataFrame(data)
display(df)

# 3. Tính điểm tổng kết
df["Tong_ket"] = (
    0.2 * df["Điểm chuyên cần"]
    + 0.3 * df["Điểm giữa kỳ"]
    + 0.5 * df["Điểm cuối kỳ"]
).round(2)

display(df)

# 4. Xếp loại sinh viên
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7.0:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

display(df)
import ipywidgets as widgets
from IPython.display import display, clear_output

# 5. Tạo danh sách xổ xuống chọn sinh viên
selectbox = widgets.Dropdown(
    options=df["Họ và tên"].tolist(),
    description="Sinh viên:",
    style={"description_width": "initial"},
    layout=widgets.Layout(width="400px"))
output = widgets.Output()
def hien_thi_sinh_vien(change=None):
    with output:
        clear_output(wait=True)
        sv = df[df["Họ và tên"] == selectbox.value].iloc[0]
        print("===== THÔNG TIN SINH VIÊN =====")
        print("Họ và tên:", sv["Họ và tên"])
        print("Điểm chuyên cần:", sv["Điểm chuyên cần"])
        print("Điểm giữa kỳ:", sv["Điểm giữa kỳ"])
        print("Điểm cuối kỳ:", sv["Điểm cuối kỳ"])
        print("Điểm tổng kết:", sv["Tong_ket"])
        print("Xếp loại:", sv["Xep_loai"])

selectbox.observe(hien_thi_sinh_vien, names="value")

display(selectbox, output)

hien_thi_sinh_vien()

# 6. Thống kê điểm tổng kết của lớp
diem_trung_binh = df["Tong_ket"].mean()
sv_cao_nhat = df.loc[df["Tong_ket"].idxmax()]
sv_thap_nhat = df.loc[df["Tong_ket"].idxmin()]
so_sv_dat = (df["Tong_ket"] >= 5).sum()
print(f"Điểm tổng kết trung bình của lớp: {diem_trung_binh:.2f}")
print(f"Sinh viên cao nhất: {sv_cao_nhat['Họ và tên']} - {sv_cao_nhat['Tong_ket']:.2f} điểm")
print(f"Sinh viên thấp nhất: {sv_thap_nhat['Họ và tên']} - {sv_thap_nhat['Tong_ket']:.2f} điểm")
print(f"Số sinh viên đạt (>= 5): {so_sv_dat}")

# 7. Vẽ biểu đồ cột
import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.bar(df["Họ và tên"], df["Tong_ket"])

plt.title("Điểm tổng kết của 10 sinh viên")
plt.xlabel("Họ và tên sinh viên")
plt.ylabel("Điểm tổng kết")
plt.xticks(rotation=45)
plt.ylim(0, 10)
plt.tight_layout()
plt.show()

# 8. Hiển thị họ tên và MSSV ở cuối trang Web App với kích thước chữ nhỏ (Yêu cầu cuối cùng)
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray; font-size: 11px;'>Họ và tên: [Nguyễn Hải Long] - MSSV: [068208011020]</p>",
    unsafe_allow_html=True