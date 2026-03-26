class Time:
    def __init__(self,hour,minute,second):
        self.__second=second
        self.__minute=minute
        self.__hour=hour
    def __add__(self,other):
        s=self.__second+other.__second
        m=self.__minute+other.__minute
        h=(self.__hour+other.__hour)%24
        if s>=60:
            s%=60
            m+=1
        if m>=60:
            m%=60
            h+=1
        return Time(h,m,s)    
    def __str__(self):
        return f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}"
t1=Time(2,30,40)
t2=Time(4,80,20)
t=t1+t2
print(t)