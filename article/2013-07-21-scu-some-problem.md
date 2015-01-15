---
layout: post
title: 叉姐专场小记(scu4290-4299)
date: 2013-07-21 16:42
categories: acmicpc
---

4290 [Xor](http://cstest.scu.edu.cn/soj/problem.action?id=4290)   :

题意：给定A集合和B集合，集合中的个数都是奇数个，询问是否存在x使得A集合中的每个数字异或后 使得和B集合相同。刚开始没看懂是集合，坑了很久。

刚开始不会做，被点播了，因为异或，所以a1^x ^a2^x .... ^b1 ^ b2 = 0;又因为x奇数个，所以可以直接计算出x的数字，当然这个是计算出来的，然后再一遍，验证这个x是否成立。


4291 [Triangles](http://cstest.scu.edu.cn/soj/problem.action?id=4291): 先放着。


4292 [Transform](http://cstest.scu.edu.cn/soj/problem.action?id=4292) : 

题意：给定起点数字和终点数字，然后每次操作可以加上自己的约数，包括1和自己，问最少的次数从起点到达终点。

刚开始想烦了，直接筛选法处理出每个数字的约数，然后直接bfs.


4293：[Product](http://cstest.scu.edu.cn/soj/problem.action?id=4293) 还没看。


4294: [Permanent](http://cstest.scu.edu.cn/soj/problem.action?id=4294) 还没看。


4295: [Path](http://cstest.scu.edu.cn/soj/problem.action?id=4295)

题意，给定一个10^5的树，然后10^5的询问是否存在某一个长度的路径，其中树的边长是1或者2.


4296:[multiplication](http://cstest.scu.edu.cn/soj/problem.action?id=4296)

题意：给定A序列和B序列，计算C序列，C序列的规则是一个累和的乘积，直接处理处前面的和。O(n)


4297:[Matching](http://cstest.scu.edu.cn/soj/problem.action?id=4297)

解法： 带花树 模板题


4298:[cut](http://cstest.scu.edu.cn/soj/problem.action?id=4298)

题意：给定一颗树，10^5个顶点，要求能割去的最多的边使得每个连通分量都是偶数个顶点，保证整棵树是偶数个顶点。

解法：仔细一想，直接做一次dfs，对于下面的字数，能割掉的就 割掉，否则剩到上面父节点处理，递归上来就好。


4299:[component](http://cstest.scu.edu.cn/soj/problem.action?id=4299)

题意，给定一颗2000个节点的树，问1-n个数量的连通分量的最小点权是多少。

解法：想了一个N^3的树形dp，然后发现复杂度略高，赛后一看ac代码就是这么做的，dp[i][j]代表i为根的子树，j个顶点的连通分量的最小权值。直接把这个数组合并处理上来就好。
