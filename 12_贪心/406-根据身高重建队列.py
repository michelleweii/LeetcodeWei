"""
middle 2021-12-13 贪心
https://leetcode-cn.com/problems/queue-reconstruction-by-height/solution/xian-pai-xu-zai-cha-dui-dong-hua-yan-shi-suan-fa-g/
https://leetcode-cn.com/problems/queue-reconstruction-by-height/solution/406du-shuo-shi-tan-xin-na-yao-wei-shi-yao-yong-tan/
（套路）：一般这种数对，还涉及排序的，根据第一个元素正向排序，根据第二个元素反向排序，
或者根据第一个元素反向排序，根据第二个元素正向排序，往往能够简化解题过程。
思路：
     * 解题思路：先排序再插入
     * 1.排序规则：按照先H高度降序，K个数升序排序
     * 2.遍历排序后的数组，根据K插入到K的位置上
     *
     * 核心思想：高个子先站好位，矮个子插入到K位置上，前面肯定有K个高个子，矮个子再插到前面也满足K的要求
     * 链接：https://leetcode-cn.com/problems/queue-reconstruction-by-height/solution/406-gen-ju-shen-gao-zhong-jian-dui-lie-java-xian-p/
遇到两个维度权衡的时候，一定要先确定一个维度，再确定另一个维度。
局部最优：优先按身高高的people的k来插入。插入操作过后的people满足队列属性
全局最优：最后都做完插入操作，整个队列满足题目队列属性
"""
class Solution:
    def reconstructQueue(self, people): #List[List[int]]) -> List[List[int]]:
        # 每个 people[i] = [hi, ki] 表示第 i 个人的身高为 hi ，前面 正好 有 ki 个身高大于或等于 hi 的人。
        # 按照元素 1 进行降序排序，对于每个元素，在其之前的元素的个数，就是大于等于他的元素的数量;
        # 按照第二个元素正向排序，我们希望 k 大的尽量在后面，减少插入操作的次数。[5,0]vs[5,2]
        #
        # 先按照h维度的身高顺序从高到低排序。确定第一个维度
        # lambda返回的是一个元组：当-x[0](维度h）相同时，再根据x[1]（维度k）从小到大排序
        people.sort(key=lambda x: (-x[0], x[1]))
        print(people) # [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]
        queue = []
        # 根据每个元素的第二个维度k，贪心算法，进行插入
        # people已经排序过了：同一高度时k值小的排前面。
        for p in people:
            print(p[1],p)
            queue.insert(p[1], p)
        return queue

if __name__ == '__main__':
    # people = [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]
    # [h,k]
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    print(Solution().reconstructQueue(people))