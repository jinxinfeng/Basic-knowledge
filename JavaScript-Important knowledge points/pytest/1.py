#代码测试中
class Good:
    def __init__(self,gid,num:int) -> None:
        self.gid = gid
        self.num=num
        pass

class Order(Good):
    def __init__(self,id:int,discount:float) -> None:
       self.id = id
       self.discount =discount
          
    def setDiscount(self, discount: float) -> None:
        self.discount = discount
    
    def getDiscount(self) -> float:
        return self.discount



class Customer(Order,Good):
    def __init__(self,rank:int,num:int,order:Order) -> None:
        self.rank = 0 #用户初始积分
        self.num=0 #用户的初始订单数
        self.order = [] #表示订单列表
    def setRank(self, rank: int)-> None:
        self.rank = rank

    def getRank(self) -> float:
        return self.rank

    
    def setNum (self,num: int) -> None:
       self.num = num

    def getNum(self) -> int:
        return self.num
    
    def setOrder(self,order: Order) -> None:
        self.order = order

    def getOrder(self) -> Order:
        return self.order;
        
    def OrderHandler1(self) -> float:
        if(self.rank >= 1000):
            self.setDiscount(0.95)
    
    def OrderHandler2(self) -> float:
        for o in self.getOrder():
            if(o.gid == self.gid and self.num >= 20):
                self.setDiscount(0.9)

    def OrderHandler3(self) -> float:
        for o in self.getOrder():
            if(o.gid != self.gid and self.num >=10):
                self.setDiscount(0.93)


class Cart(Customer,Good):
    def __init__(self, rank: int, num: int, order: Order,maxDiscount: float) -> None:
        super().__init__(rank, num, order)
        self.maxDiscount = 0.0

 

    def OrderHandler4(self) -> float:
        #计算积分，并返回最大折扣
        if(self.rank>=1000):
            self.OrderHandler1()
            self.maxDiscount += self.getNum()*self.getDiscount()
            for o in self.order:
                if(o.id== self.id and self.num>=20): 
                    self.OrderHandler2()
                    self.maxDiscount += self.getNum()*self.getDiscount()
                elif(o.id==self.id):
                    self.OrderHandler3()
                    self.maxDiscount+=self.getNum()*self.getDiscount()
                    
                else:
                    return self.maxDiscount
            
    


  
       
