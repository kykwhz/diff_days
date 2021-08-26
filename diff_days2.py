# diff_days2.py
#
# 方針
# (西暦1年1月1日から西暦y2年m2月d2日までの日数) - (西暦1年1月1日から西暦y1年m1月d1日までの日数)

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



'''
# JulianDate_past : 1月1日から数えた経過日数
'''

# ジュリアンデイズ(経過日数)関数
# 引数 年月日
# 返値 引数の当年(y年)の1月1日から引数の年月日までの経過日数
def JulianDate_past(y,m,d):
	days = sum(d_in_m[isLeap(y)][:m]) + d
	return days

# diff_days_from_1_1_1関数 - 基準日(西暦1年1月1日)から対象日(y,m,d)までの日数
# 引数 対象日(y,m,d)
# 返値 日数
def diff_days_from_1_1_1(y, m, d):
    days = []
    for n in range(1, y):
        days.append(JulianDate_past(n, 12, 31))
    days.append(JulianDate_past(y, m, d)) # diff_days.pyでは、-1を付加しているが、今回は差分なので無くても良い？
    return sum(days)

# diff_days関数 - 基準日(y1,m1,d1)から対象日(y2,m2,d2)までの日数
# 引数 基準日(y1,m1,d1)、対象日(y2,m2,d2)
# 返値 日数
def diff_days(y1, m1, d1, y2, m2, d2):
    return diff_days_from_1_1_1(y2, m2, d2) - diff_days_from_1_1_1(y1, m1, d1)

# テストコード
print(f'diff_days(2000,1,1,2000,1,1) : {diff_days(2000,1,1,2000,1,1)}')
print(f'diff_days(2000,1,1,2000,1,31) : {diff_days(2000,1,1,2000,1,31)}')
print(f'diff_days(2000,1,1,2000,12,31) : {diff_days(2000,1,1,2000,12,31)}')
print(f'diff_days(2000,1,1,2001,1,1) : {diff_days(2000,1,1,2001,1,1)}')
print(f'diff_days(2000,1,1,2001,12,31) : {diff_days(2000,1,1,2001,12,31)}')
print(f'diff_days(1999,12,31,2001,1,1) : {diff_days(1999,12,31,2001,1,1)}')
