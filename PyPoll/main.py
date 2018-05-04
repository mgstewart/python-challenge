import csv
number_of_candidates = 0

def import_analyze_output():
    '''import_analyze_output is a function that requires no parameters.
        it serves to allow the user to designate a CSV input file that
        must be local to the python script directory. It will parse the CSV
        and create statistics about votes by candidate and output the result
        including winner to both a terminal and a text file.'''
    list_of_votes =[]
    dict_of_candidates = {}
    list_of_percents = []
    total_votes = 0
    print("Welcome to the Python Parnership's Pythonic Polling Parsing Program!")
    #Allow user to designate filename, note directory is constrained to directory of script
    csv_file_name = input("Please type in the filename of the csv containing the polling data\nPlease include .csv in the name: ")
    with open(csv_file_name,'r',newline='') as csvfile:
        csv_obj = csv.reader(csvfile,delimiter=",")
        for _ in csv_obj:
            #Iterate over csv_obj and cast data into a list
            list_of_votes.append(_)
    #Remove the header row from the data
    list_of_votes.pop(0)
    print("Please wait while the polling data is analyzed, this may take some time...")
    #Loop over the list of lists containing CSV rows
    for voter in list_of_votes:
        #If the second value has been seen before in the dictionary
        #it will simply increment the value of the candidate key once
        if voter[2] in dict_of_candidates:
            dict_of_candidates[voter[2]] += 1
        #If the second value has not been seen, the value will be set
        #to a key in a dictionary with a starting value of 1
        else:
            dict_of_candidates.update({voter[2]: 1})
        #Sum the total votes by recursively incrementing by each dictionary key(i)'s value
    for i in dict_of_candidates:
        total_votes += dict_of_candidates.get(i)
        #Output results in the terminal
    print(f"Election Results\n====================\nTotal Votes: {total_votes}\n====================\n")
    #Loop over the dictionary's keys, dividing each key's value by the total_votes variable
    #then format as a rounded percentage and append into a list of percents
        #perhaps using a list as the dictionary key's value would've been simpler?
    for i in dict_of_candidates:
        list_of_percents.append(round((dict_of_candidates[i]/total_votes)*100,1))
        #Having to set _ value here is messy, but I couldn't think of a work around
        #perhaps if the functions of this script were more modular the local variable
        #reset would work better?
    _ = 0
    for i in dict_of_candidates:
        #Not a very scalable or optimal approach, but it works
        print(f"{i}: {list_of_percents[_]}% ({dict_of_candidates[i]})")
        _ = _+1
    #Use the get object on the dict to search the dict by keys and extract the max value, converted to string for print
    print("====================\nThe winner is: "+str(max(dict_of_candidates, key=dict_of_candidates.get))+"\n====================")
    print("Now outputting results to election_results.txt")
    #repeat above but output to txt file, no encoding designated but this is rural America so it's fine
    with open('election_results.txt','w') as txtfile:
        txtfile.write(f"Election Results\n====================\nTotal Votes: {total_votes}\n====================\n")
        _ = 0
        for i in dict_of_candidates:
            txtfile.write(f"{i}: {list_of_percents[_]}% ({dict_of_candidates[i]})\n")
            _ = _+1
        txtfile.write("====================\nThe winner is: "+str(max(dict_of_candidates, key=dict_of_candidates.get))+"\n====================")
    print("Thank you for using PP's Pythonic Polling Parsing Program!")

if __name__ == "__main__":
    import_analyze_output()