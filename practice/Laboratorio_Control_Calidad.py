mC_uno = mC_dos = mC_tres = 0.0 #Muestra uno, dos y tres.
mMg_uno = mMg_dos = mMg_tres = 0.0 #Muestra uno, dos y tres.
promC = promMg = 0.0
loss_boxes = boxes = 0
money_loss = 0
porc_loss_boxes = 0
num_lote = 0
estatus = ""


archivo = open("Lotes.txt")
print("\nNro Lote      Prom %C       Prom %Mg    Estatus")
for registro in archivo:
    campos = registro.split(",")
    num_lote = campos[0]
    mC_uno = float(campos[1])
    mC_dos = float(campos[2])
    mC_tres = float(campos[3])
    mMg_uno = float(campos[4])
    mMg_dos = float(campos[5])
    mMg_tres = float(campos[6])
    promC = (mC_uno + mC_dos + mC_tres)/3
    promMg = (mMg_uno + mMg_dos + mMg_tres)/3
    if (promC > 24.92 and promC < 27.92) and (promMg > 19.84 and promMg < 25.30):
        estatus = "Aprobado"
    else:
        estatus = "Rechazado"
        loss_boxes += 1
    boxes += 1
    print("{}         {:2.2f}         {:2.2f}       {}".format(num_lote, promC, promMg, estatus))

money_loss = loss_boxes * 75000
porc_loss_boxes = (loss_boxes / boxes) * 100
print("Monto de las perdidas por lotes rechazados: {}Bss".format(money_loss))
print("Porcentaje de cajas perdidas: {}%".format(porc_loss_boxes))
print("\nFin del programa.")
