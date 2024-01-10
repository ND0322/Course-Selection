from collections import namedtuple
from queue import Queue

INF = 1e18


class MCF:

    edge = namedtuple("edge", "v c w id")

    

    def __init__(self, lcs, lrobo, lbuis, ldraft):
        self.N = 7
        self.id = 7
        self.mp = {}


        self.dist = [INF] * self.N
        self.cnt = [0] * self.N
        self.inq = [False] * self.N
        self.adj = [[] for i in range(self.N)]

        self.ans = 0
        self.tot = 0

        self.addEdge(3, 1, lcs, 0)
        self.addEdge(3,1,1000, 10000)
        self.addEdge(4, 1, lrobo, 0)
        self.addEdge(4,1,1000, 10000)
        self.addEdge(5, 1, lbuis, 0)
        self.addEdge(5,1,1000, 10000)
        self.addEdge(6, 1, ldraft, 0)
        self.addEdge(6,1,1000, 10000)



    

    def addEdge(self, u,v,c,w):
        self.adj[u].append(self.edge(v,c,w, len(self.adj[v])))
        self.adj[v].append(self.edge(u, 0, -w, len(self.adj[u])-1))

    #can replace name with student number here
    def add(self, name, cs, robo, buis,draft):
        self.N+=1
        self.dist.append(INF)
        self.inq.append(False)
        self.adj.append([])
        self.cnt.append(0)
        self.mp[name] = self.id

        self.addEdge(0,self.id,2,0)
        self.addEdge(self.id, 3,1, cs)
        self.addEdge(self.id, 4,1, robo)
        self.addEdge(self.id, 5, 1, buis)
        self.addEdge(self.id, 6, 1, draft)

        self.id += 1
    
    def query(self, name):
        ans = []
        for v,c,w,id in self.adj[self.mp[name]]:
            if(not c):
                if(v == 3):
                    ans.append("cs")
                if(v == 4):
                    ans.append("robo")
                if(v == 5):
                    ans.append("buis")
                if(v == 6):
                    ans.append("draft")
        
        return ans





    def spfa(self):
        q = Queue()

        for i in range(self.N):
            self.dist[i] = INF
            self.cnt[i] = 0
            self.inq[i] = False


        self.dist[0] = 0

        q.put(0)

        while(not q.empty()):
            node = q.get()
            self.inq[node] = False

            for child,c,w,id in self.adj[node]:
                if(c > 0 and self.dist[child] > self.dist[node] + w):
                    self.dist[child] = self.dist[node] + w
                    if(not self.inq[child]):
                        self.inq[child] = True
                        q.put(child)
                        
        for i in range(self.N):
            self.inq[i] = False
        return self.dist[1] != INF

    def dfs(self, node = 0, f = 1e18):
        
        if(node == 1):
            self.tot += f * self.dist[node]
            return f
        
        
        
        ret = 0

        self.inq[node] = True

        while(self.cnt[node] < len(self.adj[node])):
            e = self.adj[node][self.cnt[node]]
            child = e.v
            
            if(not self.inq[child] and e.c > 0 and self.dist[child] == self.dist[node] + e.w):
                tmp = self.dfs(child, min(e.c, f))

                
                ret += tmp

                self.adj[node][self.cnt[node]] = self.edge(e.v, e.c - tmp, e.w, e.id)
                self.adj[child][e.id] = self.edge(node, self.adj[child][e.id].c+tmp, self.adj[child][e.id].w, self.adj[child][e.id].id)
                
                f -= tmp
                if(not f):
                    break
            
            self.cnt[node] += 1

        self.inq[node] = 0
        if(not ret):
            self.dist[node] = INF
        
        return ret 
        
    def dinic(self):
        while(self.spfa()):
            self.ans += self.dfs()
    
    def get_ans(self):
        return self.ans

    def get_tot(self):
        return self.tot

   


