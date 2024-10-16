# HackerRank Day14

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        maximumDifference = 0
        
        for i in self.__elements:
            for j in self.__elements:
                diff = abs(i-j)
                # print(diff)
                if diff > maximumDifference: 
                    maximumDifference = diff
        self.maximumDifference = maximumDifference
        return self.maximumDifference    
                    

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)