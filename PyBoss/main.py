#import necessary modules
import csv
import datetime as dt
#use the dictionary for state abbreviations from Special Hint (thank you!)
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

def import_reformat_export():
    '''This function requires no parameters imports a (local to script) CSV containing employee data and
    reformats it into an appropriate format then exports it to a new CSV'''
    print("Welcome to the Employee Reformatron 9000!")
    csvname = input("Please enter the name of the CSV file you would like to reformat:  ")
    #Import the employee data file and convert to ordered dict
    with open(csvname,'r',newline='') as csvfile:
        new_list = []
        dictreader = csv.DictReader(csvfile)
        #loop over each row in the csv dictreader
        for row in dictreader:
            #split first and last names into two strings
            first_name, last_name = row['Name'].split(" ")
            #update the dict with two new key:value pairs for each name variable
            row.update([('First Name',first_name)])
            row.update([('Last Name',last_name)])
            #remove the name doublet
            row.pop('Name')
            #extract the DoB to datetime for reformatting
            row_dt = dt.datetime.strptime(row['DOB'],"%Y-%m-%d")
            formatted_date = row_dt.strftime("%m/%d/%Y")
            #add formatted date string back into dictionary
            row.update([('DoB',formatted_date)])
            #remove DOB doublet
            row.pop('DOB')
            #slice into strings to extract the first six characters (5 digits and hyphen)
            first_six_characters = row['SSN'][:6]
            #because the row['SSN'] is immutable, assign the string replace value to a new string variable
            new_SSN = row['SSN'].replace(first_six_characters,'***-**')
            #update the ordered dictionary with the new_SSN string
            row.update([('SSN', new_SSN)])
            #assign abbrev_state the value returned by searching the state/abbrev dict with row['State'] as the key
            abbrev_state = us_state_abbrev[row['State']]
            #update the row with the new abbrev_state value
            row.update([('State',abbrev_state)])
            #add each row into a list that can be read outside this IO event
            new_list.append(row)
        #output the reformatted ordereddict to acsv output file for HR
        with open(csvname.replace('.csv','')+'_output.csv','w') as csvfile:
            fieldnames = ['Emp ID','First Name','Last Name','DoB','SSN','State']
            writer = csv.DictWriter(csvfile, fieldnames)
            writer.writeheader()
            for i in new_list:
                writer.writerow(i)
if __name__ == "__main__":
    import_reformat_export()