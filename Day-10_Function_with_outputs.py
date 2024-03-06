# function with outputs

# return;- tells the program, this is the end of the function
# used to return the output from a function.
# we can also return a function from another function.
# Also, expressions are evaluated and then the result is returned from the function.


# How to convert a string to 'Title case' in python


def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    # title function will give you the title case of a string

    return f"{formatted_f_name} {formatted_l_name}"  # this replaces the calling of function code
    # this output replaces the part of the code where the function was called. Now,


formatted_string = format_name("JoHn", "SMitH")
# save the output w.r.t 'format_name' inside a variable
print(formatted_string)
# or
print(format_name("JoHn", "SMitH"))


# function with multiple return values
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs. "
    # So this way we can catch the cases when something is not quite right and then
    # exit our function instead of wasting time for it to continue working on
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    # title function will give you the title case of a string

    return f"{formatted_f_name} {formatted_l_name}"

print(format_name(input("What is your first name"), input("What is your last name"))

# So this way we can catch the cases when something is not quite right and then
# exit our function instead of wasting time for it to continue working on
