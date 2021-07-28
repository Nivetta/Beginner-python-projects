PLACEHOLDER = "[name]"
with open("namelist.txt") as names:
    name_list = names.readlines()
    
with open("letter.txt") as letter:
    full_letter = letter.read()
    for name in name_list:
        stripped_name = name.strip()
        completed_letter = full_letter.replace(PLACEHOLDER,stripped_name)
        print(completed_letter)
        with open(f"letter_for_{stripped_name}.txt",mode = "w") as final_list:
            final_list.write(completed_letter)

