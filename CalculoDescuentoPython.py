def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento aplicado a una compra.
    
    Args:
        monto_total (float): Monto total de la compra (ej: 100.50).
        porcentaje_descuento (int, optional): Porcentaje de descuento. Por defecto es 10.
    
    Returns:
        float: Monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)  # Fórmula matemática
    return descuento
  if __name__ == "__main__":
    # Llamada 1: Descuento predeterminado (10%)
    compra_1 = 5000  # Monto en dólares, pesos, etc.
    descuento_1 = calcular_descuento(compra_1)  # No se especifica el segundo parámetro
    total_1 = compra_1 - descuento_1

    # Llamada 2: Descuento personalizado (15%)
    compra_2 = 8000
    descuento_personalizado = 15  # Porcentaje
    descuento_2 = calcular_descuento(compra_2, descuento_personalizado)
    total_2 = compra_2 - descuento_2
    # Formato de salida para la primera compra
    print("=== Detalles de la Compra 1 ===")
    print(f"- Monto original: ${compra_1:.2f}")
    print(f"- Descuento aplicado ({descuento_1 / compra_1 * 100:.0f}%): ${descuento_1:.2f}")
    print(f"- Total a pagar: ${total_1:.2f}\n")  # \n añade una línea en blanco

    # Formato de salida para la segunda compra
    print("=== Detalles de la Compra 2 ===")
    print(f"- Monto original: ${compra_2:.2f}")
    print(f"- Descuento aplicado ({descuento_personalizado}%): ${descuento_2:.2f}")
    print(f"- Total a pagar: ${total_2:.2f}")
