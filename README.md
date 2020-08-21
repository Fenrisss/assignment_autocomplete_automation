# Task#2 
This repo contains the implementation of the assignment. 
Please follow the instructions to run the tests on linux machine with python3.

0) Have pip installed `sudo apt install python3-pip`
1) Install the required libs by running the command in the project directory `pip install -r requirements.txt` 
2) [Download](https://chromedriver.storage.googleapis.com/index.html?path=84.0.4147.30/) and export the chromedriver into the project directory
3) Install chromium browser with `sudo apt-get install chromium-browser`
3) Put the project directory path into the parameter `driver_path` in `conftest.py`<br>
    * Please update accordingly the values of the parameters `filepath1`, `filepath2`, `filepath3` in ```test.py```
4) Run the following command to start the tests `pytest -v test.py`<br>
    * The screenshots of the tests keep being updated everytime the tests start
