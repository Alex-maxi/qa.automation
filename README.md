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


For running API test with Authorization
Need to create file with name "data_auth.json" in "src/config/env_config" folder.
And place in file your GitHub Authorization Token in formar:
{
    "GIT_HUB_TOKEN": "your_authorization token"
}




DOCKER RUNNING

--For creating container--
docker compose up
--For stoping container--
docker container stop selenium-hub
--For remuving container--
docker container rm selenium-hub


--For running docker container--
docker build . -t be-auto-apr
docker run --volume `pwd`/reports:/test-framework/reports -e BROWSER=remote_chrome TARGET=dev be-auto-apr


