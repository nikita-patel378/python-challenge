import os
import csv


csv_file_path = os.path.join("Resources", "employee_data1.csv")

#create some lists to store the data
Employee_ID=[]
First_Name=[]
Last_Name=[]
Date_of_Birth=[]
og_Ssn=[]
og_State=[]

# Open and read csv
with open(csv_file_path, newline="",encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)
    # Iterate through each row
    for row in csvreader:
        Employee_ID.append(row[0])
        Split_name=(row[1].split(" "))
        First_Name.append(Split_name[0])
        Last_Name.append(Split_name[1])
        Date_of_Birth.append(row[2])
        og_Ssn.append(row[3])
        og_State.append(row[4])
    #create a new array to store replacement asterisks
    Ssn=[]
    for index in og_Ssn:
        #used slicing to subsitute first five values into the following
        Ssn.append("***-**"+index[6:])
    #use dictionary from online to abbreviate states
    us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}   
    #create a new list to store abbreviations
    State=[]
    for item in og_State:
        State.append(us_state_abbrev.get(item,item))

      #zip the new lists together  
    employeedata = zip(Employee_ID,First_Name,Last_Name, Date_of_Birth,Ssn,State)
    
    exported_file = os.path.join("updated_employee_data.csv")

    #  Open the exported_file
with open(exported_file, "w", newline="", encoding='utf-8') as data_file:
    writer = csv.writer(data_file)

    # Write the header row
    writer.writerow(["Employee_ID", "First Name","Last Name","Date_of_Birth" , "Ssn",
                     "State"])

    # Write in zipped rows
    writer.writerows(employeedata)