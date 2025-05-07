class Persona():
    def __init__(self,name,surname,age,email):
        try:
            if (age > 126) or (age < 0):
                raise ValueError("возраст не православный")
        
            name.lower()
            ascii_range = range(97, 123, 1)
            for item in range(0, len(name)):
                if ord(name[item]) not in ascii_range:
                    raise ValueError("имя не православное")

            surname.lower()
            ascii_range = range(97, 123, 1)
            for item in range(0, len(surname)):
                if ord(surname[item]) not in ascii_range:
                    raise ValueError("фамилия не православная")
        
            if '@gmail.com' not in email:
                raise ValueError("почта не православная")
            
        except Exception as e: 
            print(f'{e}')
        else:
            self.name=name
            self.surname=surname
            self.age=age
            self.email=email

    def __del__(self):
        pass

a=Persona("afv",'fwef',123,'123321@gmail.com')


   