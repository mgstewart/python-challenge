import csv
number_of_candidates = 0

def import_analyze_output():
    list_of_candidates = []
    list_of_votes =[]
    dict_of_candidates = {}
    wastetime = 0
    print("Welcome to Python Corporation's Pythonic Polling Parsing Program!")
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
            if voter[2] in list_of_candidates:
                if voter[2] in dict_of_candidates:
                    dict_of_candidates[voter[2]] += 1
                wastetime += 1
            else:
                list_of_candidates.append(voter[2])
                dict_of_candidates.update({voter[2]: 1})
        print(list_of_candidates)
        print(dict_of_candidates)



if __name__ == "__main__":
    import_analyze_output()