import dbdatacompare

if __name__=="__main__":
    src_data_format=input("Enter the Source data format(Excel/DB table)\n")
    if src_data_format.upper() != 'EXCEL' and src_data_format.upper() != 'DB TABLE':
        print('Invalid Input',src_data_format.upper())
        exit()
    tgt_data_format=input("Enter the Target data format(Excel/DB table)\n")
    if tgt_data_format.upper() != 'EXCEL' and tgt_data_format.upper() != 'DB TABLE':
        print('Invalid Input')
        exit()

    if src_data_format.upper()=='DB TABLE' and tgt_data_format.upper()=='DB TABLE':
        print('Execution Started')
        dbdatacompare.dbcompare(dbdatacompare.excel_file)