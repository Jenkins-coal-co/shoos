from pprint import pprint


def main():
    with open('sneakers.csv', 'r', encoding='utf-8') as file:
        shoos = []
        for line in file.readlines()[1:-1]:
            linedict = {
                "title": line.split(',')[0],
                "color": line.split(',')[1],
                "current_price": float(line.split(',')[2]),
                "full_price": float(line.split(',')[3]),
                "publish_date": line.split(',')[4].strip()
            }
            shoos.append(linedict)
        fun_part(shoos)


def fun_part(shoos):
    print("Choos, how i should sort the shoos!")
    print("0-title")
    print("1-color")
    print("2-current_price")
    print("3-full_price")
    print("4-publish_date")
    criteria = int(input("-"))
    print(type(list(shoos[0].keys())))
    print(list(shoos[0].keys()))
    pprint(sorted(shoos, key=lambda shoo: shoo[list(shoo.keys())[criteria]]), sort_dicts=False)


main()
