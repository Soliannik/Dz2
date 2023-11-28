class Person:
    happiness = 100
    tiredness = 0
    smart = 110
    money = 1000
    name = ''
    rest = 100
    progress = 0
    alive = True

    def eat(self):
        self.happiness += 10
        self.progress += 40
    def sleep(self):
        self.tiredness -= 10
        self.happiness += 10
        self.rest += 25
        self.progress += 10
    def work(self):
        self.tiredness +=10
        self.money += 600
        self.progress -= 20
    def study(self):
        self.smart += 15
        self.tiredness += 20
        self.progress += 30
    def rest(self):
        self.progress -= 10
        self.happiness += 30
    def alive(self):
        if self.progress <= -0.5:
            print('Uh...I have bad news...')
            self.alive = False

student = Person()
student.name = 'Mike'
print(student.happiness, student.tiredness)
student.sleep()
student.study()
student.work()
student.rest()
student.alive
print(student.happiness,student.tiredness,student.smart,student.progress,student.money)

