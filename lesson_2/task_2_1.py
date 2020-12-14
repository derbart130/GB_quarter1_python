my_list = [73, None, -33, 'False', True, 36.6, {1, True}, [34, '25'], range(6)]
for i, item in enumerate(my_list, 1):
    print(f"{i}) {item} - {type(item)}")