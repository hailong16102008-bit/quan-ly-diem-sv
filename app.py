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
st.dataframe(df)
# 3. Tính điểm tổng kết
df["Tong_ket"] = (
    0.2 * df["Điểm chuyên cần"]
    + 0.3 * df["Điểm giữa kỳ"]
    + 0.5 * df["Điểm cuối kỳ"]
).round(2)

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
st.dataframe(df)

# 5. Tạo danh sách xổ xuống chọn sinh viên
st.subheader("Tra cứu thông tin cá nhân sinh viên")
selected_student = st.selectbox("Chọn tên sinh viên cần xem:", df["Họ và tên"])

student_info = df[df["Họ và tên"] == selected_student].iloc[0]

st.write(f"- **Họ và tên:** {student_info['Họ và tên']}")
st.write(f"- **Chuyên cần:** {student_info['Điểm chuyên cần']}")
st.write(f"- **Giữa kỳ:** {student_info['Điểm giữa kỳ']}")
st.write(f"- **Cuối kỳ:** {student_info['Điểm cuối kỳ']}")
st.write(f"- **Điểm tổng kết:** **{student_info['Tong_ket']}**")
st.write(f"- **Xếp loại:** **{student_info['Xep_loai']}**")

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
    unsafe_allow_html=True)
