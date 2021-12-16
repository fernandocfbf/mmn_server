def create_log(text, type):
    '''
    input: text to be printed and type (warning, success, info, error)
    output: empty
    description: prints the desired text building a log
    '''
    print("{0}: {1}".format(type, text))