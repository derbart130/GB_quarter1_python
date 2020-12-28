import json

with open("test_7j.json", "w", encoding="utf-8") as new_file:
    with open("test_7.txt", encoding="utf-8") as file_obj:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in file_obj}
        av_profit = [profit, {"Average profit": round(sum([int(i) for i in profit.values() if int(i) >0]) /
                                                   len([int(i) for i in profit.values() if int(i) >0]), 2)}]
        json.dump(av_profit, new_file, ensure_ascii=False, indent=5)
