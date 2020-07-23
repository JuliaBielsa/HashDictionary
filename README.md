The aim of this script is to crack a hash providing that you have some 
assumptions about the password. It modifies the input words trying to emulate typical human selection of passwords: capitalizing the first letter, adding a number or a date at the end, adding common special characters, replacing letters for a numbers or symbols that look similar, etc.

It creates almost 9000 variants for each word you introduce. You just have to write the hash you want to crack in the file "hash_input.txt" and the list of words in "input.txt". Once you run the script, cross your fingers and it may show you the password corresponding to that hash. It also creates to files, "output.txt" and "hash_output.txt", containing the passwords that were tried and their corresponding hashes.
