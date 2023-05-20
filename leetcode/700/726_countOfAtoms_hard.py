'''
726. 原子的数量
给定一个化学式formula（作为字符串），返回每种原子的数量。

原子总是以一个大写字母开始，接着跟随0个或任意个小写字母，表示原子的名字。

如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。例如，H2O 和 H2O2 是可行的，但 H1O2 这个表达是不可行的。

两个化学式连在一起是新的化学式。例如 H2O2He3Mg4 也是化学式。

一个括号中的化学式和数字（可选择性添加）也是化学式。例如 (H2O2) 和 (H2O2)3 是化学式。

给定一个化学式，输出所有原子的数量。格式为：第一个（按字典序）原子的名子，跟着它的数量（如果数量大于 1），然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。

示例 1:

输入:
formula = "H2O"
输出: "H2O"
解释:
原子的数量是 {'H': 2, 'O': 1}。
示例 2:

输入:
formula = "Mg(OH)2"
输出: "H2MgO2"
解释:
原子的数量是 {'H': 2, 'Mg': 1, 'O': 2}。
示例 3:

输入:
formula = "K4(ON(SO3)2)2"
输出: "K4N2O14S4"
解释:
原子的数量是 {'K': 4, 'N': 2, 'O': 14, 'S': 4}。

'''
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        self.i = 0
        n = len(formula)

        # 词法分析，读取下一个词元
        def nextTerm():
            if self.i == n:
                return None
            if formula[self.i].isupper():  # 原子名
                j = self.i + 1
                while j < n and formula[j].islower():
                    j += 1
                start = self.i
                self.i = j
                return formula[start:j]
            if formula[self.i].isdigit():  # 数字
                j = self.i + 1
                while j < n and formula[j].isdigit():
                    j += 1
                start = self.i
                self.i = j
                return int(formula[start:j])
            if formula[self.i] == '(':
                self.i += 1
                return '('
            if formula[self.i] == ')':
                self.i += 1
                return ')'

        import collections

        # 原子表达式解析
        def expr():
            counter = collections.Counter()
            term = nextTerm()
            atom = None
            while term:
                if isinstance(term, int):  # 如果是数值，需要将当前原子数增加
                    counter[atom] += term - 1
                    term = nextTerm()
                elif term == '(':
                    subcounter = expr()  # 如果是左括号，进入子表达式处理
                    term = nextTerm()
                    if isinstance(term, int):  # 如果子表达式后面跟着数值，需要将子表达式计数器乘以数值
                        for a, c in subcounter.most_common():
                            subcounter[a] = c * term
                        term = nextTerm()
                    counter.update(subcounter)  # 将子表达式的计数器更新到当前计数器里面
                elif term == ')':  # 如果是右括号，将当前表达式的计数器返回给上级
                    return counter
                else:  # 如果是原子，计数器中增加1个原子
                    atom = term
                    counter[atom] += 1
                    term = nextTerm()
            return counter

        # 对计数器中的原子按照字典序进行排序后输出
        counter = expr()
        ans = []
        for atom, count in sorted(counter.most_common(), key=lambda item: item[0]):
            ans.append(atom)
            if count > 1:
                ans.append(str(count))
        return ''.join(ans)


