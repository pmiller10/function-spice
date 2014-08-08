import random
import math

class Game:

    games = {}
    current_id = 0

    @classmethod
    def get(self, game_id):
        return self.games[game_id]

    def __init__(self):
        self.function = Function.new_random_function()
        self.data = self.function.data
        self.game_id = self.current_id
        self.games[self.game_id] = self
        print 'current id is ', self.current_id
        Game.current_id += 1
        print 'incrementing current id to ', Game.current_id

class Function:

    min_variable = -3 
    max_variable = 3

    @classmethod
    def new_from_function(self, function):
        data = Function.generate_data(function)
        return Function(data, function)

    @classmethod
    def new_random_function(self):
        sub_klasses = [Linear, Lognormal, Exponential, Trig]
        klass = random.sample(sub_klasses, 1)[0]
        print 'using class '.format(klass)
        formula = klass.generate_formula()
        return self.new_from_function(formula)

    @classmethod
    def generate_data(self, function):
        y_values = []
        x_values = range(-3,4)
        # TODO this is only a temporary try function
        for x in x_values:
            try:
                y_values.append(eval(function, {'x': x, 'math': math}))
            except Exception:
                print Warning('failed: {0} with {1}'.format(function, x))
                y_values.append(0.0)
        assert len(y_values) == len(x_values)

        return y_values

    def __init__(self, data, formula):
        self.data = data
        self.formula = formula

    def is_equal(self, other_function):
        return self.data == other_function.data

class Linear(Function):

    @classmethod
    def generate_formula(self):
        m = random.randint(self.min_variable, self.max_variable)
        b = random.randint(self.min_variable, self.max_variable)
        return "{0} * x + {1}".format(m, b)

class Lognormal(Function):

    @classmethod
    def generate_formula(self):
        # don't use 0
        b = 0
        while b == 0:
            b = random.randint(self.min_variable, self.max_variable)
        print b
        print 'log'
        return "({0}) ** x".format(b)

class Exponential(Function):
    @classmethod
    def generate_formula(self):
        y = 0
        while y == 0:
            y = random.randint(self.min_variable, self.max_variable)
        print y
        print 'exp'
        return "(x) ** {0}".format(y)

class Trig(Function):

    @classmethod
    def generate_formula(self):
        function = random.sample(['cos', 'sin', 'tan'], 1)[0]
        return 'math.' + function + '(x)'

class Polynomial(Function):

    @classmethod
    def generate_formula(self):
        order = random.randint(1,2)
        exponents = range(2,6)
        selected_exponents = random.sample(exponents, order)
        a = random.randint(self.min_variable, self.max_variable)
        formula = "{0} * x ".format(a)
        for exp in selected_exponents:
            a = random.randint(self.min_variable, self.max_variable)
            formula += "+ {0} * (x) ** {1}".format(a, exp)
        return formula
