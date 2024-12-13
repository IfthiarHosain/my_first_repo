def shipping_lebels(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    if "apt" in kwargs:
       print(f"{kwargs.get('street')},{kwargs.get('apt')}")
    elif "pobox" in kwargs:
       print(f"{kwargs.get('street')}")
       print(f"{kwargs.get('pobox')}")

    else:
      print (f"{kwargs.get('street')}")
    print(F"{kwargs.get('city')},{kwargs.get('area')},{kwargs.get('zip')}")
shipping_lebels("Dr","Badal","fuli","mousumy","the 4th",
                street="2nd street",
                pobox="3001",
                city="Dhaka",
                area="Dholaiper",
                zip="1236")