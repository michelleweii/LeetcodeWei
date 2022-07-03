# 贪心

## 252. 会议室

求一个人能否参加完所有会议。

> 根据第一维度升序，第二维度不管。
>
> ```
> intervals.sort(key=lambda x: x[0])
> ```

如果是`[[15, 10], [15, 20], [15, 30]]`，则是2维都升序。

## 253. 会议室2

需要几个会议室。

> 两个维度都升序。`intervals.sort()`。
>
> 如果下一个会议开始了，上一个还没有结束，会议室++。更新结束时间。

## [406. 根据身高重建队列](https://leetcode.cn/problems/queue-reconstruction-by-height/)

```python
people.sort(key=lambda x: (-x[0], x[1])) # 一维降序，二维升序
```



## [435. 无重叠区间](https://leetcode.cn/problems/non-overlapping-intervals/)

返回 *需要移除区间的最小数量，使剩余区间互不重叠* 。

> 两个维度都升序。`intervals.sort()`。
>
> 如果发生重叠，需要移出区间++。重置右边界。

## [452. 用最少数量的箭引爆气球](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/)

> `points.sort(key=lambda x: x[0])` # 按照第一个元素升序，左边界排序。
>
> 两个元素不挨着，则说明需要+1个箭。

## [1288. 删除被覆盖区间](https://leetcode.cn/problems/remove-covered-intervals/)

> `intervals.sort(key=lambda x:(x[0],-x[1]))`第1维升序，第2维降序。
>
> 求被覆盖个数。

