def calcular_tasa(P, A, n, tol=1e-6, max_iter=1000):
    """
    Calcula la tasa de interés mensual y anual de un préstamo.
    
    Parámetros:
    P: Monto prestado (capital inicial)
    A: Cuota mensual
    n: Plazo en meses
    tol: Tolerancia para la convergencia del método numérico
    max_iter: Número máximo de iteraciones
    
    Retorna:
    - Tasa efectiva anual (TEA)
    - Tasa mensual
    """
    
    r = 0.05  # Suposición inicial (5%)
    for _ in range(max_iter):
        f_r = P - (A * (1 - (1 + r) ** -n) / r)
        f_r_deriv = (A * ((1 + r) ** -n * n / (1 + r) - 1) / r**2)
        
        if abs(f_r) < tol:
            break
        
        r -= f_r / f_r_deriv
    
    # Calcular tasas anuales
    tasa_efectiva_anual = (1 + r) ** 12 - 1
    
    return tasa_efectiva_anual, r

# Ejemplo de uso
#P = 4900000   # Monto prestado
#A = 210922    # Cuota mensual
#n = 36        # Plazo en meses
#
#tasa_efectiva_anual, tasa_mensual = calcular_tasa(P, A, n)
#
#print(f"Tasa efectiva anual (TEA): {tasa_efectiva_anual:.4%}")
#print(f"Tasa mensual: {tasa_mensual:.4%}")