from NLP_Bluemix_Interface import NLPWatsonInterface
from tutorial import username, password

nlp_classifier = NLPWatsonInterface(username, password)
classifier_id = ''

test_cases = [
    ('Is it cold?', 'temperature'),
    # ...
]

tot = 0

if __name__ == '__main__':

    for case in test_cases:
        result = nlp_classifier.classify(classifier_id, case[0])
        print(str(result), case[1])

        if result['top_class'] == case[1]:
            tot += 1

    print('Done with a score of : ' + str(tot/len(test_cases)))
