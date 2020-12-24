brew install allure	安装
allure --version
pip install allure-pytest		安装allure-pytest
pytest test_alluredemo.py --alluredir=./result/5	运行pytest测试用例，并制定测试报告地址
allure serve ./result/5	启动测试报告
allure generate ./result/ -c -o ./result/5/ --clean		生成一份测试报告，注意路径覆盖增加--clean
allure open -h 127.0.0.1 -p 8883 ./result/5


指定feature运行
pytest test_allure_story.py --allure-features '登录'
pytest test_allure_story.py --allure-stories '登录成功'
pytest -v test_allure_story.py --allure-stories '登录成功'      加-v，打印详细数据

pytest test_alluredemo_link.py --alluredir=./result/7
allure serve ./result/7 

pytest test_alluredemo_link.py --allure-link-pattern=issue:http://www.mytesttracker.com/issue{} --alluredir=./result/7


pytest test_sevenrity.py --alluredir=./result/7 --allure-severities normal,critical