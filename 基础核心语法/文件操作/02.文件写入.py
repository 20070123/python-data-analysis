#1.访问文件（访问一个不存在的文件，他会自己创建；访问存在的文件，它会先清除原本存在的所有内容）
import time

f=open("E:/Develop/Python/写入.txt","w",encoding="utf-8")
#2.write写入
f.write("P5R真好玩吧")#----->将内容写到内存中
f.flush()#------->将内存中的内容全部存入硬盘文件中

# time.sleep(66666)#----->运行到这里可以看到E盘里已经创建了“写入.txt”文件，但是write的内容并没有真的写进文件
