**PYTEST FRAMEWORK**
1. File name should be starts with test_*.py or ends with *_test.py.
2. Methods or Functions also must contain "test" keyword.
3. To run multiple tests:
   Step 1: Open Command Prompt
   Step 2: Go to Location
   Step 3: Enter "pytest"
4. For grouping tests -> use @pytest.mark.group_name (Decorator)
   To run group of Tests -> pytest -m group_name
5. To know the list of buit-in markers
   pytest --markers
