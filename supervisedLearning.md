# **【inductive learning】**归纳学习：

通过例子进行概念对应，而非字典方式（给出明确定义）

分类学习 classification

## 概念

- instances

	equal to (input).
	vector of value, of attributes 数值、属性的向量 to defy input space 定义输入空间
	比如：图画的像素s，收入的数值，等等

- concept

	as function 函数 or as mappings 映射 from 

- target concept

	the thing we're tying to find. it's the actual **answer**.

- hypothesis 假说

	hypothesis class 假设类：the set of all concepts（functions） that you're willing to entertain 愿意考虑的所有概念(函数)的集合

- sample 样本
	
	或者说是：training set 训练集

	需要有对应**正确**的标签

- candidate 候选者

	

- testing set 测试集

- ability of generalize 泛化能力

### 注意/理解

如果训练集和测试集使用同一个集合，被视作**作弊行为**

## 方法：

- decision tree 决策树

---

# 决策树

## 概念

### 运算符号

- AND

- OR 

	看法：linear 线性问题

- XOR

	exclusive or 异或

	TRUE xor FALSE = TRUE; FALSE xor TRUE = TRUE; TRUE xor TRUE = FALSE; FALSE xor FALSE = FALSE

	理解：要么...要么.../二者只能选择一个/生活中讲的 or 基本是 xor，比如：吃鱼还是吃鸡/

	**【泛化】**

	N 个 XOR:需要额外的规则引入，比如：parity 奇偶性（奇数ODD/odd个为 TRUE，偶数EVEN/even个为 FALSE）

	看法：exponential problem 指数问题/hard 难题/evil 邪恶/