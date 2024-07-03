def my_var():
    list_of_vars = [ 42,
                    "42",
                    "quarante-deux",
                    42.0,
                    True,
                    [42],
                    {42: 42},
                    (42,),
                    set()]
    
    for item in list_of_vars:
        print(f"{item} has a type {type(item)}")


if __name__ == '__main__':
    try:
        my_var()
    except Exception as e:
        print("Error: ", e)
