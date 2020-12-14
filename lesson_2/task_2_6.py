num = int(input("Enter amount of goods: "))
n = 1
features = []
goods = []
analytics = {}
while n <= num:
    print("Enter product features:")
    features = dict({'title': input("- enter product title: "),
                  'price': input("- enter product price: "),
                  'quantity': input('- enter amount of product: '),
                  'unit': input("- enter unit: ")})
    goods.append((n, features))
    analytics = dict({'title': features.get('title'),
                      'price': features.get('price'),
                      'quantity': features.get('quantity'),
                      'unit': features.get('unit')})
    n += 1
print(goods)
print(analytics)
print(features)