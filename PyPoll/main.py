import csv
number_of_candidates = 0

def import_analyze_output():
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
    for voter in list_of_votes:
        if voter[2] in dict_of_candidates:
            dict_of_candidates[voter[2]] += 1
        else:
            dict_of_candidates.update({voter[2]: 1})
    for i in dict_of_candidates:
        total_votes = total_votes + dict_of_candidates.get(i)
    print(f"Election Results\n====================\nTotal Votes: {total_votes}\n====================\n")
    for i in dict_of_candidates:
        list_of_percents.append(round((dict_of_candidates[i]/total_votes)*100,1))
    _ = 0
    for i in dict_of_candidates:
        print(f"{i}: {list_of_percents[_]}% ({dict_of_candidates[i]})")
        _ = _+1
    print("====================\nThe winner is: "+str(max(dict_of_candidates, key=dict_of_candidates.get))+"\n====================")
    print("Now outputting results to election_results.txt")
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