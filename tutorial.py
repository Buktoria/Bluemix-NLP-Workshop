import time

from NLP_Bluemix_Interface import NLPWatsonInterface

username = ""
password = ""
training_data = open('weather_data_train.csv', 'rb')
metadata = "{\"language\":\"en\",\"name\":\"TutorialClassifier\"}"

nlp_classifier = NLPWatsonInterface(username, password)

if __name__ == '__main__':

    # First train your classifier
    response = nlp_classifier.train(training_data, metadata)

    print(response)

    # Check status till its done training
    training_status = response['status']

    # Quit if request didn't go through
    if training_status != 'Training':
        exit()

    # poll for status update
    while training_status == 'Training':
        time.sleep(15)

        training_status = nlp_classifier.status(response['classifier_id'])['status']

        print('Status: ' + training_status)

    print('Done')
