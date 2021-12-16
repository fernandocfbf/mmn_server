from datetime import datetime


def get_datetime():
    '''
    input: empty
    output: datetime string
    description: returns the current datetime
    '''
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
