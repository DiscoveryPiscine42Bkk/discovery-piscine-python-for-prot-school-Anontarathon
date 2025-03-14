def array_of_names(p):
    full = []
    for f_name, l_name in p.items():
        #
        f_name = f"{f_name.capitalize()} {l_name.capitalize()}"
        full.append(f_name)
        return full
p = {
    "jean": "valjean", "grace": "hopper", "xavier": "niel" ,"fifi": "brindacier",
}
print(array_of_names(p))