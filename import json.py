## Programming Challenge 3

def get_value(nested_object, nested_key):
    object_value = nested_object
    for key in nested_key:
        object_value = object_value.get(key, None)
        if object_value is None:
            return None
    return object_value

def get_val(nested_object):
    for k in nested_object.keys():
        print(k)
        print(nested_object.values().key())


print(get_val({"a": {"b": {"c": "d"}}}))

## To test enter object and key like below syntax
# print(get_value(anyobject,[key]))

##Valid Key Test case
print(get_value({"a": {"b": {"c": "d"}}}, ["a", "b", "c"]))
print(get_value({"x": {"y": {"z": "a"}}}, ["x", "y", "z"]))

##Invalid Key Test
print(get_value({"a": {"b": {"c": "d"}}}, ["a", "b", "d"]))
print(get_value({"x": {"y": {"z": "a"}}}, ["x", "d", "z"]))