---
layout: post
title: 13成都A Assignment For Princess
date: 2013-11-16 20:24
categories: acmicpc
---

题意：在一个80个点的有向图中，现在已经知道了这个图的点数和边数，边的权值是从1-M,现在需要构造一张图，满足以下三个限制

(1) 从每一个点开始都可以到达另外任意一个点。

（2）从图中每一个点开始都可以回到自己。

（3） 图中的任意一个环上的权值和必须是3的倍数。

解法：这道构造题，在赛后听到了威哥他们说的解法，今天自己也是差不多这么写的，但是总是觉得怪怪的，就是刚开始我们先放一个大环罩住所有的点，然后再将其他的边加入到其中，那么大环怎么放是一个值得考虑的问题， 最后我的方法就是尽可能多的放1,2 这两种边，我也不知道为什么，然后不足的话放0补足，接下去还要插入一些剩余的边，我们就枚举pair(i,f) 然后在这个大环上如果i到f上的边权和模完3之后和我们要加的边模三属性是一样的话 ，就是可以放的，然后就把每一条边都插进去。然后就ac了 ，好奇怪 ，总觉得应该有什么更优美的方法。


    #include <stdio.h>  
    #include <algorithm>  
    #include <iostream>  
    #include <memory.h>  
    #include <vector>  
      
    using namespace std;  
      
    typedef pair<int,int> PII;  
      
    int n ,m;  
    #define maxn 85  
      
    bool use[maxn][maxn];  
    int ret[maxn][maxn];  
    vector<int> edge[3];  
    int sum[maxn];  
      
    void add(int u,int v,int w) {  
        if(v > n) {  
            ret[u][1] = w;  
            use[u][1] = use[1][u] = true;  
        }  
        else {  
            use[u][v] = use[v][u] = true;  
            sum[v] = sum[v-1] + w;  
            ret[u][v] = w;  
        }  
    }  
      
    void debug() {  
        for(int i = 1;i <= n;i++) {  
            for(int f = 1;f <= n;f++)  
                cout << use[i][f] << " " ;  
            cout << endl;  
        }  
        cout << endl;  
    }  
      
    bool seek(int val) {  
        for(int i = 1 ;i <= n;i++)   
            for(int f = 1;f <= n;f++) {  
                if(i == f)  
                    continue;  
                if(use[i][f] == true)  
                    continue;  
                int tt = 0;  
                if(f > i) {  
                    tt = sum[f] - sum[i];  
                    tt %= 3;  
                }  
                else {  
                    tt = sum[i] - sum[f];  
                    tt %= 3;  
                    tt = 3 - tt;  
                }  
                if(tt == (val % 3)) {  
                    use[i][f] = use[f][i] = true;  
                    ret[i][f] = val;  
                    return true;  
                }  
            }  
        return false;  
    }  
      
    void ans() {  
        for(int i = 1 ;i <= n;i++)  
            for(int f = 0 ;f <= n;f++)  
                if(0 != ret[i][f])  
                    printf("%d %d %d\n",i ,f, ret[i][f]);  
    }  
      
      
    bool solve() {  
        int minn = min(edge[1].size() , edge[2].size());  
        minn = min(minn , n / 2);  
        int le = n - 2 * minn;  
        if(le > edge[0].size())  
            return false;  
        for(int i = 0 ;i < minn;i ++) {  
            add(i + 1, i + 2, *(edge[1].end()-1));  
            edge[1].pop_back();  
        }  
        for(int i = 0 ;i < minn;i ++) {  
            add(minn + i + 1,minn + i + 2,  *(edge[2].end()-1));  
            edge[2].pop_back();  
        }  
        for(int i = 0;i < le ;i++) {  
            add(2 * minn + i + 1,2 * minn + i + 2, *(edge[0].end()-1) );  
            edge[0].pop_back();  
        }  
        for(int i = 0 ;i < 3;i++) {  
            int size = edge[i].size();  
            for(int f = 0 ;f < size;f++)  
                if(false == seek(edge[i][f]))  
                    return false;  
        }  
        return true;  
    }  
      
    void init() {  
        memset(use, false, sizeof(use));  
        memset(ret, 0, sizeof(ret));  
        edge[0].clear();  
        edge[1].clear();  
        edge[2].clear();  
      
        memset(sum ,0, sizeof(sum));  
        for(int i = 1;i <= m;i++)  
            edge[i%3].push_back(i);  
    }  
      
    int main() {  
        int cas;  
        cin >> cas;  
        for(int i = 0 ;i < cas;i++) {  
            cin >> n >> m;  
            printf("Case #%d:\n",i + 1);  
            init();  
            if(true == solve())  
                ans();  
            else  
                cout << "-1" << endl;  
        }  
        return 0;  
    }  
	

