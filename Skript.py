#!python3
import sys
Collections = ['0','1','2','3','4','5','6','7','8','9']

def Start(other):


        if len(other) == 2 and MaskImport(other[1]):
                ListMaskAndIp = MaskImport(other[1])
                MyIp = New_IP(ListMaskAndIp[0])
                MyMaska = New_IP(ListMaskAndIp[1])
        elif len(other) == 3:
                MyIp = New_IP(other[1])
                MyMaska = New_IP(other[2])
        else:
                return ("Incorrect IP address__1")

        if MyIp.CheckType() and MyIp.CheckSize() and MyMaska.CheckType() and MyMaska.CheckSize():
                MyIp.IntegerNumber()
                MyMaska.IntegerNumber()
                MyIp.DoubleNumber()
                MyMaska.DoubleNumber()
                HostNumber = CheckHost(MyMaska.ip)
                FirstIp =  MyIp & MyMaska
                FirstIp = (str(FirstIp[0]) + '.' + str(FirstIp[1]) + '.' + str(FirstIp[2]) + '.' + str(FirstIp[3]))
                MyMaska.InvertIp()
                LastIp = MyIp | MyMaska
                LastIp = (str(LastIp[0]) + '.' + str(LastIp[1]) + '.' + str(LastIp[2]) + '.' + str(LastIp[3]))
                return ("Network address = " + FirstIp + "\nBroadcast = " + LastIp + "\nHosts number = " + HostNumber)
        else:
                return ("Incorrect IP address__2")

def CheckHost(other):
        NumberOfUnits = "".join(other)
        flag = 0
        for char in NumberOfUnits:
            if char == '0':
                        flag+=1
        return (str(2 ** flag - 2))

def CheckTypeMaskSlash(other):
        flag = 0
        for i in range(len(other)):
            if any(number == other[i] for number in Collections):
                flag += 1
        if flag != 0 and flag == len(other) and int(other) >= 0 and int(other) <= 32:
            return 1
        else: return 0

def MaskImport(other):
        other = other.split("/")
        if len(other) == 2 and CheckTypeMaskSlash(other[1]):
            MaskAddress = "1" * int(other[1]) + "0" * (32 - int(other[1]))
            NewMaskAddress = [0,0,0,0]
            for i in range(4):
                    NewMaskAddress[i] =  MaskAddress[(i * 8):((i * 8)+8)]
            MaskStr = str(int(NewMaskAddress[0],2)) + "." + str(int(NewMaskAddress[1],2)) + "." + str(int(NewMaskAddress[2],2)) + "." + str(int(NewMaskAddress[3],2))
            other[1] = MaskStr
            return other
        else: return False



class New_IP(object):
        def __init__(self, ip):
                self.ip = ip.split(".")

        def CheckType(self):
            flag = 0
            StringVariable = "".join(self.ip)
            for i in range(len(StringVariable)):
                    if any(number == StringVariable[i] for number in Collections):
                            flag +=1
            if flag == len(StringVariable):
                    return 1
            else: return 0
              
        def CheckSize(self):
                flag = 0
                TimeIp = [0,0,0,0]
                if len(self.ip) == 4:
                    for i in range(len(TimeIp)):
                            TimeIp[i] = int(self.ip[i])
                            if (TimeIp[i] >= 0) and (TimeIp[i] <= 255):
                                    flag += 1
                            else:
                                    flag = 0
                                    break
                    if flag == 4:
                            return 1
                else:
                    return 0

        def DoubleNumber(self):
                for i in range(len(self.ip)):
                        self.ip[i] = bin(self.ip[i])[2:].zfill(8)

        def IntegerNumber(self):
                for i in range(len(self.ip)):
                        self.ip[i] = int(self.ip[i])

        def InvertIp(self):
            for i in range(4):
                self.ip[i] = self.ip[i].replace('0','2').replace('1','0').replace('2','1')

        def __and__(self, other):
                LogSum = [0,0,0,0]
                for i in range(4):
                        LogSum[i] = int(self.ip[i],2) & int(other.ip[i],2)
                        #LogSum[i] = bin(LogSum[i])[2:].zfill(8)
                return LogSum

        def __or__(self, other):
            LogProduct = [0,0,0,0]
            for i in range(4):
                LogProduct[i] = int(self.ip[i],2) | int(other.ip[i],2)
                #LogProduct[i] = bin(LogProduct[i])[2:].zfill(8)
            return LogProduct   
                
if __name__ == "__main__":
        if len(sys.argv) == 2 and MaskImport(sys.argv[1]):
                ListMaskAndIp = MaskImport(sys.argv[1])
                MyIp = New_IP(ListMaskAndIp[0])
                MyMaska = New_IP(ListMaskAndIp[1])
        elif len(sys.argv) == 3:
                MyIp = New_IP(sys.argv[1])
                MyMaska = New_IP(sys.argv[2])
        else:
                print ("Incorrect IP address__1")
                sys.exit()

        if MyIp.CheckType() and MyIp.CheckSize() and MyMaska.CheckType() and MyMaska.CheckSize():
                MyIp.IntegerNumber()
                MyMaska.IntegerNumber()
                MyIp.DoubleNumber()
                MyMaska.DoubleNumber()
                HostNumber = CheckHost(MyMaska.ip)
                FirstIp =  MyIp & MyMaska
                FirstIp = (str(FirstIp[0]) + '.' + str(FirstIp[1]) + '.' + str(FirstIp[2]) + '.' + str(FirstIp[3]))
                MyMaska.InvertIp()
                LastIp = MyIp | MyMaska
                LastIp = (str(LastIp[0]) + '.' + str(LastIp[1]) + '.' + str(LastIp[2]) + '.' + str(LastIp[3]))
                print ("Network address = " + FirstIp + "\nBroadcast = " + LastIp + "\nHosts number = " + HostNumber)
        else:
                print ("Incorrect IP address__2")