def get_string(*args):

    print(type(args))
    name, age, mood = args

    template = {

        1: f"This is a sample template. My name is {name}. My age is {age}.",

        2: f"This is another sample. I'm feeling {mood}" 
    }

get_string("a", "b", "c")

