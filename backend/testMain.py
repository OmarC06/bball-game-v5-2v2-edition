from gameLogic import *

u1 = Player("0", "Guard", "user1")
u2 = Player("1", "Guard", "user2")
u3 = Player("2", "Guard", "user3")


c1 = Player("0", "Guard", "cpu1")
c2 = Player("1", "Guard", "cpu2")
c3 = Player("2", "Guard", "cpu3")



t1 = Team(u1, u2, u3)
t2 = Team(c1, c2, c3)

s = Stats(t1, t2, 5)

g = Game(t1, t2, "Hooper", s)
g.run()
# g.calcRebound(t1, t2)

# t1.onDefense = True
# t1.update()
# g.makeOptions(1, False, None, "Pass")



