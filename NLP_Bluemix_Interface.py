import requests #http://docs.python-requests.org/en/latest/user/quickstart/


class NLPWatsonInterface(object):

    def __init__(self, username, password):
        self.url = "https://gateway.watsonplatform.net/natural-language-classifier/api/v1/classifiers"
        self.auth = requests.auth.HTTPBasicAuth(username, password)

    def train(self, taining_data, metadata):
        files = {
            'training_data': taining_data,
            'training_metadata': metadata
        }
        response = requests.post(
            self.url,
            auth=self.auth,
            files=files,
        )
        return response.json()

    def status(self, classifier_id):
        response = requests.get(
            url=self.url + '/' + classifier_id,
            auth=self.auth,
        )
        return response.json()

    def delete(self, classifier_id):
        response = requests.delete(
            url=self.url + '/' + classifier_id,
            auth=self.auth,
        )
        return response.json()

    def list_classifier(self):
        response = requests.get(
            url=self.url,
            auth=self.auth,
        )
        return response.json()

    def classify(self, classifier_id, text):
        response = requests.get(
            url=self.url + '/' + classifier_id + '/classify',
            auth=self.auth,
            params={'text': text},
        )
        return response.json()
