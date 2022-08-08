#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# Zebo Zhu, 07Aug2022, Modified File
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
dicRow1 = {'ID': 1, 'CD': 'Dancing Queen', 'Artist Name': 'ABBA'}
dicRow2 = {'ID': 2, 'CD': 'All By Myself', 'Artist Name': 'Eric Carmen'}
dicRow3 = {'ID': 3, 'CD': 'It\'s Too late', 'Artist Name': 'Carole King'}
dicRow4 = {'ID': 4, 'CD': 'Ain\'t No Sunshine', 'Artist Name': 'Billy Withers'}
dicRow5 = {'ID': 5, 'CD': 'Piano Man', 'Artist Name': 'Billy Joel'}
lstTbl = []  # list of lists to hold data
#replace list of lists with list of dicts
lstRow = []  # list of data row
dicRow = {}
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
lstTbl.append(dicRow1)
lstTbl.append(dicRow2)
lstTbl.append(dicRow3)
lstTbl.append(dicRow4)
lstTbl.append(dicRow5)

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print()
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # Add the functionality of loading existing data
        objFile = open(strFileName,'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'ID': lstRow[0], 'CD': lstRow[1], 'Artist Name': lstRow[2]}
            #lstTbl.append(dicRow)
        objFile.close()
        #show the result
        print('item in the data now: ')
        for row in lstTbl:
            print(row)
        pass
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'ID': intID, 'CD': strTitle, 'Artist Name': strArtist}
        lstTbl.append(dicRow)
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')
    elif strChoice == 'd':
        # Add functionality of deleting an entry
        strID = input('Please enter the ID of the entry you want to delete: ')
        intID = int(strID)
        del lstTbl[intID - 1]
        print('item in the data now: ')
        for row in lstTbl:
            print(row)
        pass
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

