
# Menú de gestión de usuarios en PowerShell

while ($true) {
    Clear-Host
    Write-Host "1. Crear usuario"
    Write-Host "2. Crear un grupo"
    Write-Host "3. Añadir usuario a un grupo"
    Write-Host "4. Establecer contraseña que no caduque"
    Write-Host "5. Deshabilitar cuenta"
    Write-Host "6. Generar informe"
    Write-Host "7. Salir"
    
    $opcion = Read-Host "Seleccione una opción"
    
    if ($opcion -eq "1") {
        $nombreUsuario = Read-Host "Ingrese el nombre del usuario"
        $descripcion = Read-Host "Ingrese la descripción del usuario (departamento)"
        $contraseña = Read-Host "Ingrese la contraseña" -AsSecureString
        New-LocalUser -Name $nombreUsuario -Password $contraseña -FullName $nombreUsuario -Description $descripcion
    }
    
    elseif ($opcion -eq "2") {
        $nombreGrupo = Read-Host "Ingrese el nombre del grupo"
        if (-not (Get-LocalGroup -Name $nombreGrupo -ErrorAction SilentlyContinue)) {
            New-LocalGroup -Name $nombreGrupo
        }
    }
    
    elseif ($opcion -eq "3") {
        $nombreGrupo = Read-Host "Ingrese el nombre del grupo"
        $nombreUsuario = Read-Host "Ingrese el nombre del usuario"
        Add-LocalGroupMember -Group $nombreGrupo -Member $nombreUsuario
    }
    
    elseif ($opcion -eq "4") {
        $nombreUsuario = Read-Host "Ingrese el nombre del usuario"
        Set-LocalUser -Name $nombreUsuario -PasswordNeverExpires $true
    }
    
    elseif ($opcion -eq "5") {
        $nombreUsuario = Read-Host "Ingrese el nombre del usuario"
        Disable-LocalUser -Name $nombreUsuario
    }
    
    elseif ($opcion -eq "6") {
        $informe = "C:\Informe_Usuarios.txt"
        Get-LocalUser | Select-Object Name, Enabled, Description | Format-Table | Out-File $informe
        Get-LocalGroup | ForEach-Object {
            "Grupo: $_" | Out-File $informe -Append
            Get-LocalGroupMember -Group $_ | Out-File $informe -Append
        }
        Write-Host "Informe generado en $informe"
    }
    
    elseif ($opcion -eq "7") {
        break
    }
    
    else {
        Write-Host "Opción no válida, intente de nuevo."
    }
    
    Pause
}
