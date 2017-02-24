import csv

def parse(filename,keep_header=False):
    """
    Parses csv files.
    A wrapper around csv.reader that deals with idiosyncracies
    of csv files from phenome.jax.org.
    Specifically, it discards comments at the top of files and
    removes extra columns in header row (that probably result
    from converting an .xls file to a .csv)
    Typically this occurs only for phenome files from individual investigators,
    i.e., a file with a last name in the title like 'Willot1.csv'
    Other files from the site will still load correctly using this function,
    however.
    
    arguments
    ---------
    filename : string, name of csv file
    keep_header : if True, returns header. default is False.
    
    returns
    -------
    csv_file_parsed : list of lists, csv file after
                      parsing by csv.reader
    header : list of strings, header row,
             only returned if keep_header = True
    """
    
    with open(filename,'r') as csv_file_open:
        csv_file = csv_file_open.readlines()
        
    counter = 0
    while 1:
        line = csv_file[counter]
        if '//' not in line:
            break 
        counter += 1
    reader = csv.reader(csv_file[counter+1:],delimiter=',')
    parsed_file = list(reader)
    if keep_header:
        header = parsed_file[0]
        header = [col_name
                     for col_name in header
                         if col_name !='']
        return parsed_file[1:], header
    else:
        return parsed_file[1:]
