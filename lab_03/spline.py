class PiecewiseSpline():
    def __init__(self, a, b, c, d, prev_x):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.prev_x = prev_x
    def count_in_x(self, x):
        return self.a + self.b * (x - self.prev_x) + self.c * (x - self.prev_x) ** 2 + self.d * (x - self.prev_x) ** 3 
    

class Spline():
    def __init__(self, table, ledge, redge):
        self.x = [x[0] for x in table]
        self.y = [y[1] for y in table]
        
        self.ledge = ledge
        self.redge = redge
        
        self.splines = []
        self.build_spline()
    
    def build_spline(self):
        N = len(self.x)
        h = [self.x[i] - self.x[i-1] for i in range(1, N)]
        
        ksi = [0 for _ in range(N - 1)]
        et = [self.ledge / 2 for _ in range(N - 1)]
        
        for i in range(1, len(ksi)):
            A = h[i - 1]
            B = -2 * (h[i - 1] + h[i])
            D = h[i]
            F = -3 * ((self.y[i + 1] - self.y[i]) / h[i] - (self.y[i] - self.y[i - 1]) / h[i - 1])
            ksi[i] = D / (B - A * ksi[i - 1])
            et[i] = (A * et[i - 1] + F) / (B - A * ksi[i - 1])
        
        c = [0 for _ in range(N)]
        c[N - 1] = self.redge / 2
        c[0] = self.ledge / 2
        
        for i in range(len(ksi) - 1, 0, -1):
            c[i] = ksi[i] * c[i + 1] + et[i]
        
        a = [self.y[i - 1] for i in range(1, N)]
        b = [(self.y[i] - self.y[i - 1]) / h[i - 1] - 1 / 3 * h[i - 1] * (c[i] + 2 * c[i - 1]) for i in range(1, N)]
        d = [(c[i] - c[i - 1]) / (3 * h[i - 1]) for i in range(1, N)]
        
        
        for i in range(N - 1):
            self.splines.append(PiecewiseSpline(a[i], b[i], c[i], d[i], self.x[i]))
    
    
    def aproximate_value(self, aprox_x):
        pos = 0
        for i in range(1, len(self.x)):
            if self.x[i] >= aprox_x:
                break
            else:
                pos += 1
                
        if pos == 10:
            pos -= 1
        return self.splines[pos].count_in_x(aprox_x)
    
    