# Homework Calculator

h=1.5
q=1
t=1.5
p=2
e=3

print('Hello! Welcome to the Anti-Procrastinate Together homework time calculator. Please note these are only estimates and actual time needed may vary.')
print('This tool is assuming homework takes 1.5 hours to complete, quizzes take 1 hour to complete, tests take 1.5 hours to complete, projects take 2 hours to complete, and exams takes 3 hours for review.')
hn=int(input('How many pieces of homework were you assigned? '))
qn=int(input('How many quizzes do you have? '))
tn=int(input('How many tests do you have? '))
pn=int(input('How many projects do you have? '))
en=int(input('How mnay exams do you have? '))

hn=h*hn
qn=q*qn
tn=t*tn
pn=p*pn
en=e*en

tot=str(hn+qn+tn+en+pn)

print('You should spend')
hn=str(hn)
qn=str(qn)
tn=str(tn)
pn=str(pn)
en=str(en)


if hn !="0":
	print(hn+' hours on homework')
if qn != "0":
	print(qn+' hours on quiz review')
if tn != "0":
	print(tn+' hours on test review')
if en != "0":
	print(en+' hours on your exam review.')
if pn != "0":
	print(pn+' hours on your project')

print('In total, you should spend '+tot+' hours on work')

print('Thanks for using our tool and we hope it helped!')
