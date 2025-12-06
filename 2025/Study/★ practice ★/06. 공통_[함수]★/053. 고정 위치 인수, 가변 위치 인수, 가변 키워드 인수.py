def custom_print( a, *args, **kwargs):
    print(a)
    print(*args)
    print(**kwargs)

custom_print( '워언본' , 1, 2 , 3, sep = ' ', end = ' ')