class person:
    def __init__(self,name , age , gender ):
        self.name=name
        self.age=age
        self.gender=gender
        print("Introducing my name, age and gender")

p = person("jacob",25,"Male")
print('My name is', p.name ,', I am ' , p.age, 'and my gender', p.gender)

        

