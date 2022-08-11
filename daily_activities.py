import os
import time
import utils

# Menu Operation
while True:
    utils.clear_console()
    selected_option = input(
        '1 - Ingresar actividad\n' +
        '2 - Ver actividades\n' +
        '3 - Salir\n' +
        '¿Que operación quieres registrar? '
    )

    if selected_option == '1':
        utils.clear_console()
        print(utils.curent_date_letter())
        file_name = f'Actividades-{utils.month_letter()}.txt'
        activity = input('Ingresa Actividad (Escribe "cancelar" para regresar): ')

        if activity.lower() == 'cancelar':
            continue

        if not os.path.isfile(file_name):
            with open(file_name, "w") as file:
                file.write(utils.curent_date_letter() + utils.new_line)
                file.write(utils.line)
                file.write(activity + utils.new_line)
        else:
            with open(file_name) as file:
                if utils.curent_date_letter() not in file.read():
                    with open(file_name, "a") as file:
                        file.write(utils.new_line)
                        file.write(utils.curent_date_letter() + utils.new_line)
                        file.write(utils.line)
            with open(file_name, "a") as file:
                file.write(activity + utils.new_line)
                utils.clear_console()
                print('¡Actividad agregada!')
                time.sleep(1)

    elif selected_option == '2':
        utils.clear_console()
        try:
            file_month = input(f'¿De que mes(Actual="{utils.month_letter()})"?: ').title()
            os.startfile(f'Actividades-{file_month}.txt') # Abrir archivo de acuerdo al mes .txt
        except:
            print('Ingreso un mes invalido')
            time.sleep(1)
            continue

    elif selected_option == '3':
        exit()
