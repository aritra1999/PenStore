def slug_generator(name, brand):
    return str(brand.lower().replace(" ", "_") + '_' + name.lower().replace(" ", "_"))