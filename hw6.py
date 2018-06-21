


# used for printing array, must take a second argument. If second
# argument is NONE then array[i] will print otherwise a specified index in array[i]
def print_array_with_index(arr,index = None):
    if index == None:
        for i in range(len(arr)):
            print("Word: " + str(arr[i][0]) + " POS: " + str(arr[i][1]))
    else:
        for i in range(len(arr)):
            print(arr[i][index])

# used for printing dictionary
def print_dictionary(dict):
    for key, value in dict.items():
        print("Key is " + str(key) + " and value is: " + str(value))

# check if word ends with ed
def ends_with_ed(word):
    val =word.endswith(('ed'))
    if(val):
        return 1
    else:
        return 0



# check if word ends with ing
def ends_with_ind(word):
    val =word.endswith(('ing'))
    if(val):
        return 1
    else:
        return 0

# check if word ends with ly
def ends_with_ly(word):
    val =word.endswith(('ly'))
    if(val):
        return 1
    else:
        return 0

# check if word begins with a capital letter
def begins_with_uppercase(word):
    val = word[0].isupper()
    if(val):
        return 1
    else:
        return 0



file = open('WSJ_23.pos', 'r')
array_with_word_pos_and_bioTag = []
for line in file:
    # split each line where [0] will be the word and [1] will be the POS
    line1 = line.split( )
    if(len(line1)== 0):
        line1.append("START" )
        line1.append('START')
        # line1.append('START')###############################################comment out when doing test chunk#################################
    elif(line1[1] == "."):
            line1[1] = "END"
            # line1[2] = "END"###############################################comment out when doing test chunk###################################
    elif(line1[1] == ")"):
            continue
    elif(line1[1] == "("):
            continue
    elif(line1[1] == ","):
            continue
    elif(line1[1] == "``"):
            continue
    elif(line1[1] == "''"):
            continue
    elif(line1[1] == ":"):
            continue
    elif(line1[1] == "$"):
            continue
    elif(line1[1] == "#"):
            continue

    array_with_word_pos_and_bioTag.append(line1)

# print array
# print_array_with_index(array_with_word_pos_and_bioTag)




# make an array with the word after the current word
array_of_next_word_intfo = []
for i in range(len(array_with_word_pos_and_bioTag)):
    if (i >= len(array_with_word_pos_and_bioTag)-1):
        arr = ["END_OF_FILE","END_OF_FILE","END_OF_FILE"]
        array_of_next_word_intfo.append(arr)
        # print arr
    else:
        array_of_next_word_intfo.append(array_with_word_pos_and_bioTag[i+1])
        # print array_with_word_pos_and_bioTag[i+1]


# make an array with the word that is 2 places away from the current word
array_of_word_after_next_word = []
for i in range(len(array_with_word_pos_and_bioTag)):
    if (i >= len(array_with_word_pos_and_bioTag)-2):
        arr = ["END_OF_FILE","END_OF_FILE","END_OF_FILE"]
        array_of_word_after_next_word.append(arr)
        # print arr
    else:
        array_of_word_after_next_word.append(array_with_word_pos_and_bioTag[i+2])
        # print array_with_word_pos_and_bioTag[i+2]


# make an array with the word that is 2 places before from the current word
arrayOFPRevPrevWord = []
for i in range(len(array_with_word_pos_and_bioTag)):
    if (i<2):
        arr = ["BEGINNING_OF_FILE","BEGINNING_OF_FILE","BEGINNING_OF_FILE"]
        arrayOFPRevPrevWord.append(arr)
        # print arr
    else:
        arrayOFPRevPrevWord.append(array_with_word_pos_and_bioTag[i-2])
        # print array_with_word_pos_and_bioTag[i-2]



array_of_previous_word_info = []# this array will have the word as the first element of the tuple, and the previous word's data as the second
for i in range(len(array_with_word_pos_and_bioTag)):

    if(array_with_word_pos_and_bioTag[i] == "START"):
        continue
    else:
        tup =(array_with_word_pos_and_bioTag[i][0], array_with_word_pos_and_bioTag[i][1], array_with_word_pos_and_bioTag[i-1])
        array_of_previous_word_info.append(tup)




