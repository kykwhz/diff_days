# diff_days3.py
#
# 方針
# 対象年月日までの各年月日をリストの各要素に格納して、要素数の差で計算する

# 閏年判定関数
# 引数 年(int)
# 返値 0(平年) or 1(閏年)
def isLeap(y):
	if not (y % 400):
		return 1 # d_in_m[1]を参照する
	if not (y % 100):
		return 0 # d_in_m[0]を参照する
	if not (y % 4):
		return 1
	return 0

# 各月の日数テーブル
# i番目とi月が一致するように、0番目の要素は0で埋めている。
d_in_m = ((0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),\
          (0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31))

def make_dayslist(y, m, d):
    days = []
    for i in range(1, y):
        for j in range(1, 13):
            for k in range(1, d_in_m[isLeap(i)][j] + 1):
                days.append(str(i) + '年' + str(j) + '月' + str(k) + '日')
    for j in range(1, m):
        for k in range(1, d_in_m[isLeap(y)][j] + 1):
            days.append(str(y) + '年' + str(j) + '月' + str(k) + '日')
    for k in range(1,d + 1):
        days.append(str(y) + '年' + str(m) + '月' + str(k) + '日')
    return days

'''
print(len(make_dayslist(2021,8,26)) - len(make_dayslist(2021,8,25)))
'''

def diff_days(y1, m1, d1, y2, m2, d2):
    return len(make_dayslist(y2, m2, d2)) - len(make_dayslist(y1, m1, d1))

# テストコード
print(f'diff_days(2000,1,1,2000,1,1) : {diff_days(2000,1,1,2000,1,1)}')
print(f'diff_days(2000,1,1,2000,1,31) : {diff_days(2000,1,1,2000,1,31)}')
print(f'diff_days(2000,1,1,2000,12,31) : {diff_days(2000,1,1,2000,12,31)}')
print(f'diff_days(2000,1,1,2001,1,1) : {diff_days(2000,1,1,2001,1,1)}')
print(f'diff_days(2000,1,1,2001,12,31) : {diff_days(2000,1,1,2001,12,31)}')
print(f'diff_days(1999,12,31,2001,1,1) : {diff_days(1999,12,31,2001,1,1)}')
