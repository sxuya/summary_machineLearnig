问题：函数赋值给变量后，变量的方法。

**【获得的审阅者的解答】**

关于你的疑问：**因为 optimal_reg 是被定义为 fit_model 函数， 而且， fit_model 的主函数（是这么理解？）是 GridSearchCV， 所以，optimal_reg 也具有 GridSearchCV 函数的方法 predict ?**

你需要注意函数的返回值，```fit_model``` 的返回代码是这样的：
```
 # 返回网格搜索后的最优模型
    return grid.best_estimator_
```
它返回的是网格搜索的模型中的最优模型，关于```best_estimator_```属性，你可以阅读[文档](http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)中的解释：Estimator that was chosen by the search, i.e. estimator which gave highest score (or smallest loss if specified) on the left out data. Not available if refit=False.
```
# 基于训练数据，获得最优模型
optimal_reg = fit_model(X_train, y_train)
```
optimal_reg就是通过```fit_model```得出的```grid.best_estimator_```，所以```optimal_reg.predict(X_test)```就是使用最优模型来进行预测。

注意阅读代码，给出的代码注释以及查看文档能够帮助你更好的理解项目，此外你还需要注意修改关于K折交叉验证的部分，准确理解它的算法过程和作用。

**【还有不明白的地方】**

- 名词不懂。

	best_estimator_ 介绍里面说的 estimator 到底是什么类型的数据？是一个算法？是一个模型了？
---