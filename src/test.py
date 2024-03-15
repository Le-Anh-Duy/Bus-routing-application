def get_keys(obj):
    if isinstance(obj, dict):
        return list(obj.keys())
    else:
        return [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

# Example usage:
# Suppose you have an object named 'my_object'

# If it's a dictionary-like object:
my_dict = {'key1': 1, 'key2': 2, 'key3': 3}
print(get_keys(my_dict))  # Output: ['key1', 'key2', 'key3']

# If it's a custom object:
class MyClass:
    def __init__(self):
        self.attribute1 = 'value1'
        self.attribute2 = 'value2'
        self.attribute3 = 'value3'

my_object = MyClass()
print(get_keys(my_object))  # Output: ['attribute1', 'attribute2', 'attribute3']
