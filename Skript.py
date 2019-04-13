#!python3
import sys
Collections = ['0','1','2','3','4','5','6','7','8','9']

def Start(other):
        print (other)
        print ("other = ",len(other))
        if len(other) == 2:
                ListMaskAndIp = MaskImport(other[1])
                MyIp = New_IP(ListMaskAndIp[0])
                MyMaska = New_IP(ListMaskAndIp[1])
        elif len(other) == 3:
                MyIp = New_IP(other[1])
                MyMaska = New_IP(other[2])
        else:
                return ("Incorrect IP address__1")

        if MyIp.CheckType() and MyIp.CheckSize() and MyMaska.CheckType() and MyMaska.CheckSize():
                MyIp.DoubleNumber()
                MyMaska.DoubleNumber()
                HostNumber = CheckHost(MyMaska.ip)
                FirstIp =  MyIp & MyMaska
                FirstIp = (str(FirstIp[0]) + '.' + str(FirstIp[1]) + '.' + str(FirstIp[2]) + '.' + str(FirstIp[3]))
                MyMaska.InvertIp()
                LastIp = MyIp | MyMaska
                LastIp = (str(LastIp[0]) + '.' + str(LastIp[1]) + '.' + str(LastIp[2]) + '.' + str(LastIp[3]))
                return ("First_ip = " + FirstIp + "\nLast_ip = " + LastIp + "\nNumbers_of_hosts = " + HostNumber)
        else:
                return ("Incorrect IP address__2")

def CheckHost(other):
        NumberOfUnits = "".join(other)
        flag = 0
        for char in NumberOfUnits:
                if char == '0':
                        flag+=1
        return (str(2 ** flag - 2))

def MaskImport(other):
        other = other.split("/")
        MaskAddress = "1" * int(other[1]) + "0" * (32 - int(other[1]))
        NewMaskAddress = [0,0,0,0]
        for i in range(4):
                NewMaskAddress[i] =  MaskAddress[(i * 8):((i * 8)+8)]
        MaskStr = str(int(NewMaskAddress[0],2)) + "." + str(int(NewMaskAddress[1],2)) + "." + str(int(NewMaskAddress[2],2)) + "." + str(int(NewMaskAddress[3],2))
        other[1] = MaskStr
        return other

class New_IP(object):
        def __init__(self, ip):
                self.ip = ip.split(".")

        def CheckType(self):
                StringVariable = "".join(self.ip)
                for i in range(len(StringVariable)):
                        if not any(number == StringVariable[i] for number in Collections):
                                return 0
                return 1

        def CheckSize(self):
                flag = 0
                for i in range(len(self.ip)):
                        self.ip[i] = int(self.ip[i])
                        if (self.ip[i] >= 0) and (self.ip[i] <= 255):
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
                        self.ip[i] = int(self.ip[i],2)

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
        if len(sys.argv) == 2:
                ListMaskAndIp = MaskImport(sys.argv[1])
                MyIp = New_IP(ListMaskAndIp[0])
                MyMaska = New_IP(ListMaskAndIp[1])
        elif len(sys.argv) == 3:
                MyIp = New_IP(sys.argv[1])
                MyMaska = New_IP(sys.argv[2])
        else:
                print ("Incorrect IP address")
                sys.exit()
        if MyIp.CheckType() and MyIp.CheckSize() and MyMaska.CheckType() and MyMaska.CheckSize():
                MyIp.DoubleNumber()
                MyMaska.DoubleNumber()
                print (MyIp & MyMaska)
                MyMaska.InvertIp()
                print (MyIp | MyMaska)
        else:
                print ("Incorrect IP address")