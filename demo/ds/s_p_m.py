d = {'uname' : 'scott', 'age' : 20}

match d:
    case {'name' : uname, 'age' : age}:
        pass
    case {'firstname' : uname, 'year' : age}:
        pass
    case {'uname' : uname, 'age' : age}:
        pass

print(uname, age)
