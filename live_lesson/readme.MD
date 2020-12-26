pip install pytest-rerunfailures    失败重跑
pytest -vs test_rerun.py --reruns 3 -delay 1


pip install pytest-assume   断言支持，多重判断
pytest.assume(1 == 2)
    pytest.assume(True == True)
    pytest.assume(100 == 200)
    
pip install pytest-ordering 指定pytest执行顺序
@pytest.mark.run(order=1)
@pytest.mark.first

pip install pytest-xdist



