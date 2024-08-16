import matplotlib.pyplot as plt
import numpy as np

# Thông tin về các trạng thái
V1, V2, V3 = 3, 12, 3
T1, T2, T3 = 200, 80, 80
P1, P2, P3 = 10, 1, 4

# Định nghĩa phạm vi giá trị
V = np.linspace(0.5, 15, 400)
T = np.linspace(50, 250, 400)
P = np.linspace(0.5, 12, 400)

# Phương trình đẳng nhiệt
def isothermal_pressure(V, T, T0):
    return P1 * (T0 / T1) * (V1 / V)

# Phương trình đẳng áp
def isobaric_temperature(V, P, P0):
    return (T1 * V1 / P0) * P

# Phương trình đẳng khối
def isochoric_pressure(T, V, V0):
    return (P1 * T / T1) * (V0 / V)

# Tạo đồ thị
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Đồ thị đẳng nhiệt
axs[0].plot(V, isothermal_pressure(V, T1, T1), label='T = 200K')
axs[0].plot(V, isothermal_pressure(V, T2, T2), label='T = 80K')
axs[0].set_xlabel('Thể tích (V)')
axs[0].set_ylabel('Áp suất (P)')
axs[0].set_title('Đồ Thị Đẳng Nhiệt')
axs[0].legend()
axs[0].grid(True)

# Đồ thị đẳng áp
axs[1].plot(V, isobaric_temperature(V, P2, P2), label='P = 1 atm')
axs[1].plot(V, isobaric_temperature(V, P3, P3), label='P = 4 atm')
axs[1].set_xlabel('Thể tích (V)')
axs[1].set_ylabel('Nhiệt độ (T)')
axs[1].set_title('Đồ Thị Đẳng Áp')
axs[1].legend()
axs[1].grid(True)

# Đồ thị đẳng khối
T_vals = np.linspace(50, 250, 400)
axs[2].plot(T_vals, isochoric_pressure(T_vals, V1, V1), label='V = 3 l')
axs[2].plot(T_vals, isochoric_pressure(T_vals, V2, V2), label='V = 12 l')
axs[2].set_xlabel('Nhiệt độ (T)')
axs[2].set_ylabel('Áp suất (P)')
axs[2].set_title('Đồ Thị Đẳng Khối')
axs[2].legend()
axs[2].grid(True)

plt.tight_layout()
plt.show()
