key = ['D',  'B',  'D',  'C',  'C',  'D',  'A',  'E',  'A',  'D']

student_answers =  [
	 ['A'  ,'B',  'A',  'C',  'C',  'D',  'E',  'E',  'A',  'D'],
	 ['D', 'B',  'A',  'B',  'C',  'A',  'E',  'E',  'A',  'D'],
	 ['E', 'D',  'D',  'A',  'C',  'B',  'E',  'E',  'A',  'D'],
	 ['C', 'B',  'A',  'E',  'D',  'C',  'E',  'E',  'A',  'D'],
	 ['A', 'B',  'D',  'C',  'C',  'D',  'E',  'E',  'A',  'D'],
	 ['B', 'B',  'E',  'C',  'C',  'D',  'E',  'E',  'A',  'D'],
	 ['B', 'B',  'A',  'C',  'C',  'D',  'E',  'E',  'A',  'D'],
	 ['E', 'B',  'E',  'C',  'C',  'D',  'E',  'E',  'A',  'D']
  ]


noOfStud = len(student_answers)
score = {'Student '+str(x+1):0 for x in range(noOfStud)}
ques = len(key)

for i in range(noOfStud):
    for j in range(ques):
        if key[j] == student_answers[i][j]:
            score['Student '+str(i+1)] += 1

for k,v in score.items():
    print(k,'=',v)
