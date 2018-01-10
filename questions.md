���⣺������ֵ�������󣬱����ķ�����

**����õ������ߵĽ��**

����������ʣ�**��Ϊ optimal_reg �Ǳ�����Ϊ fit_model ������ ���ң� fit_model ��������������ô��⣿���� GridSearchCV�� ���ԣ�optimal_reg Ҳ���� GridSearchCV �����ķ��� predict ?**

����Ҫע�⺯���ķ���ֵ��```fit_model``` �ķ��ش����������ģ�
```
 # �������������������ģ��
    return grid.best_estimator_
```
�����ص�������������ģ���е�����ģ�ͣ�����```best_estimator_```���ԣ�������Ķ�[�ĵ�](http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)�еĽ��ͣ�Estimator that was chosen by the search, i.e. estimator which gave highest score (or smallest loss if specified) on the left out data. Not available if refit=False.
```
# ����ѵ�����ݣ��������ģ��
optimal_reg = fit_model(X_train, y_train)
```
optimal_reg����ͨ��```fit_model```�ó���```grid.best_estimator_```������```optimal_reg.predict(X_test)```����ʹ������ģ��������Ԥ�⡣

ע���Ķ����룬�����Ĵ���ע���Լ��鿴�ĵ��ܹ���������õ������Ŀ�������㻹��Ҫע���޸Ĺ���K�۽�����֤�Ĳ��֣�׼ȷ��������㷨���̺����á�

**�����в����׵ĵط���**

- ���ʲ�����

	best_estimator_ ��������˵�� estimator ������ʲô���͵����ݣ���һ���㷨����һ��ģ���ˣ�
---