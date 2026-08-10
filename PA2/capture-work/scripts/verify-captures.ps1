[CmdletBinding()]
param()

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Continue'

$CaptureRoot = 'C:\Users\Administrator\Documents\MEGA\tkgd\PA2\capture-work'
$ManifestPath = 'C:\Users\Administrator\Documents\MEGA\tkgd\PA2\capture-work\capture-manifest.csv'
$LogPath = 'C:\Users\Administrator\Documents\MEGA\tkgd\PA2\capture-work\capture-log.md'
$Errors = [System.Collections.Generic.List[string]]::new()

if (-not (Test-Path -LiteralPath $ManifestPath)) {
    throw "Manifest not found: $ManifestPath"
}

Add-Type -AssemblyName System.Drawing
$Manifest = @(Import-Csv -LiteralPath $ManifestPath)
$PngFiles = @(
    Get-ChildItem -LiteralPath "$CaptureRoot\fifa", "$CaptureRoot\chess", "$CaptureRoot\failed" -Filter *.png -File -Recurse
)

$DuplicateNames = $PngFiles | Group-Object Name | Where-Object Count -gt 1
foreach ($Duplicate in $DuplicateNames) {
    $Errors.Add("Duplicate filename: $($Duplicate.Name)")
}

foreach ($File in $PngFiles) {
    if ($File.Length -le 0) {
        $Errors.Add("Empty file: $($File.FullName)")
        continue
    }
    try {
        $Image = [System.Drawing.Image]::FromFile($File.FullName)
        try {
            if ($Image.Width -le 0 -or $Image.Height -le 0) {
                $Errors.Add("Invalid dimensions: $($File.FullName)")
            }
            Write-Output ('OK`t{0}`t{1}x{2}`t{3} bytes' -f $File.FullName, $Image.Width, $Image.Height, $File.Length)
        }
        finally {
            $Image.Dispose()
        }
    }
    catch {
        $Errors.Add("Unreadable PNG: $($File.FullName)")
    }

    $Matches = @($Manifest | Where-Object { $_.absolute_path -eq $File.FullName })
    if ($Matches.Count -eq 0) {
        $Errors.Add("No manifest row: $($File.FullName)")
    }
    elseif ($Matches.Count -gt 1) {
        $Errors.Add("Multiple manifest rows: $($File.FullName)")
    }
}

foreach ($Row in $Manifest | Where-Object { $_.filename }) {
    if (-not (Test-Path -LiteralPath $Row.absolute_path)) {
        $Errors.Add("Manifest file missing: $($Row.absolute_path)")
    }
}

$Timestamp = Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz'
Add-Content -LiteralPath $LogPath -Encoding UTF8 -Value "`n## $Timestamp`n"
Add-Content -LiteralPath $LogPath -Encoding UTF8 -Value "- Lệnh: verify-captures.ps1"
Add-Content -LiteralPath $LogPath -Encoding UTF8 -Value "- Kết quả kỹ thuật: $($PngFiles.Count) PNG; $($Errors.Count) lỗi kiểm tra."

if ($Errors.Count -gt 0) {
    $Errors | ForEach-Object { Write-Error $_ }
    exit 1
}

Write-Output "Verification complete: $($PngFiles.Count) PNG files, no technical errors."
