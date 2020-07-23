#Write a program that takes an input string and prints it as multiple lines of text such that no line of text is greater than 13 characters and words are kept whole

def text_wrap(input_string):
    input_list = input_string.split(" ")

    #removes extra spaces and empty values
    input_list = list(filter(lambda x: x!="", input_list))
    input_list = list(filter(lambda x: x!=" ", input_list))

    output_list=[input_list[0]]

    for term in input_list[1:]:
        current_line=output_list[len(output_list)-1]
        if len(current_line+" "+term)>13:
            output_list.append(term)
        else:
            replacement_line = current_line + " " + term
            output_list.pop()
            output_list.append(replacement_line)

    print("\n".join(output_list))

text_wrap("Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived, and so dedicated, can long endure. We are met on a great battle field of that war. We have come to dedicate a portion of it, as a final resting place for those who died here, that the nation might live. This we may, in all propriety do. But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow, this ground")
