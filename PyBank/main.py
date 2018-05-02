#import necessary libraries
#no os import due to same-dir files being used
import csv
import datetime

#variable declarations
import_more_spreadsheets = "N"
csv_to_import = ""
output_file_name = ""
list_of_datetimes = []
list_of_dates = []

list_of_revenues = []
date_revenue_tuples = ()
most_revenue_amount = ""
most_revenue_month = ""
least_revenue_amount = ""
least_revenue_month = ""

def import_csv_analyze():
    revenue_total = 0
    #Print beginning splash and prompt for filepath(name for local files)
    print("Welcome to the Pythonic Budget File Interpreter Mk1!")
    csv_to_import = input("Please specify the filepath for your csv(include __.csv!): ")
    with open(csv_to_import, 'r', newline='') as csvfile:
        csvreader_output = csv.reader(csvfile, delimiter=",")
        #extract rows out of csv object and convert to datetime class objects
        dates_revenue = list(csvreader_output)
        #use pop to remove the header row
        dates_revenue.pop(0)
        print(dates_revenue)
        #loop over the list so the dates can be converted to datetime class objects
        for i in range(len(dates_revenue)):
            temp_ = dates_revenue[i]
            #convert to datetime class object
            #Use if and len of the date to determine long or short-hand of the year
            # also send a nasty note to Susan in Finance about her imprecision
            if len(temp_[0]) == 6:
                date_ = datetime.datetime.strptime(temp_[0],"%b-%y")
            elif len(temp_[0]) == 8:
                date_ = datetime.datetime.strptime(temp_[0],"%b-%Y")
            else:
                print("This isn't working.")
            #create a list of datetime objects
            list_of_datetimes.append(date_)
            list_of_revenues.append(temp_[1])
            revenue_total = revenue_total + int(temp_[1])
        #Create timedelta object by subtracting the final date from the first
        date_range = list_of_datetimes[-1] - list_of_datetimes[0]
        #Divide timedelta.days by 30 to determine the date_range in months
        date_range = date_range.days / 30
        for i in range(len(list_of_datetimes)):
            list_of_dates.append(datetime.datetime.strftime(list_of_datetimes[i],"%b-%y"))
        date_revenue_tuples = (zip(list_of_dates,list_of_revenues))
        #Sort the list of date-revenue tuples by revenue
        date_revenue_tuples = sorted(date_revenue_tuples, key=lambda x: int(x[1]))
        #God there is probably a better way to do this...#janky
        #This loop will allow the loop to go to completion since the last tuple
        # will correspond to the least revenue & month it occurred in
        for _ in date_revenue_tuples:
            most_revenue_amount = _[1]
            most_revenue_month = _[0]
        #This loop will stop after the first assignment since the first tuple
        # will correspond to the least revenue & month it occurred in
        for _ in date_revenue_tuples:
            least_revenue_amount = _[1]
            least_revenue_month = _[0]
            break    
        #Output the Financial Analysis in the terminal
        print("Pythonic Budget Interpreter Financial Analysis\n=======================================")
        print("The number of months in the budget: "+str(round(date_range)))
        print("Total Revenues: $"+str(round(revenue_total)))
        print("Average Revenue Change: $"+(str(round(revenue_total/round(date_range)))))
        print("The most revenue received was: $"+str(most_revenue_amount)+"\nIt was received in this month-year: "+str(most_revenue_month))
        print("The least revenue (-loss) received was: $"+str(least_revenue_amount)+"\nIt was received in this month-year: "+str(least_revenue_month))
    with open(csv_to_import+'_output.txt','w') as output_file:
        output_file.write("Pythonic Budget Interpreter Financial Analysis\n=======================================\n")
        output_file.write("The number of months in the budget: "+str(round(date_range)))
        output_file.write("\nTotal Revenues: $"+str(round(revenue_total)))
        output_file.write("\nAverage Revenue Change: $"+(str(round(revenue_total/round(date_range)))))
        output_file.write("\nThe most revenue received was: $"+str(most_revenue_amount)+"\nIt was received in this month-year: "+str(most_revenue_month))
        output_file.write("\nThe least revenue (-loss) received was: $"+str(least_revenue_amount)+"\nIt was received in this month-year: "+str(least_revenue_month))
        
    global import_more_spreadsheets
    import_more_spreadsheets = input("Would you like to import another spreadsheet? Y/N: ")
    print("Thanks for using the Pythonic Budget File Interpreter!")
    return

while (import_more_spreadsheets == "Y"):
    import_csv_analyze()

if __name__ == "__main__":
    import_csv_analyze()