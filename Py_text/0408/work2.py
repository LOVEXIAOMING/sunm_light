import time
from multiprocessing import Pool, Manager

list2=[]

def down(num):
    list1=[]
    for i in range(3):
        list1.append("进程:"+str(num)+","+str(i))
        time.sleep(0.1)
    q.put(list1)
    print("\n"+str(list1))
def num(i):
    list2.append(q.get())
    num=len(list2)/3*100
    print("\r当前下载进度:%d%%"%num,end="")

if __name__ == '__main__':
    q = Manager().Queue()
    pool=Pool(1)
    for i in range(3):
        pool.apply_async(down,(i,),callback=num)
    pool.close()
    pool.join()