# training file INCLUDING BIO tags
# f = open('training.chunk','w')
# # pring everything as a vector with name=value with BIO TAG as the last feature
# for i in range(len(array_with_word_pos_and_bioTag)):
#     output = str(array_of_previous_word_info[i][0]) + "\tcurrent_POS="+str(array_of_previous_word_info[i][1])  + "\tis_uppercase=" + str(begins_with_uppercase(array_of_previous_word_info[i][0])) + "\tends_with_ed=" + str(ends_with_ed(array_of_previous_word_info[i][0])) + "\tends_with_ing=" + str(ends_with_ind(array_of_previous_word_info[i][0])) + "\tends_with_ly=" + str(ends_with_ly(array_of_previous_word_info[i][0]))+ "\tprevious_Word=" + str(array_of_previous_word_info[i][2][0]) + "\tprevious_POS="+  str(array_of_previous_word_info[i][2][1])  + "\tprevious_is_uppercase=" + str(begins_with_uppercase(array_of_previous_word_info[i][2][0])) + "\tprevious_ends_with_ed=" + str(ends_with_ed(array_of_previous_word_info[i][2][0])) + "\tprevious_ends_with_ing=" + str(ends_with_ind(array_of_previous_word_info[i][2][0])) + "\tprevious_ends_with_ly=" + str(ends_with_ly(array_of_previous_word_info[i][2][0]))+"\tnext_word="+ str(array_of_next_word_intfo[i][0]) + "\tnext_word_POS=" + str(array_of_next_word_intfo[i][1]) + "\tnext_is_uppercase=" + str(begins_with_uppercase(array_of_next_word_intfo[i][0])) + "\tnext_ends_with_ed=" + str(ends_with_ed(array_of_next_word_intfo[i][0])) + "\tnext_ends_with_ing=" + str(ends_with_ind(array_of_next_word_intfo[i][0])) + "\tnext_ends_with_ly=" + str(ends_with_ly(array_of_next_word_intfo[i][0]))+ "\tprevious_previous_word=" + str(arrayOFPRevPrevWord[i][0]) + "\tprevious_previous_POS="+  str(arrayOFPRevPrevWord[i][1])+ "\tnext_next_word=" + str(array_of_word_after_next_word[i][0]) + "\tnext_next_POS="+  str(array_of_word_after_next_word[i][1])  + "\tBIO_tag=" + str(array_of_previous_word_info[i][2][2])
#     f.write(output)
# f.close()



# write to test file including NO BIO tags
f = open('WSJ_23Output.pos','w')

#print all features with no BIO tag
for i in range(len(array_with_word_pos_and_bioTag)):
    output = str(array_of_previous_word_info[i][0]) + "\tcurrent_POS="+str(array_of_previous_word_info[i][1])  + "\tis_uppercase=" + str(begins_with_uppercase(array_of_previous_word_info[i][0])) + "\tends_with_ed=" + str(ends_with_ed(array_of_previous_word_info[i][0])) + "\tends_with_ing=" + str(ends_with_ind(array_of_previous_word_info[i][0])) + "\tends_with_ly=" + str(ends_with_ly(array_of_previous_word_info[i][0]))+ "\tprevious_Word=" + str(array_of_previous_word_info[i][2][0]) + "\tprevious_POS="+  str(array_of_previous_word_info[i][2][1])  + "\tprevious_is_uppercase=" + str(begins_with_uppercase(array_of_previous_word_info[i][2][0])) + "\tprevious_ends_with_ed=" + str(ends_with_ed(array_of_previous_word_info[i][2][0])) + "\tprevious_ends_with_ing=" + str(ends_with_ind(array_of_previous_word_info[i][2][0])) + "\tprevious_ends_with_ly=" + str(ends_with_ly(array_of_previous_word_info[i][2][0]))+"\tnext_word="+ str(array_of_next_word_intfo[i][0]) + "\tnext_word_POS=" + str(array_of_next_word_intfo[i][1]) + "\tnext_is_uppercase=" + str(begins_with_uppercase(array_of_next_word_intfo[i][0])) + "\tnext_ends_with_ed=" + str(ends_with_ed(array_of_next_word_intfo[i][0])) + "\tnext_ends_with_ing=" + str(ends_with_ind(array_of_next_word_intfo[i][0])) + "\tnext_ends_with_ly=" + str(ends_with_ly(array_of_next_word_intfo[i][0]))+ "\tprevious_previous_word=" + str(arrayOFPRevPrevWord[i][0]) + "\tprevious_previous_POS="+  str(arrayOFPRevPrevWord[i][1])+ "\tnext_next_word=" + str(array_of_word_after_next_word[i][0]) + "\tnext_next_POS="+  str(array_of_word_after_next_word[i][1])
    f.write(output)
f.close()
