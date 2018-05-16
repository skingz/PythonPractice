
#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import math
import time
import calendar
import string
# import datetime
from test.test_math import math_testcases
from _datetime import datetime
from _functools import reduce

class ExampleClass(object):
    '''
    classdocs
    '''


#     def __init__(self):
#         '''
#         Constructor
#         '''
       
    def test(self):
        print("this is a test"); 
        
    # ���ĸ����֣�1��2��3��4������ɶ��ٸ�������ͬ�����ظ����ֵ���λ�������Ƕ��٣�
    def prac_1(self):
        num=0;
        for i in range(1,5):
            for j in range(1,5):
                if(i==j):
                    continue;
                for k in range(1,5):
                    if (i==k) or (k==j):
                        continue;
                    num=num+1;
                    print (i,j,k);

        print("total order num is",num);
        
    def prac_2(self,income):
        pro=0;
        money=[100,60,40,20,10,0];
        rat=[0.01,0.015,0.03,0.05,0.075,0.1];
        for i in range(0,6):
            if(income>money[i]):
                pro+= (income-money[i])*rat[i];
                print(pro);
                income=money[i];
        print(pro);
        
    def prac_3(self):
        n=11;
        while(1):
            x=math.pow(n,2)-100;
            m=math.sqrt(x+100+168);
            if(math.floor(m)==m):
                print(x);
                break;
            n+=1;
            
    def prac_4(self,year,month,day):
        if(year<1900):  print("year is error.."); return;
        if(month<1 or month>13): print("month is error.."); return;
        isRunNian=((year%4)==0);
        tmp2mdays=0;
        if(isRunNian):  tmp2mdays=29;
        else: tmp2mdays=28;
        monthDays= (0,31,tmp2mdays,31,30,31,30,31,31,30,31,30,31);
        currentMonthday=monthDays[month];
        if(currentMonthday<day):print("day is error.."); return;
        totalDays=day;
        for i in range(1,month):
            totalDays+=monthDays[i];
        print(year,month,day,"is ..", totalDays);
        
    def prac_5(self,oldArr):
        if(type(oldArr)==list ):
            oldArr.sort();
            print(oldArr);
        else: print(type(oldArr),"is not surpoted");
        
    def prac_6(self,lastIndex):
        pre0=0;pre1=1;
        print(pre0,pre1);
        for i in range(2,lastIndex):
            if(i%2==1):pre1+=pre0;print(pre1);
            else :pre0+=pre1;print(pre0);
            
    #��� 9*9 �˷��ھ���
    def prac_8(self):
        for i in range(1,10):
            print("");
            for j in range(1,i+1):
                print ("%d*%d=%d" %(i,j,i*j),end=' ');
                
    def prac_10(self):
        print( time.strftime('%Y-%m-%d %H:%M:%S') );
        time.sleep(1);
        print( time.strftime('%Y-%m-%d %H:%M:%S') );
        
    #�ŵ����⣺��һ�����ӣ��ӳ������3������ÿ���¶���һ�����ӣ�С���ӳ����������º�ÿ��������һ�����ӣ��������Ӷ���������ÿ���µ���������Ϊ���٣�
    def __prac_11_1(self,rabAge):
        num=1;
        if(rabAge>2): 
            for i in range(1,rabAge-1):
                num+=self.__prac_11_1(i);
        return num;
        
    def prac_11(self,monthIndex):
        for i in range(1,monthIndex+1):
            print(self.__prac_11_1(i));
            
    # �ж�101-200֮���ж��ٸ����������������������
    def prac_12(self):
        for i in range(101,201):
            tmp=int(math.sqrt(i));
            have=0;
            for j in range(2,tmp+1):
                if(i%j==0): have=1;break;
            if(have==0):print(i);
            
    #��ӡ�����е�"ˮ�ɻ���"����ν"ˮ�ɻ���"��ָһ����λ�������λ���������͵��ڸ�������
    def prac_13(self):
        for i in range(100,1000):
            num1=int(i/100);
            num2=int(i/10)%10;
            num3=i%10;
            if((math.pow(num1,3)+math.pow(num2,3)+math.pow(num3,3))==i ):
                print(i);
        print("end...");
        
    #��һ���������ֽ������������磺����90,��ӡ��90=2*3*3*5��
    def prac_14(self,num):
        limN=int(num/2);
        isFound=0;
        for i in range(2,limN):
            if(num%i==0):print(i);isFound=1;self.prac_14(int(num/i));  break;
        if(isFound==0):print(num);
        
    #���������������Ƕ������ɴ��⣺ѧϰ�ɼ�>=90�ֵ�ͬѧ��A��ʾ��60-89��֮�����B��ʾ��60�����µ���C��ʾ
    def prac_15(self,num):
        if(num>=90):print("A");
        elif(num>60):print("B");
        else:print("C");
        
    #���ָ����ʽ������
    def prac_16(self):
        print(calendar.month(2016,3));
        print(time.strftime("%d-%m-%y",time.localtime()));
        print(datetime.now());
        print(datetime.strftime(datetime(2016,3,6),"%d--%m--%Y"));
        
    #����һ���ַ����ֱ�ͳ�Ƴ�����Ӣ����ĸ���ո����ֺ������ַ��ĸ���
    def prac_17(self):
        s=input("please input your string:\n");
        for c in s:
            if c.isalpha():print("a",end=' ');
            elif c.isspace():print("is empty",end=' ');
            elif c.isnumeric():print("is 0",end=' ');
            else: print(" is other ",end=' ');
        
    #��s=a+aa+aaa+aaaa+aa...a��ֵ������a��һ�����֡�����2+22+222+2222+22222(��ʱ����5�������)������������ɼ��̿��ơ�
    def prac_18_1(self):
        num=int(input("please input the base num:"));
        rtimes=int(input("the repeat times:"));
        total=0;
        for i in range(1,rtimes+1):
            tmp=0;
            for j in range(0,i):
                tmp+=math.pow(10, j)*num;
            print("+%d" %(tmp),end="");
            total+=tmp;
        print("=",total);
    def prac_18(self):
        num=int(input("please input the base num:"));
        rtimes=int(input("the repeat times:"));
        arr=[];
        uu=0;
        for i in range(rtimes):
