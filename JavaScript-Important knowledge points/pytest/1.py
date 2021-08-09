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
            
    
########
class Customer:
    def _init_(self,rank:float, num:int, order:list, money:float,discount:float)->None:
        #用户积分
        self.rank=rank
        #用户的初始订单数
        self.num=0
        #用户的订单列表
        self.order=[]
        #未打折的金额
        self.money=money
        #未打折就是1
        self.discount=1
    def setRank(self,rank:float)->None:
        self.rank=rank
    def getRanke(self)->float:
        return self.rank
    def setMoney(self,money:float)->None:
        self.money=money
    def getMoney(self)->float:
        return self.money
    def setNum(self,num:int)->None:
        self.num=num
    def getNum(self)->None:
        return self.num
    def setOrder(self,order:list)->None:
        self.order=order
    def getOrder(self)->list:
        return self.order
    def setDiscount(self, discount:float)-> None:
        self.discount=discount
    def getDisocunt(self, discount)->float:
        return self.discount
    def orderDiscount1(self)->float:
        if self.rank>=1000:
            self.setDiscount(0.95)
        else:
            self.setDiscount(1)
        return self.discount

    def orderDiscount2(self)->float:
        dict={}
        list=[]
        for o in self.getOrder():
            dict[o]=dict.get(o,0)+1
        for v in dict.values():
            list.append(v)
        a=max(list)
        if a>=20:
            self.setDiscount(0.9)
        else:
            self.setDiscount(1)  
        return self.discount
    def orderDiscount3(self)->float:
        dict={}
        for o in self.getOrder():
            dict[o]=dict.get(o,0)+1
        if len(dict)>=10:
            self.setDiscount(0.93)
        else:
            self.setDiscount(1)
        return self.discount
 #输入用户数据
if __name__ == "__main__":
    customer=Customer()
    order=["青菜","西红柿","辣椒","哈密瓜","香蕉","青菜","西红柿","青菜"]
    customer.setOrder(order)
    customer.setMoney(100)
    customer.setRank(2000)
    discount1=customer.orderDiscount1()
    discount2=customer.orderDiscount2()
    discount3=customer.orderDiscount3()
    list=[discount1,discount2,discount3]
    print(list)
    a=min(list)
    b=a*customer.getMoney()
    remainrank=customer.getMoney()*(1-a)
    customer.setRank(customer.rank-remainrank)
    print(customer.rank)

  
       
