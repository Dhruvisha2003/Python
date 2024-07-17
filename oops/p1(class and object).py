class cricket:
    def a(self):
        self.name = input('Enter Name :')
        self.matches = int(input('Enter Matches :'))
        # self.runs = int(input('Enter Runs :'))
        run = []
        for i in range(self.matches):
            print('Enter Runs of Match',i,':')
            arr = int(input())
            run.append(arr)
        print('Name of player :',self.name)
        print('Number of matches :',self.matches)
        print('Runs : ',run)
        sum = 0
        for i in range(len(run)):
            sum = sum + run[i]
        average = sum / len(run)
        print('Average of Runs : ',average)
      

list1 = []
n = 3
for i in range(n):
    list1.append(cricket())
print(list1)

for obj in list1:
    obj.a()


