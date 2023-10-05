#!/usr/bin/python3
if __name__ == "__main__":
    '''
    import hidden_1
    '''
    import hidden_4
    """
     prints all the names defined by the compiled module hidden_4.pyc
    """
    for name in dir(hidden_4):
        if not name.startswith('__'):
            print(name)
