# diff_days.py
#
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
# タプルd_in_mの確認
print(f'平年の日数は{sum(d_in_m[0])}です')
print(f'閏年の日数は{sum(d_in_m[1])}です')
'''

# 月の指定はn月からm月の場合、[n:m+1]
# 例)7月から8月までの62日間の日数を計算する
# print(f'平年の7月〜8月の日数は{sum(d_in_m[0][7:9])}')


'''
# isLeap関数のテストコード
print(f'isLeap(1999) : {isLeap(1999)}') # return 0 (平年)
print(f'isLeap(2000) : {isLeap(2000)}') # return 1 (400で割り切れるので閏年)
print(f'isLeap(2001) : {isLeap(2001)}') # return 0 (平年)
print(f'isLeap(2002) : {isLeap(2002)}') # return 0 (平年)
print(f'isLeap(2003) : {isLeap(2003)}') # return 0 (平年)
print(f'isLeap(2004) : {isLeap(2004)}') # return 1 (4で割り切れるので閏年)
print(f'isLeap(2005) : {isLeap(2005)}') # return 0 (平年)
print(f'isLeap(2099) : {isLeap(2099)}') # return 0 (平年)
print(f'isLeap(2100) : {isLeap(2100)}') # return 0 (100で割り切れるので平年)
print(f'isLeap(2101) : {isLeap(2101)}') # return 0 (平年)
'''

'''
# JulianDate_past : 1月1日から数えた経過日数
# JulianDate_remaqin : 12月31日までの残り日数
'''

# ジュリアンデイズ(経過日数)関数
# 引数 年月日
# 返値 引数の当年(y年)の1月1日から引数の年月日までの経過日数
def JulianDate_past(y,m,d):
	days = sum(d_in_m[isLeap(y)][:m]) + d
	return days

# ジュリアンデイズ(残日数)関数
# 引数 年月日
# 返値 引数の年月日から引数の当年(y年)の12月31日までの残日数
def JulianDate_remain(y,m,d):
	days = sum(d_in_m[isLeap(y)][m + 1:]) + (d_in_m[isLeap(y)][m] - d + 1)
	return days

'''
# JulianDate_past関数のテストコード
print(f'JulianDate_past(2020,12,31) : {JulianDate_past(2020,12,31)}')
print(f'JulianDate_past(2021,12,31) : {JulianDate_past(2021,12,31)}')
'''

# JulianDate_past関数とJulianDate_remain関数のテストコード
print(f'JulianDate_past(2021,1,31) : {JulianDate_past(2021,1,31)}')
print(f'JulianDate_remain(2021,1,31) : {JulianDate_remain(2021,1,31)}')
print(f'JulianDate_past(2020,1,31) + JulianDate_remain(2021,1,31) = {JulianDate_past(2021,1,31) + JulianDate_remain(2021,1,31)}')

# diff_days関数 - 基準日(y1,m1,d1)から対象日(y2,m2,d2)までの日数
# 引数 基準日(y1,m1,d1)、対象日(y2,m2,d2)
# 返値 日数
def diff_days(y1, m1, d1, y2, m2, d2):
	days = []

	if y1 == y2:
		days.append(JulianDate_past(y2, m2, d2) - JulianDate_past(y1, m1, d1))
	else:
		days.append(JulianDate_remain(y1, m1, d1))

		for n in range(y1+1, y2):
			days.append(JulianDate_past(n, 12, 31))

		days.append(JulianDate_past(y2,m2,d2) - 1)
	
#	return days
	return sum(days)

# テストコード
print(f'diff_days(2000,1,1,2000,1,1) : {diff_days(2000,1,1,2000,1,1)}')
print(f'diff_days(2000,1,1,2000,1,31) : {diff_days(2000,1,1,2000,1,31)}')
print(f'diff_days(2000,1,1,2000,12,31) : {diff_days(2000,1,1,2000,12,31)}')
print(f'diff_days(2000,1,1,2001,1,1) : {diff_days(2000,1,1,2001,1,1)}')
print(f'diff_days(2000,1,1,2001,12,31) : {diff_days(2000,1,1,2001,12,31)}')
print(f'diff_days(1999,12,31,2001,1,1) : {diff_days(1999,12,31,2001,1,1)}')

"datetime.pyから引っ張ってきた"
def _is_leap(year):
    "year -> 1 if leap year, else 0."
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def test():
	"aあいうえお" # この行頭のダブルクォーテーションのリテラル？は、コメントみたいな形として人間には扱われるのか？