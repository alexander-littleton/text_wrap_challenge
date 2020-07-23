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
            output_list.pop().append(replacement_line)

    print("\n".join(output_list))

user_input = ''

while user_input != 'exit':
    user_input = input('Submit text for word wrapping or enter "exit" to quit: ')
    if user_input != 'exit': text_wrap(user_input) 