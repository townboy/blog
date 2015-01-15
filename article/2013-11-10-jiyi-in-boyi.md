---
layout: post
title: 博弈搜索中的记忆化
date: 2013-11-10 19:33
categories: acmicpc
---

先看下面几道题目 
[uva 11844](http://acm.hust.edu.cn/vjudge/problem/viewProblem.action?id=23316) 
[hdu 4778](http://acm.hdu.edu.cn/showproblem.php?pid=4778)
[hdu 4753](http://acm.hdu.edu.cn/showproblem.php?pid=4753)

这几道题目都是这个类型的，但是刚开始并没有弄得十分清楚，现在拿出来整理一下。

题意：

（1）有一些方块摆在地上，alice和bob可以轮流对方块进行射击，现在射击会有随机性，随机发生三种情况，询问双方采用最优策略，询问先手胜利概率是多少？

（2）每个包中有一些颜色块，包数不超过21个，alice和bob轮流选择一个包丢入一个共享的锅中，如果现在锅中某一种颜色的的数目超过S，那么就可以获得一块魔法石通过消去S个一样的颜色块，并且可以获得一次额外的机会，现在询问双方采用最优的策略， max( Va - Vb) 是多少。

（3）现在在一个4*4的方格图中，每两个点之间可以存在有一条边，现在如果加入一条边形成一个四边形，得一分，两个四边形，得两分，双方采用最优策略，现在max（Va-Vb)


思路：

在这类问题中，一个很明显的特征，双方要求采用最优策略，这个就是一个很显然的极大极小过程搜索，将每一步转化成一个状态，然后配合上极大极小搜索的剪枝利器，alphabeta剪枝，代码框架如下 

    int alphabeta(State &s,int player ,int alpha,int beta) {  
        if(s.isfinal())  
            return s.score;  
      
        vector<State> children;  
        s.expand(player, children);  
          
        int n = children.size();  
        for(int i = 0;i < n;i++ ) {  
            int v = alphabeta(children[i] , 1 - player, alpha,beta);  
            if(0 == player)  
                alpha = max(alpha ,v);  
            else  
                beta = min(beta, v);  
            if(beta <= alpha)  
                break;  
        }  
        return !player ? alpha : beta;  
    }  
	
这就是一个极大极小搜索加上alphabeta剪枝之后的代码。

在以上几道题目中，这个算法无情的tle了。

仔细看这个算法，几乎将所有状态遍历了一遍，但是拿第二道题为例来看，如果将每一个包看成一个资源，那么消耗掉相同的资源之后，不论前面的得分是怎么样的，现在锅中的状态是确定的，那么接下去先手的人一定会采用对他来说最有利的策略，所以这里不就是搜了很多次了嘛？

所以这个地方可以用记忆化的方法记录下来，框架还是采用alphabeta搜索的框架，对接下去的状态采用最优选择策略并记录下来。

那么他和alphabeta这个算法看着确实很像，但是还有一些细节差距。

先放代码

    int dfs(State s) {  
        if(INF != dp[s.s])  
            return dp[s.s];  
        if(all == s.s)  
            return dp[s.s] = 0;  
      
        vector<State> children;  
        vector<int > score;  
      
        s.expand(children, score);  
      
        int n = children.size();  
        int ret = -INF;  
      
        for(int i = 0;i < n; i++) {  
            int ans = dfs(children[i]) + score[i];  
            ret = max(ret ,ans);  
        }  
        return dp[s.s] = ret;  
    }  
	
是不是和alphabeta代码很像啊，确实。

因为这个算法就是在之间的搜索上改的，按照我们普通的思想进行了记忆化，这里要注意的是，现在dfs往下走的时候 我们就不用当前路径上的得分了，因为这些状态其实是不确定的，我们这里计算的时候之后的路径上的最优解，在取最优值的时候需要加上当前这步的收获减去后继的dp值，为什么？因为我们这里定义的都是当前步的先手拿的最大获利，而到了最终态的时候，因为是后继路径的最大值，所以我们return 0；这样递归上去就可以得出正解。

需要注意的是，这样的优化之后就不能使用alphabeta剪枝，而且只能适用于个数较小的时候，否则状态太大，而且必须是前面的状态不会影响到后面的状态才行，否则就不符合记忆化的初衷了。
