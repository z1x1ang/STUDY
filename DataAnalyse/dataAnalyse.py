#Rounding
import math
from decimal import *
if __name__=="__main__":
 #输入精确后的数字
 #该算法只能计算小数(小数位不全是0)
 a= Decimal(input('输入经过四舍五入的数字：'))
 # 分析小数点位数
 len=len(str(a).split(".")[1])
 b=0.5*(10**(-len))
 b=Decimal(str(b))
 print('{0}≤x*<{1}'.format(a-b,a+b))
 print('绝对误差限{0},相对误差限{1}'.format(b,b/a))