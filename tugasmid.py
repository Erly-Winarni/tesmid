import sympy as sp

def temukan_domain_dan_range():
    x = sp.Symbol('x')
    expr = sp.sympify()

    domain = sp.calculus.util.continous_domain(expr, x, sp.S.Reals)
    f_range = sp.calculus.util.function_range(expr, x, domain)
    return domain, f_range

def main():
    print("Program untuk mencari domain dan range dari sebuah fungsi.")

    expression = input("Masukkan fungsi dalam variabel x (misalnya: 1/(x-1), sqrt(x), x**2 - 4): ")

    try: 
        domain, f_range = temukan_domain_dan_range()

        print(f"Domain dari fungsi {expression}: {domain}")
        print(f"Range dari fungsi {expression}: {f_range}")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

main()



