def wish(person, message):
    print(message, person)

wish('Andy', 'Good Morning')   # Positional args
wish(message = 'Hi', person = 'Mike')   # keyword args
wish(person = 'Joe', message = 'Hello')   # keyword args

wish('Jack', message = 'Hi')   # Positional and Keyword



