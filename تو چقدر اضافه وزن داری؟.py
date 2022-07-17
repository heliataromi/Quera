weight = int(input())
height = float(input())

bmi = weight / height ** 2
state = ''

if bmi < 18.5:
	state = 'Underweight'

elif 18.5 <= bmi < 25:
	state = 'Normal'

elif 25 <= bmi < 30:
	state = 'Overweight'

else:
	state = 'Obese'

print('%.2f' % bmi)

print(state)
