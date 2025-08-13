# Programa: Cálculo del IMC con opciones de guardar, leer y borrar
# Autor: Jonathan Monrroy
# Descripción: Script para calcular el IMC, clasificarlo y gestionar la información en archivo local

# Definición de las categorías
bajoPeso = "Bajo peso";
pesoNormal = "Peso normal";
sobrePeso = "Sobrepeso";

# Bucle principal
while true
    # Mostrar menú de opciones
    fprintf("\n==============================\n");
    fprintf("     CÁLCULO DE IMC - MENÚ\n");
    fprintf("==============================\n");
    fprintf("1. Calcular IMC y guardar información\n");
    fprintf("2. Leer información guardada\n");
    fprintf("3. Borrar archivo de información\n");
    fprintf("4. Salir del programa\n");
    fprintf("==============================\n");

    # Leer la opción del usuario
    opcion = input("Seleccione una opción (1-4): ");

    # Validar la opción ingresada
    if opcion < 1 || opcion > 4
        fprintf("Opción inválida. Intente de nuevo.\n");
        continue;
    end

    # Ejecutar acción según la opción
    switch opcion
        case 1
            # Leer datos del usuario
            nombre = input("Ingrese su nombre: ", "s");
            peso = input("Ingrese su peso en kilogramos: ");
            altura = input("Ingrese su altura en metros: ");

            # Calcular IMC
            imc = peso / (altura^2);

            # Determinar la categoría del IMC
            if imc < 18.5
                categoria = bajoPeso;
            elseif imc >= 18.5 && imc < 25
                categoria = pesoNormal;
            else
                categoria = sobrePeso;
            end

            # Mostrar resultados
            fprintf("\n%s, su IMC es: %.2f\n", nombre, imc);
            fprintf("Categoría: %s\n", categoria);

            # Guardar en archivo
            archivo = fopen("imc.txt", "a");
            fprintf(archivo, "Nombre: %s | Peso: %.2f kg | Altura: %.2f m | IMC: %.2f | Categoría: %s\n", ...
                    nombre, peso, altura, imc, categoria);
            fclose(archivo);
            fprintf("Información guardada correctamente.\n");

        case 2
            # Leer información del archivo
            if exist("imc.txt", "file")
                archivo = fopen("imc.txt", "r");
                contenido = fread(archivo, "*char")';
                fclose(archivo);
                fprintf("\n--- CONTENIDO DEL ARCHIVO ---\n");
                fprintf("%s\n", contenido);
            else
                fprintf("\nNo se encontró información guardada.\n");
            end

        case 3
            # Borrar archivo
            if exist("imc.txt", "file")
                delete("imc.txt");
                fprintf("Archivo eliminado exitosamente.\n");
            else
                fprintf("No hay archivo para eliminar.\n");
            end

        case 4
            # Salir del programa
            fprintf("\nGracias por usar el programa. ¡Hasta pronto!\n");
            break;
    endswitch
end

