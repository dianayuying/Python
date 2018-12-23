"""
Game Statement:
    Bulls correct position
    Cows incorrect position but in the digit in the list
"""
class BullsAndCows:
    def __init__(self, n):
        self.checkN(n)
        self.secrete=n
        self.gameStatus=0
        self.winStatus=0

    def checkN(self, n):
        if type(n)!=int:
            raise ValueError("not an integer")
        if n<0:
            raise ValueError("not a positive number")
        if len(str(n))!=4:
            raise ValueError("number error")
        else:
            nList=list(str(n))
            nList.sort()
            for i in range(len(nList)-1):
                if nList[i]==nList[i+1]:
                    raise ValueError("number error")

    def checkStatus(self):
        if self.winStatus==1:
            return "You already won!"
        self.gameStatus+=1
        if (self.gameStatus>8):
            return "Sorry, you're out of turns!"
        return None

    def compare_with(self, n):     
        checkStr=self.checkStatus()
        if checkStr:
            return checkStr
        else:
            try:
                self.checkN(n)
            except ValueError:
                self.gameStatus -=1
                raise ValueError("error")

            # Main Logic
            countIn =0
            countBull =0
            for i,x in enumerate(str(n)):
                if x in str(self.secrete): countIn +=1
                if x==str(self.secrete)[i]: countBull +=1 
        
            if countBull==1:
                bullStr = str(countBull)+" bull"
            else:
                bullStr = str(countBull)+" bulls"
            
            if countIn-countBull==1:
                cowStr = " and "+str(countIn-countBull)+" cow"
            else:
                cowStr = " and "+str(countIn-countBull)+" cows"

            if countBull==4:
                self.winStatus=1
                return "You win!"
            else:
                return bullStr+cowStr

#---------
# Other People:
class BullsAndCows:
    def __init__(self, n):
        self.check(n)
        self.s    = str(n)
        self.won  = False
        self.turn = 1
    
    def check(self,n):
        if not (999 < n <= 9999) or len(set(str(n))) != 4:
            raise ValueError()
    
    def compare_with(self, n):
        if self.won:    return "You already won!"
        if self.turn>8: return "Sorry, you're out of turns!"
        
        self.check(n)
        self.turn += 1
        s,c,b = str(n),0,0
        
        if s==self.s:
            self.won = True
            return "You win!"
        for i,ch in enumerate(self.s):
            if ch==s[i]: b+= 1
            else:        c += s.find(ch) != -1

        return f"{b} bull{'s'*(b!=1)} and {c} cow{'s'*(c!=1)}"


#--------------
#Test case

bac = BullsAndCows(7536)
Test.assert_equals(bac.compare_with(1234), "1 bull and 0 cows")
Test.assert_equals(bac.compare_with(5601), "0 bulls and 2 cows")
Test.assert_equals(bac.compare_with(6750), "0 bulls and 3 cows")
Test.assert_equals(bac.compare_with(6357), "0 bulls and 4 cows")
Test.assert_equals(bac.compare_with(7014), "1 bull and 0 cows")
Test.assert_equals(bac.compare_with(6508), "1 bull and 1 cow")
Test.assert_equals(bac.compare_with(4289), "0 bulls and 0 cows")
Test.assert_equals(bac.compare_with(7536), "You win!")

for x in [987, 12345, 1111]:
    Test.expect_error("ValueError was not raised", lambda: BullsAndCows(x), ValueError)
    Test.expect_error("ValueError was not raised", lambda: BullsAndCows(1234).compare_with(x), ValueError)

bac = BullsAndCows(1234)
for i in range(8): bac.compare_with(2035)
Test.assert_equals(bac.compare_with(2035), "Sorry, you're out of turns!")
Test.assert_equals(bac.compare_with(6789), "Sorry, you're out of turns!")
Test.assert_equals(bac.compare_with(111111), "Sorry, you're out of turns!")

bac = BullsAndCows(1234)
bac.compare_with(1234)
Test.assert_equals(bac.compare_with(1234), "You already won!")
Test.assert_equals(bac.compare_with(6789), "You already won!")
Test.assert_equals(bac.compare_with(11111), "You already won!")