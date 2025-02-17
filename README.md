### 关于CS61A中的注意点和难点

#### 1、Cats中的Problem 7

差不多算是课程前中期top难度的问题，不过题目给了模版框架，给了思路上的提示。

这里我的解决思路是：

1. 若typed或source为对方的子串，我们只需add或remove掉typed与source不同的地方即可，也就是两者长度差次操作。
2. 其他情况，我们用截取并递归的方式从头遍历typed的每个字符，每次比较typed的第一个字符与source的第一个字符，若相同那么我们直接截取typed与source第一个字符后面的部分进行递归即可`minimum_mewtations(typed[1:], source[1:], limit)`。
3. 若两者第一个字符不同那么我们就要对typed进行操作，依次递归三种操作，取最小操作数即可。
4. 注意Python中的字符串是可以像list一样使用`s[:]`进行浅拷贝拆分的

```python
def minimum_mewtations(typed, source, limit):
    if typed in source or source in typed:
        return abs(len(source) - len(typed))
    if limit < 0: return 0
    if typed[0] == source[0]: return minimum_mewtations(typed[1:], source[1:], limit)
    else:
        add = 1 + minimum_mewtations(typed, source[1:], limit - 1)
        remove = 1 + minimum_mewtations(typed[1:], source, limit - 1)
        substitute = 1 + minimum_mewtations(typed[1:], source[1:], limit - 1)
        return min(add, remove, substitute)
```



#### 2、lab06的Q3，Q4

这两个问题并不难，但是要注意一点，Q3中的`make_change(amount, coins)`，是**不能直接修改coins**的，如果你直接修改coins，依旧可能过Q3的测试，但是Q4中会用到这个函数，由于修改coins而导致错误。
