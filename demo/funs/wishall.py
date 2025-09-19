def wishall(*names, message='Hello'):
    for n in names:
        print(message, n)


wishall('Martin', 'Mike', 'Jason', message = 'Hi')
wishall('Jack', 'Mark')




