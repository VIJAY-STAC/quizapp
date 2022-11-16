import json

# read file
Quizejsonfile = open('quizquestions.json','r')
jsondata = Quizejsonfile.read()

# parse data
a = json.loads(jsondata)

def Quize():
  score = 0
  for i in range(0,len(a)):
      print("\n{}.{}\n".format(i+1,a[i]['question'])) 
      for k in range(0,len(a[i]['choices']),1):
          print("{}) {}".format(k+1,(a[i]['choices'][k]))) 
      ans = int(input('\nSelect the correct option: ')) 
      if (a[i]['choices'][ans-1] ) == a[i]['correct_ans']:
          score = score + 1
  return score


name = input("Enter your  name : ")
Total_Score = Quize()         
print('\n{} your total score is :{} '.format(name.title(), Total_Score))
