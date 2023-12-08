***Author: Sainadh Puritipati***

***To run test without reports:***
pytest tests/filename.py

***To run test with reports:***
pytest tests/filename.py --html=./filename.html

***To run in parallel mode:***
pytest tests/filename.py -v -n 3 --html=./filename.html

-v = verbose
-n = parallel execution

***To run with specific browser:***

pytest --browser chrome -v tests/test_LoginPage.py --html=./reports/login_page_report.html

