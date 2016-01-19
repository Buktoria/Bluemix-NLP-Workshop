# IBM Bluemix Nature Langauge Classifer

---

This workshop is here to give you an introduction to IBM Bluemix and their NLP api. I have writen a simple wrapper for making http requests to their api.

## References

Feel free to use  the code that is provided in this workshop. In addition IBM offers docs for HTTP, node, and Java for this api. IBM also has a sample node application. You can play around and build off of it if you choose.

[Bluemix NLP Api Docs](https://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/natural-language-classifier/api/v1/)

[Sample Node Application](https://github.com/watson-developer-cloud/natural-language-classifier-nodejs?cm_mc_uid=04244272908614529838667&cm_mc_sid_50200000=1453044122)

[Other samples using Bluemix Api's](https://github.com/watson-developer-cloud)

## Setting up the API for your account

### Step One: Create a service

1. Log in to your Bluemix account
2. Go to API's
3. Under Watson services click on "Natural Language Classifier"
4. Click create "Create"

Addition documentation can be found [here](https://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/doc/nl-classifier/get_start.shtml)


## Create your Training Data

### Step 2: Create Training Data

Training data is in the form of a csv file. You can either use a csv editor, or just use a text editor like sublime or atom to create the files and save them as a .csv file.

[Creating your own training data references](https://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/doc/nl-classifier/data_format.shtml)

## Create a Python Application for Text Classification

### Step Three: Train a Classifier

1. Make a new python virtual environment for the tutorial in python3. You can do this by doing the following, `virtualenv -p python3 nlp_venv` Then to activate, `source nlp_venv/bin/activate`

2. Get your service credentials. To do this go to "Service Credentials"

3. Copy and paste your credentials into the tutorial file.

4. Change the file name for the csv to the one you created.

5. Run the python script by doing the following, `python tutorial.py`


## Test Your Classifier

### Step Four: Testing

1. Add your classifier_id to the "testing.py" file

2. Add some test cases to the `test_cases` list

3. Run the testing script by doing the following, `python testing.py` and be amazed
 