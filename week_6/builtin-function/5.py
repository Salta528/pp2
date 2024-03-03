def all_true(elements):
    return all(elements)
def f(ell):
    result = all_true(ell)
    return result
tuple_elements = ("abc", 45, "male", 0)
res = f(tuple_elements)
print(res)