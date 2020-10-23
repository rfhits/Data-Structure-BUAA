political_divisions =[{"name": "Alabama", "abbreviation": "AL",
                          "counties": ["Dale", "Autauga", "Baldwin", "Bibb", "Bullock", "Chilton", "Coffee", "Coosa",
                                       "Etowah", "Franklin", "Lamar", "Macon", "Marion", "Morgan", "Randolph", "Sumter",
                                       "Wilcox", "Barbour", "Blount", "Butler", "Calhoun", "Chambers", "Cherokee",
                                       "Choctaw", "Clarke", "Clay", "Cleburne", "Colbert", "Conecuh", "Covington",
                                       "Crenshaw", "Cullman", "Dallas", "DeKalb", "Elmore", "Escambia", "Fayette",
                                       "Geneva", "Greene", "Hale", "Henry", "Houston", "Jefferson", "Lauderdale",
                                       "Lawrence", "Lee", "Lowndes", "Madison", "Marengo", "Marshall", "Mobile",
                                       "Monroe", "Montgomery", "Jackson", "Perry", "Pickens", "Pike", "Russell",
                                       "St. Clair", "Shelby", "Talladega", "Tallapoosa", "Tuscaloosa", "Walker",
                                       "Washington", "Winston", "Limestone"]},
                         {"name": "Alaska", "abbreviation": "AK",
                          "counties": ["Valdez-Cordova",
                                       "Wade Hampton", "Wrangell",
                                       "Yukon-Koyukuk",
                                       "Ketchikan Gateway",
                                       "Aleutians East", "Bethel",
                                       "Hoonah-Angoon", "Sitka",
                                       "Kenai Peninsula",
                                       "Kodiak Island",
                                       "Lake and Peninsula",
                                       "Nome", "Petersburg",
                                       "North Slope",
                                       "Northwest Arctic",
                                       "Southeast Fairbanks",
                                       "Yakutat",
                                       "Aleutians West",
                                       "Anchorage", "Bristol Bay",
                                       "Denali", "Dillingham",
                                       "Fairbanks North Star",
                                       "Haines", "Juneau",
                                       "Matanuska-Susitna",
                                       "Prince of Wales-Hyder",
                                       "Skagway"]},
                         {"name": "Arizona", "abbreviation": "AZ",
                          "counties": ["Mohave", "Santa Cruz", "Cochise", "Graham", "La Paz", "Pima", "Pinal",
                                       "Yavapai", "Yuma", "Apache", "Coconino", "Gila", "Greenlee", "Maricopa",
                                       "Navajo"]},
                         {"name": "Arkansas", "abbreviation": "AR",
                          "counties": ["Cleveland", "Columbia", "Baxter", "Cleburne", "Cross",
                                       "Drew", "Garland", "Hot Spring", "Jackson",
                                       "Little River", "Madison", "Montgomery", "Pike",
                                       "Poinsett", "St. Francis", "Searcy", "Sharp", "Union",
                                       "Van Buren", "Washington", "Woodruff", "Arkansas",
                                       "Ashley", "Benton", "Boone", "Bradley", "Calhoun",
                                       "Carroll", "Chicot", "Clark", "Clay", "Conway",
                                       "Craighead", "Crawford", "Crittenden", "Newton",
                                       "Ouachita", "Perry", "Phillips", "Polk", "Pope",
                                       "Prairie", "Pulaski", "Randolph", "Saline", "Scott",
                                       "Sebastian", "Sevier", "Stone", "Dallas", "Desha",
                                       "Faulkner", "Franklin", "Fulton", "Grant", "Greene",
                                       "Hempstead", "Howard", "Independence", "Izard",
                                       "Jefferson", "Johnson", "Lafayette", "Lawrence", "Lee",
                                       "Logan", "Lonoke", "Marion", "Miller", "Mississippi",
                                       "Monroe", "Nevada", "White", "Yell", "Lincoln"]},
                         {"name": "California", "abbreviation": "CA",
                          "counties": ["Colusa", "Glenn", "Kings", "Mariposa", "Modoc", "Sacramento", "San Bernardino",
                                       "Santa Barbara", "Shasta", "Tulare", "Alameda", "Alpine", "Marin", "Mendocino",
                                       "Merced", "Mono", "Monterey", "Napa", "Nevada", "Orange", "Placer", "Plumas",
                                       "Riverside", "San Benito", "San Diego", "San Francisco", "San Joaquin", "Amador",
                                       "Butte", "Calaveras", "Contra Costa", "Del Norte", "El Dorado", "Fresno",
                                       "Humboldt", "Imperial", "Inyo", "Kern", "Lake", "Lassen", "Los Angeles",
                                       "Madera", "San Luis Obispo", "San Mateo", "Santa Clara", "Santa Cruz", "Sierra",
                                       "Siskiyou", "Solano", "Sonoma", "Stanislaus", "Tehama", "Trinity", "Tuolumne",
                                       "Ventura", "Yolo", "Yuba", "Sutter"]},
                         {"name": "Colorado", "abbreviation": "CO",
                          "counties": ["Hinsdale", "Kiowa", "Lincoln", "Mineral", "Montrose", "Phillips", "Pueblo",
                                       "Rio Grande", "Sedgwick", "Washington", "Adams", "Alamosa", "Bent", "Boulder",
                                       "Broomfield", "Crowley", "Elbert", "Gilpin", "Gunnison", "Huerfano", "Jackson",
                                       "Jefferson", "Kit Carson", "Lake", "La Plata", "Larimer", "Las Animas", "Logan",
                                       "Mesa", "Moffat", "Montezuma", "Morgan", "Otero", "Ouray", "Park", "Pitkin",
                                       "Prowers", "Rio Blanco", "Routt", "Saguache", "San Juan", "San Miguel", "Summit",
                                       "Teller", "Weld", "Yuma", "Cheyenne", "Arapahoe", "Archuleta", "Baca", "Chaffee",
                                       "Clear Creek", "Conejos", "Costilla", "Custer", "Delta", "Denver", "Dolores",
                                       "Eagle", "El Paso", "Fremont", "Garfield", "Grand", "Douglas"]},
                         {"name": "Connecticut", "abbreviation": "CT",
                          "counties": ["Tolland", "Windham", "Fairfield", "Hartford", "Litchfield", "Middlesex",
                                       "New Haven", "New London"]}]


