import json
import pprint

with open('../food_services.json', encoding='utf-8') as file:
    data_in = json.load(file)
    res_company = {}
    res_district = {}
    for data in data_in:
        res_district[data['District']] = res_district.setdefault(data['District'], 0) + 1
        if data['OperatingCompany']:
            res_company[data['OperatingCompany']] = res_company.setdefault(data['OperatingCompany'], 0) + 1
    res_dis = sorted(res_district.items(), key=lambda x: x[1])[-1]
    res_com = sorted(res_company.items(), key=lambda x: x[1])[-1]
    print(f'{res_dis[0]}: {res_dis[1]}')
    print(f'{res_com[0]}: {res_com[1]}')


