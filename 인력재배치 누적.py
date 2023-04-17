import matplotlib.pyplot as plt
import numpy as np

x = np.array(['2023-03-20', '2023-03-27', '2023-04-03', '2023-04-10', '2023-04-17'])
y = np.array([ 4, 6, 1, 2, 1])

fig, ax = plt.subplots()

# 각 바를 누적해서 그리기 위해 bottom 속성 사용
ax.bar(x, y, bottom=np.cumsum(np.hstack(([0], y[:-1]))), label='Cumulative')

# 각 바의 최상단에 총 개수를 추가합니다.
for i, v in enumerate(np.cumsum(y)):
    ax.text(i, v, str(v), ha='center', va='bottom')

# 각 영역의 중앙에 해당하는 위치에 숫자를 추가합니다.
for i in range(len(x)):
    x_pos = i
    y_pos = 0
    for j, y_value in enumerate(y[:i+1]):
        y_pos += y_value
    ax.text(x_pos, y_pos - y_value / 2, str(y_value), ha='center', va='center')

# y축 범위 변경
ax.set_ylim(0, 30)

# y축 눈금 설정
ax.set_yticks(np.arange(0, 31, 5))

ax.set_xlabel('Date')
ax.set_ylabel('Number of Employees')

plt.show()
