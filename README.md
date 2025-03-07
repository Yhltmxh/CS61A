# 关于CS61A中的注意点和难点

## 1、Cats中的Problem 7

差不多算是课程前中期top难度的问题，不过题目给了模版框架，给了思路上的提示。

这里我的解决思路是：

1. 若typed或source为对方的子串，我们只需add或remove掉typed与source不同的地方即可，也就是两者长度差次操作。
2. 其他情况，我们用截取并递归的方式从头遍历typed的每个字符，每次比较typed的第一个字符与source的第一个字符，若相同那么我们直接截取typed与source第一个字符后面的部分进行递归即可`minimum_mewtations(typed[1:], source[1:], limit)`。
3. 若两者第一个字符不同那么我们就要对typed进行操作，依次递归三种操作，取最小操作数即可。
4. 注意Python中的字符串是可以像list一样使用`s[:]`进行浅拷贝拆分的。

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

## 2、lab06的Q3，Q4

这两个问题并不难，但是要注意一点，Q3中的`make_change(amount, coins)`，是**不能直接修改coins**的，如果你直接修改coins，依旧可能过Q3的测试，但是Q4中会用到这个函数，由于修改coins而导致错误。

## 3、Ants中的Problem 5和Problem 9

这两个问题中都涉及到对同一个place的所有bee攻击的操作，题目提示对于place.bees要进行拷贝后遍历，不然某个bee被移除后遍历会出现问题，而对于这段操作有个问题值得思考，那就是我们遍历的是拷贝的新列表的元素，而为何能通过拷贝的元素移除原列表的元素且对新列表无影响呢？

```python
# 上述操作
bees = list(self.place.bees)
for bee in bees:
    bee.reduce_health(self.damage)
    
    
# Insert类中的reduce_health方法
def reduce_health(self, amount):
    self.health -= amount
    if self.health <= 0:
        self.zero_health_callback()
        self.place.remove_insect(self)
  

# Place类中的remove_insect方法
def remove_insect(self, insect):
    insect.remove_from(self)

    
# Bee类中的remove_from方法
def remove_from(self, place):
    place.bees.remove(self) # 将bee从原列表中删除
    super().remove_from(place)
```

解释：

- 可以看到bee最终是通过`list.remove(x)`删除的，在 Python 中，当使用 `list.remove(x)` 方法删除一个元素时，列表是根据元素的 `==` 比较（值比较）来判断是否匹配，而不是根据对象的地址（即 `is` 比较）。如果对象未重写 `__eq__` 方法，默认使用 `is` 比较（即对象的地址），如果对象重写了 `__eq__` 方法，则根据自定义的规则判断。
- 而Bee类中未重写 `__eq__` 方法，因此这里`remove`是通过比较对象的地址来找到list中要删除的对象。
- 使用`list(self.place.bees)`来拷贝列表其实是浅拷贝，它只会将每个对象元素的索引（也就是地址）拷贝到新列表中，因此新旧列表中对应的元素所指向的都是同一个对象
- 而我们进行`remove`时只会将list中的对象索引移除，该对象仍然存在于内存中，直到没有其他引用指向它时，Python 的垃圾回收机制才会释放其占用的内存。又因为新列表中的对象索引保留了，故我们依旧可以通过新列表的索引找到这个对象。

## 4、Scheme解释器中的Problem 9和Optional Problem

1. Problem 9的实现是有一定难度的，需要仔细思考整个函数递归调用栈帧的创建过程，考虑嵌套的lambda调用和普通函数递归调用时环境细节
2. 尾递归优化要注意哪些使用到`scheme_eval`的地方要将第三个参数改为`True`，如`if, and, or`等的实现，以及要注意有些地方不能使用尾递归的地方改为`True`会出现问题
3. `let-to-lambda`注意要递归实现，可以灵活使用`引用，反应用，准引用`，以及`cons`来构建链表
