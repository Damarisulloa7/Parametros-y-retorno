def calcular_descuento(monto_total: float, porcentaje_descuento: float = 10) -> float:
    """
  Calcula el descuento aplicando un porcentaje al monto total de compra

  Args:
      monto_total: Monto total de la compra
      porcentaje_descuento: Porcentaje de descuento (valor predeterminado 10%)

  Returns:
      Monto del descuento calculado
  """
    return monto_total * (porcentaje_descuento / 100)


if __name__ == "__main__":
    # Primera llamada (descuento predeterminado 10%)
    compra1 = 5000.00
    descuento1 = calcular_descuento(compra1)
    total1 = compra1 - descuento1

    # Segunda llamada (descuento personalizado 15%)
    compra2 = 8000.00
    descuento2 = calcular_descuento(compra2, 15)
    total2 = compra2 - descuento2

    # Mostrar resultados con formato detallado
    print("\n" + "═" * 50)
    print(f"| {'CÁLCULO DE DESCUENTOS':^46} |")
    print("═" * 50)

    # Resultado primera compra
    print(f"| {'Compra 1 (10% predeterminado)':<30} |")
    print(f"| {'Monto original:':<20} ${compra1:>10.2f}   |")
    print(f"| {'Descuento aplicado:':<20} ${descuento1:>10.2f}   |")
    print(f"| {'Total con descuento:':<20} ${total1:>10.2f}   |")
    print("|" + "-" * 48 + "|")

    # Resultado segunda compra
    print(f"| {'Compra 2 (15% personalizado)':<30} |")
    print(f"| {'Monto original:':<20} ${compra2:>10.2f}   |")
    print(f"| {'Descuento aplicado:':<20} ${descuento2:>10.2f}   |")
    print(f"| {'Total con descuento:':<20} ${total2:>10.2f}   |")
    print("═" * 50 + "\n")
