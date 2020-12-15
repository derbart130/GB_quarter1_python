num = int(input("Enter amount of goods: "))
features = {'title': '', 'price': '', 'quantity': '', 'unit': ''}
analytics = {'title': [], 'price': [], 'quantity': [], 'unit': []}
goods = []
i = 1
print(f"Product №1")
while i <= num:
    for key in features.keys():
        feature = input(f"Enter value of product feature: {key} = ")
        features[key] = int(feature) if key == 'price' or key == 'quantity' else feature
        analytics[key].append((features[key]))
    goods.append((i, features))
    i += 1
    if i <= num:
        print(f"Product №{i}")
    else:
        break
print(f"\nList of goods:\n{goods}")
print(f"\nCurrent analytics:\n{'*' * 100}")
for key, value in analytics.items():
    print(f"{key[:25]:>30}, {value}")