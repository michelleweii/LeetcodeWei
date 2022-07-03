# 思路是使用栈，将对应的字符通过字典映射为数字，只要求数字和为0即可

# 思路2用一个字典的数据类型，来实现与栈顶元素做匹配，dic={')':'(','}':'{',']':'['}
# （这里注意一下，key是right，value是left）
#
# 举个例子：[({})]
# [入栈，(入栈，{入栈，}是right的元素，弹出现在栈的栈顶元素stack[-1]，
# 与dic中key为}的值做一个匹配，如果stack[-1]不等于dic的value，则返回false，如果值相等，匹配成功，返回True
#
# 弹出栈顶元素，剩下的一次类推。知道所有元素出栈后，如果这时栈还有元素，则返回False。
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 注意空串是ture
        if len(s)%2 != 0:
            return False
        dicts = {'(':')','{':'}','[':']'}
        stack = []
        for key in s:
            if key in dicts:
                stack.append(key)
            else:
                # }是right的元素，弹出现在栈的栈顶元素stack[-1]
                # 如果栈不空，弹出栈顶元素
                # 对比栈顶元素是否是当前元素的配对元素
                if not stack or key != dicts[stack.pop()]:
                    return False
        return stack==[]

if __name__ == '__main__':
    s = "()[]{]"
    print(Solution().isValid(s))