#             uu+=math.pow(10, i)*num;
#             arr.append(uu);
            uu+=num;
            num*=10;
            arr.append(uu);
        print(arr);
        print(reduce(lambda x,y:x+y,arr));
    
    def prac_19_1(self,num):
        limN=int(num/2);
        arr=[];
        isFound=0;
        for i in range(2,limN):
            if(num%i==0):arr.append(i);isFound=1;arr+=self.prac_19_1(int(num/i));  break;
        if(isFound==0):arr.append(num);
        return arr;
    #һ�������ǡ�õ�����������֮�ͣ�������ͳ�Ϊ"����"������6=1��2��3.����ҳ�1000���ڵ���������
    def prac_19(self):
        for i in range(2,1000):
            arr=[];
            limN=int(i/2);
            for j in range(1,limN+1):
                if(i%j==0):arr.append(j);
#             print(i,arr);
            if((i)==reduce(lambda x,y:x+y,arr)):
                print(i,arr);
                
    #һ���100�׸߶��������£�ÿ����غ�����ԭ�߶ȵ�һ�룻�����£������ڵ�10�����ʱ�������������ף���10�η�����ߣ�
    def prac_20(self):
        height=100;
        total=0;
        for i in range(1,11):
            total+=height;
            height/=2;
            total+=height;
#             print(height,total);
        print(height,total);
        
    #���ӳ������⣺���ӵ�һ��ժ�����ɸ����ӣ���������һ�룬����񫣬�ֶ����һ���ڶ��������ֽ�ʣ�µ����ӳԵ�һ�룬�ֶ����һ�����Ժ�ÿ�����϶�����ǰһ��ʣ�µ�һ����һ��������10���������ٳ�ʱ����ֻʣ��һ�������ˡ����һ�칲ժ�˶��١�
    def prac_21(self):
        num=1;
        for i in range(9):
            num=(num+1)*2;
        print(num);
        
    def prac_22(self):
        arr=['x','y','z'];
        arr1=arr.copy();arr1.remove('x');
        arr2=arr1.copy();arr2.remove('z');
        print(arr1,arr2);
        for a in arr1:
            for c in arr2:
                for b in arr:
                    if((a!=c) and(a!=b) and (b!=c)) : print(a,b,c);
                
    def prac_23(self):
        num=11;
        for i in range(num):
            rownum=i*2+1;
            if(rownum>num):rownum=(num-i-1)*2+1;
            rowbnum=int((num-rownum)/2);
            for m in range(rowbnum):
                print(" ",end='');
            for j in range(rownum):
               print("*",end='');
            print("");
    def prac_24(self):
        arr=[1,2];
        total=2;
        for i in range(2,21):
            arr.append(arr[i-2]+arr[i-1]);
            total+=arr[i]/arr[i-1];
        print(arr,total);