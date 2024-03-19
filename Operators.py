"""
    Operators:
    
        1.Arithmetic Operators: + - / * // % **
        2.Assignment Operators: =, +=, -=, *=, /=, //=, %=, **= (a = a + a = a+ = 1)
        3.Relational Operators: == != < > <= >= [This result in a boolean value]
        4.Logical Operators: and or not
        5.Membership operator - To check whether a value is present in a sequence  (list, string,tuple,dictionary) in, not in
        6.Identity Operator - is, is not
        7.Bitwise Operator - &,|, ^, ~,<<, >>


"""
colors = ['Violet','Indigo', 'Blue', 'Green', 'Yellow', 'Orange', 'Red']
print('Violet' not in colors)

b = False
print(b is not False)
print(type(b) is bool)