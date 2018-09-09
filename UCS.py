# Das, Aditya.
# axd5763
# 2018-09-08
import collections
import sys

class Graph:
    def __init__(self):
        self.edges = {}                                          # holds the neighbours to the cities
        self.weights = {}                                        # holds the distance of the neighbours from the cities
        self.path = {}                                           # will temporarily hold a path

    def neighbors(self, node):
        return self.edges[node]                                  # returns the neighbours

    def get_cost(self, from_node, to_node):
        index = self.edges[from_node].index(to_node)
        return self.weights[from_node][index]

    def set_path(self, from_node, to_node):
        self.path[from_node] = from_node + "->" + to_node   

    def get_path(self):
        return self.path      

class ModelData :
  def __init__( self, inputFile = None ) :
    self.node = [] 
    
    if inputFile is not None :
      self.loadFile( inputFile )

  def loadFile( self, inputFile ) :
    fp=open(inputFile, 'r')
    lines=fp.read().split('\n')                                 #cleaned file stream in lines
    for line in lines:
      line = line.strip()							                        	# line has a clean stream with data on individual lines
      if(line and 'END'  not in line):
        each_line = line.split()
        self.node.append(each_line)					                    # a list that contains each lines list
  
  def getNode( self )    : return self.node

class Uninformed:
    def __init__(self,arguments):
        self.arguments=arguments
        self.visited=set()
        self.isFound = False
        self.graph=Graph()
        (self.graph.edges, self.graph.weights) = self.get_edges(self.arguments)
        A = self.something(self.arguments)
        
    def get_edges(self,arguments):
      edges = dict()
      weights = dict()
      model=ModelData(arguments[2])
      lists = model.getNode()
      cities = set()
      for(s,d,dis) in lists:
        cities.add(s)
        cities.add(d)
      #print(cities)
      for city in cities:
        nighbrs = []                                            # creating a fresh neighbour and weight list
        wigts = []
        for (x,y,z) in lists:
          if x==city:
            nighbrs.append(y)
            wigts.append(int(z))
          elif y ==city:
            
            nighbrs.append(x)
            wigts.append(int(z))
        edges[city] = nighbrs
        weights[city] = wigts
      return (edges,weights)


    def something(self,arguments):
        dictnry = dict()
        all_dist=[]
        dictnry[arguments[3]] = 0

        model=ModelData(arguments[2])
        for (x,y,z) in model.node:
          if x==arguments[3]:
            dictnry[y] = int(z)
            
          elif y ==arguments[3]:
            dictnry[x] = int(z)
        
        dictnry = [(v, k) for k, v in dictnry.items()]
        dictnry.sort()
        dictnry = [(k, v) for v, k in dictnry]
        while dictnry:

          dictnry = [(v,k) for k,v in dictnry]
          dictnry.sort()
          dictnry = [(k,v) for v,k in dictnry]
          
          (key,value) = dictnry[0]
          del dictnry[0]
          if key not in self.visited:
            self.visited.add(key)
            if key == arguments[4]:
                self.isFound=True
                print self.isFound
                all_dist.append(value)
                # all_dist = [(v) for v in all_dist]
                # all_dist.sort()
                print "distance:",int(all_dist[0])
                #break
            for i in self.graph.neighbors(key):
              if i not in self.visited:
                #self.visited.add(key)
                total_distance= value+self.graph.get_cost(key,i)
                self.graph.set_path(key,i)
                dictnry.append((i, int(total_distance)))
                #print dictnry
                #print self.visited
        if self.isFound==True:
          print 'Path present'
        else:
          print 'Path not present'
          print "distance: infinity"                  
def _main() :
  
  fName = sys.argv[2]
  source = sys.argv[3]
  goal = sys.argv[4]
  model = ModelData( fName )
  x=sys.argv
  # Get the file name to load.
  if len(sys.argv)==5 and sys.argv[1] == 'uninf':
      Uninformed(x)
  elif len(sys.argv)==5 and sys.argv[1]!='uninf':
  		print"Enter proper arguments and try again"
  
  elif len(sys.argv)==6 and sys.argv[1]=='inf':
  		print"inf"
  elif len(sys.argv)==6 and sys.argv[1]!='inf':
  		print"Enter proper arguments and try again"
  
  elif len(sys.argv)<5 or len(sys.argv)>6:
  		print"Enter proper arguments and try again"
 
if __name__ == '__main__' :
  _main()

