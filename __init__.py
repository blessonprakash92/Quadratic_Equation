# Crating Quadratic Equation Package for Python Library

class Solve_Quad_Ed(object):
    def __init__(self, a, b, c):
        self.a = a
        '''
        Coefficient a should be > 0 in order for the 
        equation to remain quadratic in nature
        '''
        self.b = b
        self.c = c

        d = b * b - 4 * a * c

        if d < 0:
            print('Complex solution exists')
            print('Program cannot solve solutions with complex values')
            print('Shutting down in process...')
            print('.')
            print('.')
            print('.')
            print('.')
            print('.')
            print('.')
            print('Shut down complete')
            print('Please try again')

        else:
            x1 = (-b + d ** 0.5) / (2 * a)
            x2 = (-b + d ** 0.5) / (2 * a)
            print('The value of x1 is = ', x1)
            print('The value of x2 is = ', x2)