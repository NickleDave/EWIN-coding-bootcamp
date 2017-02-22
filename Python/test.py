def skip_comments_and_comma_row(csv_file,keep_header=False):
    with open(csv_file,'r') as dummy_filename:
       csv_file = dummy_filename.readlines()
    counter = 0
    while 1:
        line = csv_file[counter]
        if '//' not in line:
            break 
        counter += 1
    if keep_header:
        header = csv_file[counter+1] 
        return csv_file[counter+2:],header
    else:
        return csv_file[counter+2:]