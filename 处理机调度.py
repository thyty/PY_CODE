import copy
import tabulate as ta
class jcb:
    now_time=0
    def __init__(self,name,arrtime,time):
        self.name=name
        self.time=time
        self.arrtime = arrtime
        self.sertime=0
        self.fintime=0
        self.turtime=0.0
        self.tturtime=0.0
        pass
k=[6,50,20,10,40,8]
d=[0,2,5,5,12,15]
def kk():
    i = 0
    job_list = [jcb(chr(ord('A') + i), d[i],k[i]) for i in range(6)]
    return job_list
def body(jobs,method):
    print('进程调度算法{}\t'.format(method))
    sumt=0
    sumtt=0
    table = [['作业名', '到达时间', '服务时间', '开始时间', '完成时间', '周转时间', '带权周转时间']]
    jcb.now_time = 0
    global readyf
    readyf = copy.deepcopy(jobs)
    readyf.sort(key=lambda x: x.arrtime)
    readyff = readyf[0:]
    ready=[readyf[0]]
    for dd in range(6):
        cd = []
        i = ready[0]
        print('当前时间{}\t正在运行的进程{}\t'.format(jcb.now_time, ready[0].name))
        for q in readyf:
            if i == q:
                q.sertime = jcb.now_time
                q.fintime = jcb.now_time + q.time
                q.turtime = q.fintime - q.arrtime
                jcb.now_time = q.fintime
        for w in readyff:
            if w.arrtime <= jcb.now_time :
                if w not in ready:
                    ready.append(w)
        ready.pop(0)
        while ready==[] and dd!=5:
            print(1)
            jcb.now_time+=1
            for w in readyff:
                if w.arrtime <= jcb.now_time:
                    if w not in ready:
                        ready.append(w)
        if method=='hr':
            h(ready)
        elif method=='sjf':
            s(ready)
        elif method=='fcfs':
            f(ready)
        for t in ready:
            cd.append(t.name)
        print('就绪队列{}\t'.format(cd))
        for e in readyff:
            if i==e:
                readyff.remove(e)
    for i in readyf:
        tm = [i.name, i.arrtime, i.time, i.sertime, i.fintime, i.turtime, round(i.turtime / i.time, 2)]
        table.append(tm)
    print(ta.tabulate(table, headers='firstrow', tablefmt='grid'))
    for y in range(1,7):
        sumt=sumt+table[y][5]
        sumtt=sumtt+table[y][6]
    print('平均周转时间{}\t平均带权周转时间{}\t'.format(round(sumt*1.0/6,2),round(sumtt*1.0/6,2)))
def h(re):
    re.sort(key=lambda x: (x.time+jcb.now_time-x.arrtime)/x.time,reverse=True)
def s(re):
    re.sort(key=lambda x: x.time)
def f(re):
    re.sort(key=lambda x: x.arrtime)
def main():
    jobs = kk()
    for method in ['fcfs','sjf','hr']:
        body(copy.deepcopy(jobs),method)
if __name__ == '__main__':
    main()


