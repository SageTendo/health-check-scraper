BASE_URL = 'https://healthcheck.higherhealth.ac.za/'
LOGIN_URL = 'https://healthcheck.higherhealth.ac.za/login/?next=/'
RECEIPT_URL = 'https://healthcheck.higherhealth.ac.za/receipt/'

STATUS = {
    # Low risk status parameters
    'green': {
        'symptoms_fever': 'no',
        'symptoms_cough': 'no',
        'symptoms_sore_throat': 'no',
        'symptoms_difficulty_breathing': 'no',
        'symptoms_taste': 'no',
        'medical_exposure': 'no',
        'medical_confirm_accuracy': 'yes'
    },
    # Mid risk status parameters
    'orange': {
        'symptoms_fever': 'no',
        'symptoms_cough': 'yes',
        'symptoms_sore_throat': 'no',
        'symptoms_difficulty_breathing': 'no',
        'symptoms_taste': 'no',
        'medical_exposure': 'no',
        'medical_confirm_accuracy': 'yes'
    },
    # High risk status parameters
    'red': {
        'symptoms_fever': 'yes',
        'symptoms_cough': 'yes',
        'symptoms_sore_throat': 'yes',
        'symptoms_difficulty_breathing': 'yes',
        'symptoms_taste': 'yes',
        'medical_exposure': 'yes',
        'medical_confirm_accuracy': 'yes'
    }
}

IMAGE_DIMENSIONS = {
    # Low risk receipt dimensions
    'green': (500, 590),
    # Mid risk receipt dimensions
    'orange': (500, 870),
    # High risk receipt dimensions
    'red': (500, 830)
}

if __name__ == '__main__':
    print(IMAGE_DIMENSIONS['green'])
