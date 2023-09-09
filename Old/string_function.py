Str = "     ocean academy       "
print(Str.split())
# .split()
# .strip() - empty space starting and ending
print(Str.strip())
print(Str.rstrip())
print(Str.lstrip())
print(Str.lstrip("    "))
# .find-used to find index
print(Str.find("academy",5,10))
#  -1 not found
print(len(Str))
string = "1234"
print(Str.isdigit())
print(string.isdigit())
# print(Str.isalnum())
# print(string.isalnum())
# print(Str.isspace())
# print(string.isspace())
print(Str.capitalize())
print(Str.upper())
print(Str.isprintable())