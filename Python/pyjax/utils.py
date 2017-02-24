import numpy as np

def sort_by_strain(parsed_file,key_index,value_index):
    """
    takes csv file of individual animal data
    and sorts into a dictionary where the key is
    strain of mouse and the value for each key is
    a list. The list contains all the measurements
    from individual animals of that strain.
    
    arguments
    ---------
    key_index : index of column in each row that should be
                used for keys. should have repeated values.
    value_index : index of column in each row that is the 
                  value to associate with the keys.
                  
    returns
    -------
    mouse_dict: dictionary where keys are strains of mice and
                values are lists, all entries in column of
                interest that correspond to a given strain
    """
    
    sorted_by_strain = {} # make empty dictionary
    for row in parsed_file:
        row_key = row[key_index] 
        row_val = float(row[value_index]) # convert from string to float!
        if row_key in mouse_dict.keys():
            sorted_by_strain[row_key].append(row_val)
        else:
            sorted_by_strain[row_key] = [row_val]
    return sorted_by_strain

def compute_mouse_dict_mean_and_std(sorted_by_strain):
    """
    computes means and standard deviations for dictionary produced by
    sort_by_strains function, where the key is a mouse strain and the 
    value is a list of measurements of some variable, e.g. Auditory Startle
    Response at 100 decibels 

    arguments
    ---------
    sorted_by_strain : dictionary returned by sort_by_strain function.
                       keys should be names of mouse strains, and values
                       should be lists of measurements

    returns
    -------
    mouse_means : dictionary where key is strain name and value is mean
    mouse_stddevs : dictionary where key is strain name and value is standard
                    deviation
    """
    
    mouse_means = {}
    mouse_stdevs = {}
    
    for key,val in sorted_by_strain.items():
        mouse_means[key] = np.mean(val)
        mouse_stddevs[key] = np.std(val)
    return mouse_means, mouse_stddevs
