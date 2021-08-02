function Set-FlaskEnv {
    [CmdletBinding(SupportsShouldProcess = $true, ConfirmImpact = 'Low')]
    param($CmdArgs)

    if ($CmdArgs -like "dev") {
        Write-Output "Setting FLASK_ENV='development'"
        [Environment]::SetEnvironmentVariable("FLASK_ENV", "development", "Process") | Out-Null
    }

    elseif ($CmdArgs -like "prod") {
        Write-Output "Setting FLASK_ENV='production'"
        [Environment]::SetEnvironmentVariable("FLASK_ENV", "production", "Process") | Out-Null
    }

    elseif ($CmdArgs -like "clear" -or $CmdArgs -like "clr") {
        Write-Output "Clearing FLASK_ENV"
        [Environment]::SetEnvironmentVariable("FLASK_ENV", "", "Process") | Out-Null
    }
#    if ($PSCmdlet.ShouldProcess("environment variable $key", "set value $value")) {
#        [Environment]::SetEnvironmentVariable($key, $value, "Process") | Out-Null
#    }
}

Set-FlaskEnv($args)