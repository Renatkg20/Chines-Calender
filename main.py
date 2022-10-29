# User input the year and program gives result accourding Chines Calendar
user = input("Please input the year: ")

lis1 = {1:"Cock",2:"Dog",3:"Pig",4:"Rate",5:"Bull",6:"Tiger", 7:"Hare",8:"Dragon",9:"Snake",10:"Horse",11:"Sheep",0:"Monkey"}

ans = int(user) % 12

print(user,"is ", lis1.get(ans))