另外两道题目的代码：

06 
	
	#include <stdio.h>  
    #include <iostream>  
    #include <memory.h>  
    #include <queue>  
      
    using namespace std;  
      
    typedef pair<int,int> PII;  
    #define maxn 110000  
      
    PII b[maxn];  
    PII w[maxn];  
    int jb, jw;  
    int n ,m;  
      
    bool isfib[maxn];  
    int set[maxn];  
      
    int find(int x) {  
        return set[x] == x ? x : set[x] = find(set[x]);  
    }  
      
    bool solve() {  
        int minn = 0 ,maxx = 0;  
        for(int i = 1;i <= n;i++)  
            set[i] = i;      
      
        for(int i = 0;i < jb ;i++) {  
            int u = b[i].first;  
            int v = b[i].second;  
            u = find(u);  
            v = find(v);  
            if(u != v)  
                set[u] = v;  
        }  
      
        for(int i = 0;i < jw ;i++) {  
            int u = w[i].first;  
            int v = w[i].second;  
            u = find(u);  
            v = find(v);  
            if(u != v) {  
                set[u] = v;  
                minn ++;  
            }  
        }  
      
        int head = 0;  
        for(int i = 1;i <= n; i++)  
            if(set[i] == i)  
                head ++;  
        if(1 != head)  
            return false;  
      
        for(int i = 1;i <= n;i++)  
            set[i] = i;      
      
        for(int i = 0;i < jw ;i++) {  
            int u = w[i].first;  
            int v = w[i].second;  
            u = find(u);  
            v = find(v);  
            if(u != v) {  
                set[u] = v;  
                maxx ++;  
            }  
        }  
        for(int i = minn;i <= maxx;i++)  
            if(true == isfib[i])  
                return true;  
        return false;  
    }  
      
    void init() {  
        int a = 1, b = 2;   
        memset(isfib , false ,sizeof(isfib));  
        isfib[a] = true;  
        while(b < maxn) {  
            isfib[b] = true;  
            int c = a + b;  
            a = b;  
            b = c;  
        }  
    }  
      
    int main() {  
        int cas;  
        cin >> cas;  
        int u ,v, t;  
      
        init();  
      
        for(int i = 0 ;i < cas;i++) {  
            cin >> n >> m;  
            jb = jw = 0;  
            for(int f = 0 ;f < m;f++) {  
                scanf("%d%d%d",&u, &v, &t);  
                if(1 == t)  
                    w[jw ++ ] = make_pair(u,v);  
                else  
                    b[jb ++ ] = make_pair(u,v);  
            }  
            bool ret = solve();  
            printf("Case #%d: ", i + 1);  
            if(true == ret)  
                cout << "Yes" << endl;  
            else  
                cout << "No" << endl;  
        }  
        return 0;  
    }  
	
08

    #include <stdio.h>  
    #include <iostream>  
    #include <algorithm>  
    #include <memory.h>  
    #include <vector>  
    #include <string>  
      
    using namespace std;  
      
    string yu[9];  
      
    void init() {  
        yu[0] = "B]";  
        yu[1] = "KB]";  
        yu[2] = "MB]";  
        yu[3] = "GB]";  
        yu[4] = "TB]";  
        yu[5] = "PB]";  
        yu[6] = "EB]";  
        yu[7] = "ZB]";  
        yu[8] = "YB]";  
    }  
      
    int main() {  
        int a ,cas;  
        cin >> cas;  
        char ch[100];  
        init();  
        for(int i = 0 ;i < cas;i ++) {  
            scanf("%d[%s",&a,ch);  
            double l = 1;  
            for(int i = 0 ;i < 9;i++) {  
                if(yu[i] == ch)  
                    break;  
                l *= (1000.0 / 1024);  
            }  
            printf("Case #%d: %.2lf%%\n",i + 1 , 100 - 100*l);  
        }  
        return 0;  
    }  
