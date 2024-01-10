import mincostflow

m = mincostflow.MCF(100,100,100,100)

m.add("tom",1,2,3,4)

m.add("a",1,2,3,4)
m.add("b",1,2,3,4)
m.add("c",1,2,3,4)
m.add("d",1,2,3,4)
m.add("e",1,2,3,4)
m.add("f",1,2,3,4)
m.add("g",1,2,3,4)
m.add("h",1,2,3,4)
m.add("i",1,2,3,4)
m.add("j",1,2,3,4)
m.add("k",1,2,3,4)
m.add("l",1,2,3,4)
m.add("m",1,2,3,4)
m.add("m",1,2,3,4)
m.add("o",1,2,3,4)



m.dinic()

print(m.get_ans(), m.get_tot())
print(m.query("tom"))
   