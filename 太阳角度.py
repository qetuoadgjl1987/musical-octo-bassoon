x1=[]
y1=[]
from decimal import Decimal
import math
ST=[9,10.5,12,13.5,15]
day=[-60,-29,0,31,62,93,123,155,186,217,249,280]
pai=3.14
# day=31
# 太阳时角 w
avest=[]
for i in ST:
      tysj=pai*(i-12)/12
      avest.append(tysj)
      # print(tysj)
tysj=sum(avest)/5
#太阳赤纬角 cwj
for j in day:
      j=float(j)
      aaa=math.sin(2*pai*j/365)*math.sin((2*pai*23.45)/180)
      cwj=math.asin(aaa)
      # print(aaa)
      # print(cwj)

      #太阳高度角
      singdj=math.cos(round(cwj,3))*math.cos(round(39.3/180*pai,3))*math.cos(round(tysj,3))+math.sin(round(cwj,3))*math.sin(round(39.3/180*pai,3))
      # print(math.asin(round(singdj,3))/3.14*180)
# print(singdj)

#太阳方位角
# cosfwj=(math.sin(cwj)-singdj*math.sin(39.3/360*pai))/(math.cos())
      H1=3
      A1=0.4237-0.00821*(6-H1)**2
      B1=0.505+0.00595*(6.5-H1)**2
      C1=0.2711+0.01858*(2.5-H1)**2
      G0=1366
      # print(A1,
      #       B1,
      #       C1)
      DNI=G0*(A1+B1*((math.e)**(-(C1/singdj))))
      print(DNI)









