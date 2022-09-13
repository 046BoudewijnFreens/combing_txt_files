#input_files_folder is de directory van de file waarin de text bestanden moeten worden gecombineerd
def txt_samenvoegen(input_files_folder,output_file):
    import glob
    import pandas as pd
    import os

#Script to combine multiple txt files into one big txt
    print(output_file)
    # Define relative path to folder containing the text files

    files = []

    # Create a dataframe list by using a list comprehension
    files = [pd.read_table(file, delimiter=',', names =['month', 'first', 'second'] ) for file in glob.glob(os.path.join(input_files_folder ,"*.txt"))]

    # Concatenate the list of DataFrames into one
    files_df = pd.concat(files)
    files_df.drop([0], axis=0, inplace=True)
    files_df = files_df.drop(files_df.columns[[1]],axis = 1)


    #Write a the combined tables in one big txt file
    files_df.to_csv(output_file, header=None, index=None)

