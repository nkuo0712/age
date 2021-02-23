driving = input('請問你有開過車嗎？ ')
age = input('請問你的年齡是？ ')
age = int(age)
if driving == '有':
	if age >= 18:
		print('原來如此')
	else:
		print('奇怪 你怎麼會有開過車')
elif driving == '沒有':
	if age >= 18:
		print('你可以考駕照了呀')
	else:
		print('很好，再過幾年你就可以考了')
else:
	print('這樣呀 我知道了')