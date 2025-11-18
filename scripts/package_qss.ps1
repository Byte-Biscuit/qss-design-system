<#
.SYNOPSIS
    Package qss file and icons into a versioned zip archive.

.DESCRIPTION
    This script reads the project version from the project's pyproject.toml
    (the value of `version = "..."`), copies `qss_desigin_system.qss` and
    the `icons` directory from `src/main/ui` into a temporary staging
    directory, and creates a zip archive named
    `qss-desigin-system.<version>.zip` under the `dist` directory at the
    project root.

.USAGE
    .\package_qss.ps1
    .\package_qss.ps1 -ProjectRoot 'C:\path\to\repo' -OutDir 'C:\outdir'

.PARAMETER ProjectRoot
    The path to the project root. Defaults to the parent folder of the script.

.PARAMETER OutDir
    Destination folder for the produced zip. Defaults to <ProjectRoot>\dist

#>

[CmdletBinding()]
param(
    [string]$ProjectRoot = (Split-Path -Parent $PSScriptRoot),
    [string]$OutDir
)

if (-not $OutDir) {
    $OutDir = Join-Path $ProjectRoot 'dist'
}

Write-Host "Project root: $ProjectRoot"
Write-Host "Output dir: $OutDir"

$pyproject = Join-Path $ProjectRoot 'pyproject.toml'
if (-not (Test-Path $pyproject)) {
    Write-Error "pyproject.toml not found at $pyproject"
    exit 2
}

$toml = Get-Content -Raw -Path $pyproject

function Get-VersionFromPyProject {
    $pyproject = Join-Path $ProjectRoot 'pyproject.toml'
    if (-not (Test-Path $pyproject)) {
        throw "pyproject.toml not found in current directory: $PWD"
    }
    $content = Get-Content $pyproject -Raw
    # naive TOML parse for project.version
    if ($content -match 'version\s*=\s*"(?<ver>[0-9]+\.[0-9]+\.[0-9]+[0-9A-Za-z\.-]*)"') {
        return $Matches['ver']
    }
    throw 'Unable to find version string in pyproject.toml'
}

$version = Get-VersionFromPyProject


$uiDir = Join-Path $ProjectRoot 'src\main\ui'
$qssFile = Join-Path $uiDir 'qss_desigin_system.qss'
$iconsDir = Join-Path $uiDir 'icons'

if (-not (Test-Path $qssFile)) {
    Write-Error "QSS file not found at $qssFile"
    exit 4
}

if (-not (Test-Path $iconsDir)) {
    Write-Warning "Icons directory not found at $iconsDir. The archive will contain the QSS file only."
}

# Create staging folder in TEMP
$guid = [Guid]::NewGuid().ToString()
$staging = Join-Path $env:TEMP "qss_package_$guid"
if (Test-Path $staging) { Remove-Item $staging -Recurse -Force }
New-Item -ItemType Directory -Path $staging | Out-Null

Write-Host "Staging area: $staging"

Copy-Item -Path $qssFile -Destination (Join-Path $staging (Split-Path $qssFile -Leaf)) -Force

if (Test-Path $iconsDir) {
    Copy-Item -Path $iconsDir -Destination (Join-Path $staging 'icons') -Recurse -Force
}

New-Item -ItemType Directory -Path $OutDir -Force | Out-Null

$zipName = "qss-desigin-system.$version.zip"
$destZip = Join-Path $OutDir $zipName

if (Test-Path $destZip) {
    Write-Host "Removing existing archive: $destZip"
    Remove-Item $destZip -Force
}

Write-Host "Creating archive $destZip ..."

try {
    # Compress-Archive accepts files and folders; use the wildcard to include contents
    Compress-Archive -Path (Join-Path $staging '*') -DestinationPath $destZip -Force
    Write-Host "Archive created: $destZip"
} catch {
    Write-Error "Failed to create archive: $_"
    Remove-Item $staging -Recurse -Force -ErrorAction SilentlyContinue
    exit 5
}

# Cleanup staging
Remove-Item $staging -Recurse -Force -ErrorAction SilentlyContinue

Write-Host "Done."
exit 0
