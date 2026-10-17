# *args: any number of positional arguments

def show_args(*args):
    print(args)

show_args(1, 3, 5)
show_args("ali", 3.3, True)

# args is just a tuple holding everything you passed in. A practical use:
# The name args isn’t special. The * is what matters, so *numbers works the same way
def total( *numbers ):
    return sum(numbers)

print(total(1, 3, 5))
print(total(2, 4))

# **kwargs: any number of keyword arguments
def show_kwargs(**kwargs):
    print(kwargs)

show_kwargs(name="Khan", city="Peshawar")
show_kwargs(country="Pakistan")

# kwargs is a dictionary of key=value pairs. A practical use:

def profile( **info ):
    for key, value in info.items():
        print(f"{key}: {value}")

profile(username="abidroid", email="abid93@gmail.com", website="intellilogics.dev")
