class Start():
    def __init__(self):
        self.employees = [Employee('','','') for i in range(5)]
        self.viewers = [Viewer('','','','','') for i in range(5)]

        self.attractions = [Attraction('','','','','','', self.employees,'') for i in range(5)]
        self.tills = [Till('', '', '', self.employees, '') for i in range(5)]
        self.outlets = [Outlet('','',self.employees,'') for i in range (5)]

        self.system = System('','',self.tills, self.outlets, self.attractions)

    def main(self):
        self.system.start()

class System():
    def __init__(self, time, user, list_of_tills, list_of_outlets, list_of_attractions):
        self._time = time
        self._user = user

        self._list_of_tills = list_of_tills
        self._list_of_outlets = list_of_outlets
        self._list_of_attractions = list_of_attractions

    def start(self):
        pass

    def authorization(self, user):
        #авторизация текущего пользователя
        pass

    def add_employee(self, user):
        #добавление нового сотрудника в список сотрудников
        pass

    def buy_ticket(self, attractions):
        #покупка билетов посетителем
        pass

    def check_ticket(self, tickets, viewer):
        #проверка билетов сотрудником
        pass

    def form_order(self, products, viewer):
        #оформление заказа
        pass

    def review(self, attractions):
        #оставить отзыв
        pass

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value


class Authorization():
    def __init__(self, list_of_users):
        self.list_of_users = list_of_users

    def new_user(self):
        #добавление нового пользователя при регистрации
        pass

    def authorization(self):
        #авторизация созданного пользователя
        pass


class User():
    def __init__(self, login, password, bill, role):
        self._login = login
        self._password = password
        self._bill = bill
        self.role = role

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        self._login = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def bill(self):
        return self._bill

    @bill.setter
    def bill(self, value):
        self._bill = value

    @property
    def role(self):
        return self.role

    @role.setter
    def role(self, value):
        self.role = value

    def add_to_bill(self, sum):
        #пополнение счета пользователя на определенную сумму
        pass


class Viewer(User):
    def __init__(self, login, password, bill, list_of_tickets, list_of_products):
        super().__init__(login, password, bill, 'viewer')
        self._list_of_tickets = list_of_tickets
        self._list_of_products = list_of_products

    def buy_ticket(self, tickets):
        #посетитель покупает билеты
        pass

    def buy_product(self, products):
        # посетитель покупает товары
        pass

    def review(self, attractions):
        # посетитель оставляет отзыв
        pass


class Employee(User):
    def __init__(self, login, password, bill):
        super().__init__(login, password, bill, 'employee')

    def check_ticket(self, viewer_tickets, viewer):
        # сотрудник проверяет билеты
        pass

    def form_order(self, viewer_products, viewer):
        # сотрудник оформляет заказ
        pass


class Attraction():
    def __init__(self, x, y, action, description, capacity, reviews, employees, tickets):
        self.location = {x, y}
        self.action = action
        self.description = description
        self.capacity = capacity
        self.reviews = reviews
        self.employees = employees
        self.tickets_in_order = tickets

    def work(self):
        # смена активности аттракциона
        pass

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._capacity = value

    @property
    def review(self):
        return self._review

    @review.setter
    def review(self, value):
        self._review = value


class Till():
    def __init__(self, x, y, action, employees, tickets):
        self.location = {x, y}
        self.action = action
        self.list_of_employees = employees
        self.list_of_tickets = tickets

    def work(self):
        # смена активности кассы
        pass

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value


class Outlet():
    def __init__(self, x, y, action, employees):
        self.location = {x, y}
        self.action = action
        self.list_of_employees = employees

    def work(self):
        # смена активности торговой точки
        pass

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value


class Ticket():
    def __init__(self, cash, action):
        self.cash = cash
        self.action = action

    @property
    def cash(self):
        return self.cash

    @cash.setter
    def cash(self, value):
        self.cash = value

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value


class Product():
    def __init__(self, cash, action, outlets):
        self.cash = cash
        self.action = action
        self.list_of_outlets = outlets

    @property
    def cash(self):
        return self.cash

    @cash.setter
    def cash(self, value):
        self.cash = value

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value