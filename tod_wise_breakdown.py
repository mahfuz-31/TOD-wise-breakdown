import pandas as pd  # type: ignore

plan_month = input("Enter Plan Month: ")
plan_next_month = input("Enter Plan Next Month: ")
plan_end = input("Enter Plan Month End: ")
plan_next_end = input("Enter Plan Next Month End: ")
date_ranges = []
before_plan_month = 'Before ' + plan_month
date_ranges.append(before_plan_month)

dates = ['1-7', '8-15', '16-23']
dates.append('24-' + str(plan_end))
for i in dates:
    date_ranges.append(i + '/' + plan_month)

dates = ['1-5', '6-10', '11-20']
dates.append('21-' + str(plan_next_end))
for i in dates:
    date_ranges.append(i + '/' + plan_next_month)
date_ranges.append('On-ward')
print(date_ranges)

factories = [
    'JAL',
    'JFL',
    'JKL',
    'MFL',
    'FFL2',
    'JKL2'
]
unit = pd.DataFrame()
unit['Factory'] = factories
for i in range(1, 11):
    file = 'D:/1. Work/3. Half Monthly/TOD wise breakdown/Unit/' + str(i) + '.csv'
    df = pd.read_csv(file)
    unit[date_ranges[i - 1]] = None
    for index, row in df.iterrows():
        factory = row['Pl. Board']
        for index1, row1 in unit.iterrows():
            if factory == row1['Factory']:
                unit.loc[index1, date_ranges[i - 1]] = row[str(plan_end) + '-' + plan_month + "-25"]

buyer = pd.DataFrame()
buyer['Buyers'] = [
    'ASDA STORE LTD.',
    'BESTSELLER A/S',
    'KMART AUSTRALIA LIMITED',
    'VF CORPORATION',
    'ZLABELS GMBH',
    'OCHNIK',
    'C & A BUYING GMBH & CO. KG',
    'H & M HENNES & MAURITAZ GBC AB',
    'VOGUE SOURCING LIMITED',
    'INDISKA',
    'ITX KIDS',
    'BONITA GMBS & CO. KG',
    'ESPRIT MACAO COMMERCIAL OFFSHORE LTD.',
    'G-STAR RAW CV',
    'GUESS EUROPE SAGL',
    'HUGO BOSS AG',
    'MQ MARQET AB',
    'NEW FRONTIER',
    'NEXT SOURCING LTD.',
    'PUMA',
    'Ralph Lauren Corporation',
    'TOM TAILOR SOURCING LTD.',
    'CAMEL ACTIVE / BHB-Fashion Service Gmbh',
    'ITX LADIES',
    'BIOWORLD International Ltd'
]

for i in range(1, 11):
    file = 'D:/1. Work/3. Half Monthly/TOD wise breakdown/Buyer/' + str(i) + '.csv'
    df = pd.read_csv(file)
    buyer[date_ranges[i - 1]] = None
    for index, row in df.iterrows():
        b = row['Buyer']
        for index1, row1 in buyer.iterrows():
            if b == row1['Buyers']:
                buyer.loc[index1, date_ranges[i - 1]] = row[str(plan_end) + '-' + plan_month + "-25"]
with pd.ExcelWriter('D:/1. Work/3. Half Monthly/TOD wise breakdown/output.xlsx') as writer:
    unit.to_excel(writer, sheet_name='Unit-Wise', index=False)
    buyer.to_excel(writer, sheet_name='Buyer-Wise', index=False)
