medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Add your code here
updated_medical_data = medical_data.replace('#', '$')
# print(updated_medical_data)

num_records = 0

for character in updated_medical_data:
    if character == '$':
        num_records += 1

# print("There are " + str(num_records) + " medical records in the data.")

medical_data_split = updated_medical_data.split(';')
# print(medical_data_split)

medical_records = []
for record in medical_data_split:
    medical_records.append(record.split(','))
# print(medical_records)

medical_records_clean = []
for record in medical_records:
    record_clean = []
    for item in record:
        record_clean.append(item.strip())
    medical_records_clean.append(record_clean)

# print(medical_records_clean)


for record in medical_records_clean:
    record[0] = record[0].upper()
    # print(record[0])

names = []
ages = []
bmis = []
insurance_costs = []

for record in medical_records_clean:
    names.append(record[0])
    ages.append(record[1])
    bmis.append(record[2])
    insurance_costs.append(record[3])

# print("Names: " + str(names))
# print("Ages: " + str(ages))
# print("BMIS: " + str(bmis))
# print("Insurance Costs: " + str(insurance_costs))

total_bmi = 0
for bmi in bmis:
    total_bmi += float(bmi)
  
average_bmi = total_bmi/len(bmis)
# print("Average BMI: " + str(average_bmi))

# Extra
# Calculate the average insurance cost in insurance_costs.
print(insurance_costs)

insurance_costs_clean = []
for record in insurance_costs:
  insurance_costs_clean.append(record.replace('$',''))

insurance_integer = 0
for costs in insurance_costs_clean:
  insurance_integer += float(costs)

average_insurance = insurance_integer/len(insurance_costs_clean)
print("The average cost of insurance is $" + str(average_insurance) + ".")

# Write a for loop that outputs a string for each individual:
for i in range(0,len(medical_records_clean)):
    print('{} is {} years old with a BMI of {} and an insurance cost of {}.'.format(names[i], ages[i], bmis[i], insurance_costs[i]))
