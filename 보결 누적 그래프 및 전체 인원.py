import matplotlib.pyplot as plt
import numpy as np

# 데이터 설정
x = np.array(['2023-03-27', '2023-04-03', '2023-04-10', '2023-04-17'])
y1 = np.array([6,1,2,1]) #인력재배치의 기간별 수치
y2 = np.array([6,6,7,7]) #외부채용의 기간별 수치
y3 = np.array([2,0,0,0]) #미채용의 기간별 수치
y4 = np.array([6,4,4,4]) #미정(협의중)의 기간별 수치
y5 = np.array([1247,1241,1240,1235]) #전체 직원 수

# 누적 그래프 생성
fig, ax1 = plt.subplots()
ax1.bar(x, y1, label='relocation')
ax1.bar(x, y2, bottom=y1, label='recruit')
ax1.bar(x, y3, bottom=y1+y2, label='no-recruit')
ax1.bar(x, y4, bottom=y1+y2+y3, label='undecided')
for i, v in enumerate(y1+y2+y3+y4):
    ax1.text(i, v, str(v), ha='center', va='bottom')
for i in range(len(x)):
    x_pos = i
    y_pos = 0
    for j, y in enumerate([y1[i], y2[i], y3[i], y4[i]]):
        if y > 0:
            y_pos += y
            ax1.text(x_pos, y_pos - y / 2, str(y), ha='center', va='center')
ax1.legend()
ax1.set_ylabel('Number of Employees')

# 선형 그래프 생성
fig, ax2 = plt.subplots()
ax2.plot(x, y5, color='skyblue', linestyle='--', linewidth=1.5, label='total employee')
for i, v in enumerate(y5):
    ax2.text(i, v, str(v), ha='center', va='bottom', color='blue', fontweight='bold')
ax2.set_ylim(500, 1500)
ax2.set_yticks(np.arange(500, 1501, 50))
ax2.set_ylabel('Total Number of Employees')
ax2.legend()

# 그래프 출력
plt.show()

# 누적 막대 그래프 출력
fig1.show()

# 선 그래프 출력
fig2.show()
