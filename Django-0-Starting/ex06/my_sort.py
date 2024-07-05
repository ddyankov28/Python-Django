def sort_dict():
    d = {
        'Hendrix'    : '1942',
        'Allman'     : '1946',
        'King'       : '1925',
        'Clapton'    : '1945',
        'Johnson'    : '1911',
        'Berry'      : '1926',
        'Vaughan'    : '1954',
        'Cooder'     : '1947',
        'Page'       : '1944',
        'Richards'   : '1943',
        'Hammett'    : '1962',
        'Cobain'     : '1967',
        'Garcia'     : '1942',
        'Beck'       : '1944',
        'Santana'    : '1947',
        'Ramone'     : '1948',
        'White'      : '1975',
        'Frusciante' : '1970',
        'Thompson'   : '1949',
        'Burton'     : '1939',
    }
    singers_dict = {}
    for name, year in d.items():
        if year in singers_dict:
            singers_dict[year] += f" {name}"
        else:
            singers_dict[year] = name
    # for y, n in singers_dict.items():
    #     print(f"{y} : {n}")
    sorted_by_year_singers_dict = {}
    for year in sorted(singers_dict):
        sorted_by_year_singers_dict[year] = singers_dict[year]
    #for year, name in sorted_by_year_singers_dict.items():
        #print(f"{year} : {name}")
    for name in sorted_by_year_singers_dict.values():
        list_name = name.split()
        list_name.sort()
        name = ' '.join(list_name)
        print(name)

if __name__ == "__main__":
    try:
        sort_dict()
    except Exception as e:
        print("Error: ", e)

