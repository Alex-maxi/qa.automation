For changing environment need to update "src.config.config.py" file. Add 'self.register("new_env_var") if needed.'
Also add environment data in files 'dev.json' or 'qa.json'. Be default used 'dev.json' file.

To SET Environment before test(tests) in terminal, use command:
        TARGET='qa' pytest .
        TARGET='dev' pytest .

For changing single variable execute like in example:
        BASE_URL_API='some_new_url' pytest . 
 
For running all tests execute command in terminal:
        pytest .

For running single test file execute command in terminal:
        pytest tests/file_name.py

For running tests using mark:
        pytest -m mark_name