# 本题会提供一个political_divisions.py文件，其中定义了political_divisions列表，包含了美国七个州的部分行政区信息。
# political_divisions列表包含若干字典，每个字典表示一个州。
# 每个州份分别包含三个字典项：
# name项对应的值为一个字符串，表示州的名称；
# abbreviation项对应的值为一个字符串，表示州的缩写；
# counties项对应的值为一个列表，表示州所含的部分郡级行政单位名称。

# 现在要求你编写一个程序，可以对political_divisions.py程序中的political_division列表之内的信息进行两种查询操作：

# 操作1：给定一个州的名称或缩写，并给出一个字母，输出字典内包含的所有首字母为该字母的郡（counties）的信息；
# 如: 1 AK B表示搜索所有阿拉斯加州以B开头的郡级行政单位名称；

# 操作2：给出一个郡名称，输出字典内所有包含同名郡的州的缩写；
# 如： 2 Washington表示搜索所有包含名为Washington的郡级行政单位的州份缩写。

# 请你对用户的n个查询操作，分别完成查询操作。
# 备注：请将political_divisions.py程序内容粘贴到你编写的程序前，注意列表中州名、缩写和郡名称各自的特点

# 【输入形式】输入数据共n+1行：
# 第一行为一个整数n，表示所有查询的总次数；
# 接下来的n行，每行包含一个查询:
# 对于第一种查询，数字1后有一个空格，其后为表示州名称或缩写的字符串，由大小写字母组成，其后再跟一个空格，为查询的首字母，大小写均有可能；
# 对于第二种查询，数字2后有一个空格，其后为表示郡级行政单位名称的字符串，由大小写字母和空格组成。

# 【输出形式】输出包含n行，每行包含数个以英文逗号+空格隔开的字符串，包含每次查询的所有结果，结果以字典序（字符顺序从小到大）排列；最后一个结果后没有逗号。

# 【样例输入】
# 2
# 1 AK B
# 2 Washington

# 【样例输出】
# Bethel, Bristol Bay
# AL, AR, CO

n= int(input())
out = []
for i in range(n):
    istru=input().split()       # instruction 指令
    if istru[0] == '1':
        ans=[]
        for state in political_divisions:
            if (state["name"]== istru[1]) or (state["abbreviation"] == istru[1]):
                for county in state["counties"]:
                    if county[0] == istru[2].capitalize():  # 首字母判断
                        ans.append(county)
        ans.sort()
        out.append((', ').join(ans))
    else:
        ans=[]
        county_name = (' ').join(istru[1:])     # 州下的郡，名字里可能有空格，注意这个空格是半角。
        for state in political_divisions:
            if county_name in state["counties"]:
                ans.append(state["abbreviation"])
        ans.sort()
        out.append((', ').join(ans))
for i in out:
    print(i)
