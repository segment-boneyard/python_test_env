# Python Test Env
Super simple setup with Flask to test server-side calls

### Setup
1. Clone repo
2. (optional but recommended) Set up and activate a virtualenv (see steps below).
3. Install requirements with `pip install -r requirements.txt`
4. Run file with `python test.py`. You should now see something like:
```
(venv) $ python test.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 207-260-893
 ```
 5. In a new terminal window, curl to the url listed in the previous step. You should see something like:
 ```
 $ curl http://127.0.0.1:5000/
SENT event   $
 ```
 
 ### Usage
 Update the calls and writekey as needed. Repeat step 5 each time you've made a change. Only repeat step 4 if the local server has shut down/you closed it.
 
 ## Reference
 
 ### pip
 If you don't have `pip` installed already, you should!
 
 In a nutshell, you will download get-pip.py, then run the following: `python get-pip.py`
 
 https://pip.pypa.io/en/stable/installing/
 
 ### virtualenv
 1. Install virtualenv: `pip install virtualenv`
 2. `cd` to your directory of interest. Create a virtual environement with the command `virtualenv <virtualenv_name>`. A common convention is `virtualenv venv`.
 3. Activate the virtualenv with `venv bin/src/activate`.
 4. Your commandline should now show `(<virtualenv_name>)` at the beginning of your terminal line. For instance, here's mine: `(venv) Saras-MacBook-Pro:python_segment_env sarathurman$`
