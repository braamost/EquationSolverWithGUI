from math import *
from convertToFunc import create_function_from_expression
from significantFigures import round_to_significantFigures

def false_position(expression, a, b, significantFigures, tol=0.00001, maxIterations=50):

    f = create_function_from_expression(expression)
    
   
    a = round_to_significantFigures(a, significantFigures)
    b = round_to_significantFigures(b, significantFigures)
    
    if a >= b:
        raise ValueError("(b) must be greater than (a)")
    
    
    fa = round_to_significantFigures(f(a), significantFigures)
    fb = round_to_significantFigures(f(b), significantFigures)
    
    if fa * fb >= 0:
        raise ValueError(f"method may fail.")
    
    it = 0
    previous_c = a
    correct_sig_figs = 0
    
    while True:
        it += 1
        
        numerator = round_to_significantFigures(a*fb - b*fa, significantFigures)
        denominator = round_to_significantFigures(fb - fa, significantFigures)
        c = round_to_significantFigures(numerator/denominator, significantFigures)
        
        fc = round_to_significantFigures(f(c), significantFigures)
        
       
        if c != 0:
            relative_error = abs(c - previous_c) / abs(c) * 100
        else:
            relative_error = abs(c - previous_c) * 100
        
     
        correct_sig_figs = floor(2 - log10(2 * relative_error))
        
       
        if relative_error <= tol:
            break
            
        if fc == 0:  
            break
        elif fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        
        previous_c = c
        
        
        if it >= maxIterations:
            print(f"Warning: Maximum iterations ({maxIterations}) reached")
            break
    
    return {
        'root': round_to_significantFigures(c, significantFigures),
        'iterations': it,
        'relative_error': round_to_significantFigures(relative_error, significantFigures),
        'correct_Significant_Figures': correct_sig_figs,
        'function_value': round_to_significantFigures(fc, significantFigures)
    }

print(false_position("3*x**4+6.1*x**3-2*x**2+3*x+2 ", -1, 0,6,tol=0.01)) 