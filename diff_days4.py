# フェアフィールド(Fairfield)の公式
# 参照URI
# https://ja.wikipedia.org/wiki/ツェラーの公式#フェアフィールドの公式

def days(y, m, d):
    if m == 1 or m == 2:
        y -= 1
        m += 12
    return 365 * y + y // 4 - y // 100 + y // 400 + 306 * (m + 1) // 10 + d - 428

def diff_days(y1, m1, d1, y2, m2, d2):
    return days(y2, m2, d2) - days(y1, m1, d1)

# テストコード
print(f'diff_days(2000,1,1,2000,1,1) : {diff_days(2000,1,1,2000,1,1)}')
print(f'diff_days(2000,1,1,2000,1,31) : {diff_days(2000,1,1,2000,1,31)}')
print(f'diff_days(2000,1,1,2000,12,31) : {diff_days(2000,1,1,2000,12,31)}')
print(f'diff_days(2000,1,1,2001,1,1) : {diff_days(2000,1,1,2001,1,1)}')
print(f'diff_days(2000,1,1,2001,12,31) : {diff_days(2000,1,1,2001,12,31)}')
print(f'diff_days(1999,12,31,2001,1,1) : {diff_days(1999,12,31,2001,1,1)}')
