# Prim算法

[Prim算法详解](https://www.cnblogs.com/ggzhangxiaochao/p/9070873.html)

## 算法的目的

给一个（无向）连通图，找一棵树，  
这个树也是个连通的子图  
这个树各个边的权和最小

## 算法的应用

为一个城市群，建立相互连通的公路  
建立最短的、能互相通信的通道

## 算法核心思想

每次只找一条边，一条可连通的，最“短”的边

## 算法简单描述

1. 输入：一个加权连通（无向）图，其中顶点集合为V，边集合为E；

2. 初始化：Vnew = {x}，其中x为集合V中的任一节点（起始点）

3. 重复下列操作，直到Vnew = V：  
在集合E中选取和Vnew中的元素接连、且权重最小的边，注意新边的俩个点不能在Vnew中  
如果存在有多条满足前述条件即具有相同权值的边，则可任意选取其中之一
将此边所接连的新的点加入集合Vnew中，

4. 输出：使用集合Vnew和Enew来描述所得到的最小生成树。

具体的应用，见
[1-最低消耗](/0-OnlineJudge/13-2020秋季第十一次练习/1-最低消耗.py)
