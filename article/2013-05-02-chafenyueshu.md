---
layout: post
title: 差分约束 小结
date: 2013-05-02 12:35
categories: acmicpc
---

刚开始学差分约束的时候 总觉得很矛盾，一方面觉得很矛盾，不就是建个图跑最短路吗，可以一看到题目基本都傻眼了，这尼玛怎么建图啊，怎么跑啊。找了网上的不少资料，很多人重复说这么一句话“最小值跑最长路，最大值跑最短路”。咋一看还确实挺有道理，但是这又是为什么呢。

这几天做了几道差分约束之后，感受稍微深刻了一下，写一下自己的总结。

“最小值跑最长路，最大值跑最短路” 这句话是不准确的，因为其实这两种方法是互通的。在这里随便举个例子。如果要求dis[t] 和 dis[1] 之间的最小值，假设dis[t] 比dis[1]要大，那么我们的答案就是 dis[t] >= dis[1]+ans; 这里的ans就是答案，所以我们可以将dis[1] 赋成0，然后从1开始作为源点开始跑最长路，这样跑出来的答案就是ans，当然其中所有的点都要按照大于号的形式来建图。另外一种方法就是将答案转化为dis[1] <= dis[t] -ans 那么这个时候需要将图中的边改成小于号，也就是说反向并且权值取反，从dis[t] 赋成0 开始跑最短路，那么跑出来的dis[1] 再取反就是答案。

从这个例子可以清晰的看出，差分约束就是在将约束条件整理出来，然后合理的建图再根据需求进行计算就可以了。