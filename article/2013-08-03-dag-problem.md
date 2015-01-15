---
layout: post
title: dag图中定点覆盖问题
date: 2013-08-03 20:29
categories: acmicpc
---

dag值得就是有向无环图，所以我们特别的针对无环这个特性。

问题（1）最小路径覆盖问题，用最少的条数的链去覆盖掉我们所有的点，其中每一个点覆盖且仅能覆盖一次。因为无环，所以这里存在一类高效的解法，就是将原图中的点进行拆点， 然后进行二分匹配。完美解决。


问题（2）如果还是在一个dag图中，我们采用链去覆盖掉所有的点，这样子前面的二分匹配肯定是没有办法解决了。

首先联想到一种土办法。就是很明显，首先我们可以看做就是这条链可以经过这个点，但是不起到覆盖的作用，不就是和上面的覆盖一次的模型相同了吗，但是这条链又是确确实实的从这里经过了，肿么办，那么我们就将x这个顶点的所有后继到x该顶点，都连接一条边，正确性不难证明，就是如果进行朴素的这样操作，边数就达到n^2级别了，真是好恐怖，幸亏这类题目一般数据一般都不大，一般都不会丧心病狂的来卡这种时间，事实上很多次我为了简洁，直接用n^3的floyd算出两点间的距离，屡试不爽。

我们不能就仅仅满足于这种朴素的方法，根据05年任恺的论文，暂时还未学习，如果哪天需要学习了，那么来补上。

点覆盖的问题暂时到此为止，至少能满足我们的做题需求。