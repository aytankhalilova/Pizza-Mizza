import abc

class Pizza(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_price(self):
        pass

    @abc.abstractmethod
    def get_status(self):
        pass


class Funghi(Pizza):
    def __init__(self):
        self.__pizza_price=6.0

    def get_price(self):
        return self.__pizza_price

    def get_status(self):
        return "Funghi"


class Hawaii(Pizza):
    def __init__(self):
        self.__pizza_price=8.0

    def get_price(self):
        return self.__pizza_price

    def get_status(self):
        return "Hawaii"


class PizzaDecorator(Pizza):
    def __init__(self,pizza):
        self.pizza=pizza

    def get_price(self):
        return self.pizza.get_price()

    def get_status(self):
        return self.pizza.get_status()


class  Mozzarella(PizzaDecorator):
    def __init__(self,pizza):
        super().__init__(pizza)
        self.__mozzarella_price=2.0

    @property
    def price(self):
        return self.__mozzarella_price

    def get_price(self):
        return super().get_price()+self.price

    def get_status(self):
        return super().get_status()+"  Mozzarella"

class Tomato_Sauce(PizzaDecorator):
    def __init__(self,pizza):
        super().__init__(pizza)
        self.__tomato_sauce_price=1.0

    @property
    def price(self):
        return self.__tomato_sauce_price

    def get_price(self):
        return super().get_price()+self.price

    def get_status(self):
        return super().get_status()+" Tomato Sauce"

class Mushroom(PizzaDecorator):
    def __init__(self,pizza):
        super().__init__(pizza)
        self.__mushroom_price=3.0

    @property
    def price(self):
        return self.__mushroom_price

    def get_price(self):
        return super().get_price()+self.price

    def get_status(self):
        return super().get_status()+" Mushroom"

class Pineapple(PizzaDecorator):
    def __init__(self,pizza):
        super().__init__(pizza)
        self.__pineapple_price=5.0

    @property
    def price(self):
        return self.__pineapple_price

    def get_price(self):
        return super().get_price()+self.price

    def get_status(self):
        return super().get_status()+" Pineapple"


class PizzaBuilder():
    def __init__(self,pizza_type):
        self.pizza_type=pizza_type
        self.pizza=eval(pizza_type)()
        self.extentions_list=[]

    def add_extention(self,extention):
        if extention=="Mozzarella":
            self.pizza=Mozzarella(self.pizza)
        elif extention=="Tomato_Sauce":
            self.pizza=Tomato_Sauce(self.pizza)
        elif extention=="Mushroom":
            self.pizza=Mushroom(self.pizza)
        elif extention=="Pineapple":
            self.pizza=Pineapple(self.pizza)


        self.extentions_list.append(extention)

    def remove_extention(self,extention):
        if extention in self.extentions_list:
            self.extentions_list.remove(extention)

        temp_pizza=eval(self.pizza_type)()
        for i in self.extentions_list:
            temp_pizza=eval(i)(temp_pizza)

        self.pizza=temp_pizza

    def get_status(self):
        return self.pizza.get_status()

    def get_price(self):
        return self.pizza.get_price()
