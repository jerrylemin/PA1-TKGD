[CmdletBinding()]
param()

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Continue'

$CaptureRoot = 'C:\Users\Administrator\Documents\MEGA\tkgd\PA2\capture-work'
$ManifestPath = 'C:\Users\Administrator\Documents\MEGA\tkgd\PA2\capture-work\capture-manifest.csv'
$LogPath = 'C:\Users\Administrator\Documents\MEGA\tkgd\PA2\capture-work\capture-log.md'
$AgentBrowserCommand = Get-Command agent-browser -ErrorAction SilentlyContinue

$RequiredDirectories = @(
    $CaptureRoot,
    "$CaptureRoot\fifa\desktop",
    "$CaptureRoot\fifa\mobile",
    "$CaptureRoot\fifa\states",
    "$CaptureRoot\chess\desktop",
    "$CaptureRoot\chess\mobile",
    "$CaptureRoot\chess\states",
    "$CaptureRoot\failed",
    "$CaptureRoot\scripts"
)
foreach ($Directory in $RequiredDirectories) {
    New-Item -ItemType Directory -Path $Directory -Force | Out-Null
}

if (-not $AgentBrowserCommand) {
    Add-Content -LiteralPath $LogPath -Encoding UTF8 -Value "`n## $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')`n`n- Command: check agent-browser.`n- Technical result: agent-browser was not found.`n"
    throw 'agent-browser is required.'
}
$AgentBrowser = Join-Path (Split-Path -Parent $AgentBrowserCommand.Source) 'node_modules\agent-browser\bin\agent-browser-win32-x64.exe'
if (-not (Test-Path -LiteralPath $AgentBrowser)) {
    $AgentBrowser = (Get-Command agent-browser.cmd -ErrorAction Stop).Source
}

if (-not (Test-Path -LiteralPath $ManifestPath)) {
    'capture_id,product,viewport,page_area,state,source_url,final_url,page_title,filename,absolute_path,captured_at_local,width_px,height_px,file_size_bytes,popup_action,authentication_state,status,failure_reason,related_pa1_figure,related_pa1_use_case,notes_factual_only' |
        Set-Content -LiteralPath $ManifestPath -Encoding UTF8
}

$ExistingRows = @(Import-Csv -LiteralPath $ManifestPath)
$script:CaptureSequence = $ExistingRows.Count

function Write-CaptureLog {
    param([Parameter(Mandatory)][string]$Message)
    Add-Content -LiteralPath $LogPath -Encoding UTF8 -Value "- $Message"
}

function Start-LogSection {
    param([Parameter(Mandatory)][string]$Url)
    Add-Content -LiteralPath $LogPath -Encoding UTF8 -Value "`n## $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')`n"
    Write-CaptureLog "URL: $Url"
}

function Invoke-AgentBrowser {
    param(
        [Parameter(Mandatory)][string]$Session,
        [Parameter(Mandatory)][string[]]$Arguments
    )
    $Printable = 'agent-browser --session ' + $Session + ' ' + ($Arguments -join ' ')
    Write-CaptureLog "Command: $Printable"
    $Output = & $AgentBrowser --session $Session @Arguments 2>&1 | Out-String
    $ExitCode = $LASTEXITCODE
    $Excerpt = (($Output -replace '\s+', ' ').Trim())
    if ($Excerpt.Length -gt 300) {
        $Excerpt = $Excerpt.Substring(0, 300)
    }
    $ResultSummary = "exit code $ExitCode"
    if ($Excerpt) {
        $ResultSummary += ': ' + $Excerpt
    }
    Write-CaptureLog "Technical result: $ResultSummary"
    [pscustomobject]@{
        ExitCode = $ExitCode
        Output = $Output.Trim()
    }
}

function Get-UniquePath {
    param([Parameter(Mandatory)][string]$RequestedPath)
    if (-not (Test-Path -LiteralPath $RequestedPath)) {
        return $RequestedPath
    }
    $Directory = Split-Path -Parent $RequestedPath
    $BaseName = [System.IO.Path]::GetFileNameWithoutExtension($RequestedPath)
    $Extension = [System.IO.Path]::GetExtension($RequestedPath)
    for ($Run = 2; $Run -lt 100; $Run++) {
        $Candidate = Join-Path $Directory ('{0}-r{1:D2}{2}' -f $BaseName, $Run, $Extension)
        if (-not (Test-Path -LiteralPath $Candidate)) {
            return $Candidate
        }
    }
    throw "No unused output path for $RequestedPath"
}

function Get-ImageInfo {
    param([Parameter(Mandatory)][string]$Path)
    try {
        Add-Type -AssemblyName System.Drawing -ErrorAction Stop
        $Image = [System.Drawing.Image]::FromFile($Path)
        try {
            [pscustomobject]@{
                Width = $Image.Width
                Height = $Image.Height
                Bytes = (Get-Item -LiteralPath $Path).Length
                Readable = $true
            }
        }
        finally {
            $Image.Dispose()
        }
    }
    catch {
        [pscustomobject]@{
            Width = 0
            Height = 0
            Bytes = if (Test-Path -LiteralPath $Path) { (Get-Item -LiteralPath $Path).Length } else { 0 }
            Readable = $false
        }
    }
}

function Add-ManifestRow {
    param(
        [Parameter(Mandatory)][hashtable]$Values
    )
    $script:CaptureSequence++
    $Row = [ordered]@{
        capture_id = 'CAP-{0:D4}' -f $script:CaptureSequence
        product = $Values.Product
        viewport = $Values.Viewport
        page_area = $Values.PageArea
        state = $Values.State
        source_url = $Values.SourceUrl
        final_url = $Values.FinalUrl
        page_title = $Values.PageTitle
        filename = $Values.Filename
        absolute_path = $Values.AbsolutePath
        captured_at_local = $Values.CapturedAt
        width_px = $Values.Width
        height_px = $Values.Height
        file_size_bytes = $Values.Bytes
        popup_action = $Values.PopupAction
        authentication_state = $Values.AuthenticationState
        status = $Values.Status
        failure_reason = $Values.FailureReason
        related_pa1_figure = $Values.RelatedFigure
        related_pa1_use_case = $Values.RelatedUseCase
        notes_factual_only = $Values.Notes
    }
    [pscustomobject]$Row | Export-Csv -LiteralPath $ManifestPath -Append -NoTypeInformation -Encoding UTF8
}

function New-OutputPath {
    param(
        [Parameter(Mandatory)][pscustomobject]$Plan,
        [string]$Area = $Plan.Area,
        [string]$State = $Plan.State,
        [switch]$Failed,
        [switch]$States
    )
    $Timestamp = Get-Date -Format 'yyyyMMdd-HHmmss'
    $Name = '{0}-{1}-{2}-{3}-{4}.png' -f $Plan.Product, $Plan.Viewport, $Area, $State, $Timestamp
    $Directory = if ($Failed) {
        "$CaptureRoot\failed"
    }
    elseif ($States) {
        "$CaptureRoot\$($Plan.Product)\states"
    }
    else {
        "$CaptureRoot\$($Plan.Product)\$($Plan.Viewport)"
    }
    Get-UniquePath -RequestedPath (Join-Path $Directory $Name)
}

function Get-AuthenticationState {
    param([string]$FinalUrl, [string]$PageText)
    if ($FinalUrl -match '/login|/signin|sign-in') {
        return 'LoginRequired'
    }
    if ($PageText -match '(?i)sign in to continue|log in to continue|login required') {
        return 'LoginRequired'
    }
    return 'Guest'
}

function Get-BlockedReason {
    param([string]$Text)
    if ($Text -match '(?i)captcha|verify you are human|challenge-platform|bot protection') {
        return 'Bot protection or CAPTCHA was displayed.'
    }
    if ($Text -match '(?i)access denied|forbidden') {
        return 'Access was denied.'
    }
    return ''
}

function Save-CurrentPage {
    param(
        [Parameter(Mandatory)][pscustomobject]$Plan,
        [Parameter(Mandatory)][string]$Session,
        [Parameter(Mandatory)][string]$Path,
        [string]$PopupAction = '',
        [string]$Notes = '',
        [string]$ForcedStatus = ''
    )
    $Shot = Invoke-AgentBrowser -Session $Session -Arguments @('screenshot', $Path, '--full')
    if ($Shot.ExitCode -ne 0 -or -not (Test-Path -LiteralPath $Path)) {
        return [pscustomobject]@{ Success = $false; ExitCode = $Shot.ExitCode; Reason = $Shot.Output }
    }
    $Info = Get-ImageInfo -Path $Path
    if (-not $Info.Readable -or $Info.Bytes -le 0) {
        return [pscustomobject]@{ Success = $false; ExitCode = 1; Reason = 'PNG could not be opened or was empty.' }
    }
    $FinalUrlResult = Invoke-AgentBrowser -Session $Session -Arguments @('get', 'url')
    $TitleResult = Invoke-AgentBrowser -Session $Session -Arguments @('get', 'title')
    $ReadResult = Invoke-AgentBrowser -Session $Session -Arguments @('read')
    $FinalUrl = $FinalUrlResult.Output.Trim()
    $Title = $TitleResult.Output.Trim()
    $AuthenticationState = Get-AuthenticationState -FinalUrl $FinalUrl -PageText $ReadResult.Output
    $Status = if ($ForcedStatus) {
        $ForcedStatus
    }
    elseif ($Plan.ExpectScrollable -and $Info.Height -le $Plan.Height) {
        'PARTIAL'
    }
    else {
        'SUCCESS'
    }
    Add-ManifestRow -Values @{
        Product = $Plan.Product
        Viewport = $Plan.Viewport
        PageArea = $Plan.Area
        State = $Plan.State
        SourceUrl = $Plan.Url
        FinalUrl = $FinalUrl
        PageTitle = $Title
        Filename = [System.IO.Path]::GetFileName($Path)
        AbsolutePath = $Path
        CapturedAt = Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz'
        Width = $Info.Width
        Height = $Info.Height
        Bytes = $Info.Bytes
        PopupAction = $PopupAction
        AuthenticationState = $AuthenticationState
        Status = $Status
        FailureReason = ''
        RelatedFigure = $Plan.RelatedFigure
        RelatedUseCase = $Plan.RelatedUseCase
        Notes = $Notes
    }
    Write-CaptureLog "File output: $Path"
    [pscustomobject]@{ Success = $true; ExitCode = 0; Reason = ''; Info = $Info }
}

function Add-MissingState {
    param(
        [Parameter(Mandatory)][pscustomobject]$Plan,
        [Parameter(Mandatory)][string]$Reason,
        [string]$FinalUrl = '',
        [string]$Title = '',
        [string]$AuthenticationState = 'Guest',
        [string]$Status = 'MISSING_CURRENT_STATE'
    )
    Add-ManifestRow -Values @{
        Product = $Plan.Product
        Viewport = $Plan.Viewport
        PageArea = $Plan.Area
        State = $Plan.State
        SourceUrl = $Plan.Url
        FinalUrl = $FinalUrl
        PageTitle = $Title
        Filename = ''
        AbsolutePath = ''
        CapturedAt = Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz'
        Width = 0
        Height = 0
        Bytes = 0
        PopupAction = ''
        AuthenticationState = $AuthenticationState
        Status = $Status
        FailureReason = $Reason
        RelatedFigure = $Plan.RelatedFigure
        RelatedUseCase = $Plan.RelatedUseCase
        Notes = $Reason
    }
    Write-CaptureLog "Technical result: $Status - $Reason"
}

function Invoke-PopupHandling {
    param(
        [Parameter(Mandatory)][pscustomobject]$Plan,
        [Parameter(Mandatory)][string]$Session,
        [Parameter(Mandatory)][string]$SnapshotText
    )
    $PopupAction = ''
    if ($SnapshotText -notmatch '(?i)cookie|consent|accept all|reject all|manage cookies|don.t miss|not now|maybe later') {
        return $PopupAction
    }

    $PopupPlan = $Plan.PSObject.Copy()
    $PopupPlan.Area = 'popup'
    $PopupPlan.State = 'visible'
    $PopupPath = New-OutputPath -Plan $PopupPlan -States
    Save-CurrentPage -Plan $PopupPlan -Session $Session -Path $PopupPath -Notes 'Popup or banner was visible before handling.' | Out-Null

    $ButtonNames = @('Accept All', 'Accept all', 'Accept', 'I Accept', 'Agree', 'Allow all', 'Reject All', 'Reject all', 'Not Now', 'Not now', 'Maybe Later', 'Close')
    foreach ($ButtonName in $ButtonNames) {
        if ($SnapshotText -notmatch [regex]::Escape($ButtonName)) {
            continue
        }
        $Click = Invoke-AgentBrowser -Session $Session -Arguments @('find', 'role', 'button', 'click', '--name', $ButtonName)
        if ($Click.ExitCode -eq 0) {
            $PopupAction = $ButtonName
            Invoke-AgentBrowser -Session $Session -Arguments @('wait', '1000') | Out-Null
            Invoke-AgentBrowser -Session $Session -Arguments @('snapshot', '-i', '-c') | Out-Null
            Write-CaptureLog "Popup handled: $ButtonName"
            break
        }
    }
    return $PopupAction
}

function Invoke-StateAction {
    param(
        [Parameter(Mandatory)][pscustomobject]$Plan,
        [Parameter(Mandatory)][string]$Session,
        [Parameter(Mandatory)][string]$SnapshotText
    )
    if (-not $Plan.Action) {
        return [pscustomobject]@{ Success = $true; Reason = ''; Snapshot = $SnapshotText }
    }

    if ($Plan.Action -eq 'require-text') {
        $Read = Invoke-AgentBrowser -Session $Session -Arguments @('read')
        if (($SnapshotText + "`n" + $Read.Output) -notmatch [regex]::Escape($Plan.TargetText)) {
            return [pscustomobject]@{ Success = $false; Reason = "Text '$($Plan.TargetText)' was not displayed."; Snapshot = $SnapshotText }
        }
        return [pscustomobject]@{ Success = $true; Reason = ''; Snapshot = $SnapshotText }
    }

    if ($Plan.Action -eq 'click-text') {
        if ($SnapshotText -notmatch [regex]::Escape($Plan.TargetText)) {
            return [pscustomobject]@{ Success = $false; Reason = "Control '$($Plan.TargetText)' was not displayed."; Snapshot = $SnapshotText }
        }
        $Click = Invoke-AgentBrowser -Session $Session -Arguments @('find', 'text', $Plan.TargetText, 'click', '--exact')
        if ($Click.ExitCode -ne 0) {
            return [pscustomobject]@{ Success = $false; Reason = "Control '$($Plan.TargetText)' could not be activated."; Snapshot = $SnapshotText }
        }
    }
    elseif ($Plan.Action -eq 'mobile-menu') {
        $Clicked = $false
        foreach ($Name in @('Open menu', 'Menu', 'Navigation', 'More')) {
            $Click = Invoke-AgentBrowser -Session $Session -Arguments @('find', 'role', 'button', 'click', '--name', $Name)
            if ($Click.ExitCode -eq 0) {
                $Clicked = $true
                break
            }
        }
        if (-not $Clicked) {
            return [pscustomobject]@{ Success = $false; Reason = 'Mobile navigation control was not found.'; Snapshot = $SnapshotText }
        }
    }
    elseif ($Plan.Action -eq 'bot-start') {
        $Clicked = $false
        foreach ($Name in @('Play', 'Choose', 'Start Game')) {
            if ($SnapshotText -notmatch [regex]::Escape($Name)) {
                continue
            }
            $Click = Invoke-AgentBrowser -Session $Session -Arguments @('find', 'role', 'button', 'click', '--name', $Name)
            if ($Click.ExitCode -eq 0) {
                $Clicked = $true
                break
            }
        }
        if (-not $Clicked) {
            return [pscustomobject]@{ Success = $false; Reason = 'Guest bot start control was not found.'; Snapshot = $SnapshotText }
        }
    }
    elseif ($Plan.Action -eq 'ticket-handoff') {
        $Clicked = $false
        foreach ($Name in @('Explore details', 'Buy now', 'Buy Packages Now', 'Register your interest')) {
            if ($SnapshotText -notmatch [regex]::Escape($Name)) {
                continue
            }
            $Click = Invoke-AgentBrowser -Session $Session -Arguments @('find', 'text', $Name, 'click', '--exact')
            if ($Click.ExitCode -eq 0) {
                $Clicked = $true
                break
            }
        }
        if (-not $Clicked) {
            return [pscustomobject]@{ Success = $false; Reason = 'No public ticket CTA was available for handoff.'; Snapshot = $SnapshotText }
        }
    }

    Invoke-AgentBrowser -Session $Session -Arguments @('wait', '--load', 'domcontentloaded') | Out-Null
    Invoke-AgentBrowser -Session $Session -Arguments @('wait', '--load', 'networkidle') | Out-Null
    Invoke-AgentBrowser -Session $Session -Arguments @('wait', '2000') | Out-Null
    $NewSnapshot = Invoke-AgentBrowser -Session $Session -Arguments @('snapshot', '-i', '-c')
    [pscustomobject]@{ Success = $true; Reason = ''; Snapshot = $NewSnapshot.Output }
}

function Invoke-LazyLoadScroll {
    param(
        [Parameter(Mandatory)][string]$Session
    )
    $HeightResult = Invoke-AgentBrowser -Session $Session -Arguments @('eval', 'document.documentElement.scrollHeight')
    $InitialHeight = 0
    if ($HeightResult.Output -match '(\d+)') {
        $InitialHeight = [int]$Matches[1]
    }
    $Steps = if ($InitialHeight -gt 0) { [Math]::Ceiling($InitialHeight / 1200) } else { 8 }
    $Steps = [Math]::Min([Math]::Max($Steps, 1), 40)
    for ($Index = 0; $Index -lt $Steps; $Index++) {
        Invoke-AgentBrowser -Session $Session -Arguments @('scroll', 'down', '1200') | Out-Null
        Invoke-AgentBrowser -Session $Session -Arguments @('wait', '250') | Out-Null
    }
    $SecondHeightResult = Invoke-AgentBrowser -Session $Session -Arguments @('eval', 'document.documentElement.scrollHeight')
    $SecondHeight = 0
    if ($SecondHeightResult.Output -match '(\d+)') {
        $SecondHeight = [int]$Matches[1]
    }
    if ($SecondHeight -gt $InitialHeight) {
        $ExtraSteps = [Math]::Min([Math]::Ceiling(($SecondHeight - $InitialHeight) / 1200) + 1, 20)
        for ($Index = 0; $Index -lt $ExtraSteps; $Index++) {
            Invoke-AgentBrowser -Session $Session -Arguments @('scroll', 'down', '1200') | Out-Null
            Invoke-AgentBrowser -Session $Session -Arguments @('wait', '250') | Out-Null
        }
    }
    Invoke-AgentBrowser -Session $Session -Arguments @('scroll', 'up', '100000') | Out-Null
    Invoke-AgentBrowser -Session $Session -Arguments @('wait', '2000') | Out-Null
}

function Initialize-Session {
    param(
        [Parameter(Mandatory)][string]$Session,
        [Parameter(Mandatory)][int]$Width,
        [Parameter(Mandatory)][int]$Height
    )
    Invoke-AgentBrowser -Session $Session -Arguments @('close') | Out-Null
    Start-Sleep -Milliseconds 1000
    Invoke-AgentBrowser -Session $Session -Arguments @('open', 'about:blank') | Out-Null
    $Viewport = Invoke-AgentBrowser -Session $Session -Arguments @('set', 'viewport', "$Width", "$Height")
    if ($Viewport.ExitCode -ne 0) {
        throw "Could not set viewport for $Session."
    }
}

function Invoke-CapturePlanItem {
    param(
        [Parameter(Mandatory)][pscustomobject]$Plan
    )
    Start-LogSection -Url $Plan.Url
    Write-CaptureLog "Viewport: $($Plan.Width)x$($Plan.Height), session $($Plan.Session)"
    for ($Attempt = 1; $Attempt -le 3; $Attempt++) {
        Write-CaptureLog "Attempt: $Attempt/3"
        $Open = Invoke-AgentBrowser -Session $Plan.Session -Arguments @('open', $Plan.Url)
        if ($Open.ExitCode -ne 0) {
            Invoke-AgentBrowser -Session $Plan.Session -Arguments @('reload') | Out-Null
            Invoke-AgentBrowser -Session $Plan.Session -Arguments @('wait', '15000') | Out-Null
            continue
        }
        Invoke-AgentBrowser -Session $Plan.Session -Arguments @('wait', '--load', 'domcontentloaded') | Out-Null
        Invoke-AgentBrowser -Session $Plan.Session -Arguments @('wait', '--load', 'networkidle') | Out-Null
        Invoke-AgentBrowser -Session $Plan.Session -Arguments @('wait', '3000') | Out-Null
        $Snapshot = Invoke-AgentBrowser -Session $Plan.Session -Arguments @('snapshot', '-i', '-c')
        $PopupAction = Invoke-PopupHandling -Plan $Plan -Session $Plan.Session -SnapshotText $Snapshot.Output
        if ($PopupAction) {
            $Snapshot = Invoke-AgentBrowser -Session $Plan.Session -Arguments @('snapshot', '-i', '-c')
        }
        $ActionResult = Invoke-StateAction -Plan $Plan -Session $Plan.Session -SnapshotText $Snapshot.Output
        $FinalUrlResult = Invoke-AgentBrowser -Session $Plan.Session -Arguments @('get', 'url')
        $TitleResult = Invoke-AgentBrowser -Session $Plan.Session -Arguments @('get', 'title')
        $AuthenticationState = Get-AuthenticationState -FinalUrl $FinalUrlResult.Output -PageText $ActionResult.Snapshot
        $BlockedReason = Get-BlockedReason -Text ($Snapshot.Output + "`n" + $ActionResult.Snapshot)
        if ($BlockedReason) {
            $FailedPath = New-OutputPath -Plan $Plan -Failed
            $FailureCapture = Save-CurrentPage -Plan $Plan -Session $Plan.Session -Path $FailedPath -PopupAction $PopupAction -Notes $BlockedReason -ForcedStatus 'BLOCKED'
            if (-not $FailureCapture.Success) {
                Add-MissingState -Plan $Plan -Reason $BlockedReason -FinalUrl $FinalUrlResult.Output -Title $TitleResult.Output -AuthenticationState $AuthenticationState -Status 'BLOCKED'
            }
            return
        }
        if (-not $ActionResult.Success) {
            Add-MissingState -Plan $Plan -Reason $ActionResult.Reason -FinalUrl $FinalUrlResult.Output -Title $TitleResult.Output -AuthenticationState $AuthenticationState
            return
        }
        if ($Plan.RequiresAuth -and $AuthenticationState -eq 'LoginRequired') {
            $FailedPath = New-OutputPath -Plan $Plan -Failed
            $FailureCapture = Save-CurrentPage -Plan $Plan -Session $Plan.Session -Path $FailedPath -PopupAction $PopupAction -Notes 'Login was required.' -ForcedStatus 'BLOCKED'
            if (-not $FailureCapture.Success) {
                Add-MissingState -Plan $Plan -Reason 'Login was required.' -FinalUrl $FinalUrlResult.Output -Title $TitleResult.Output -AuthenticationState $AuthenticationState -Status 'BLOCKED'
            }
            return
        }
        Invoke-LazyLoadScroll -Session $Plan.Session
        $OutputPath = New-OutputPath -Plan $Plan
        $Saved = Save-CurrentPage -Plan $Plan -Session $Plan.Session -Path $OutputPath -PopupAction $PopupAction -Notes $Plan.Notes
        if ($Saved.Success) {
            return
        }
        Write-CaptureLog "Network or screenshot error: $($Saved.Reason)"
        Invoke-AgentBrowser -Session $Plan.Session -Arguments @('reload') | Out-Null
        Invoke-AgentBrowser -Session $Plan.Session -Arguments @('wait', '--load', 'networkidle') | Out-Null
        Invoke-AgentBrowser -Session $Plan.Session -Arguments @('wait', '15000') | Out-Null
    }

    $FinalUrlResult = Invoke-AgentBrowser -Session $Plan.Session -Arguments @('get', 'url')
    $TitleResult = Invoke-AgentBrowser -Session $Plan.Session -Arguments @('get', 'title')
    $FailedPath = New-OutputPath -Plan $Plan -Failed
    $FailureShot = Invoke-AgentBrowser -Session $Plan.Session -Arguments @('screenshot', $FailedPath, '--full')
    if ($FailureShot.ExitCode -eq 0 -and (Test-Path -LiteralPath $FailedPath)) {
        $Info = Get-ImageInfo -Path $FailedPath
        Add-ManifestRow -Values @{
            Product = $Plan.Product
            Viewport = $Plan.Viewport
            PageArea = $Plan.Area
            State = $Plan.State
            SourceUrl = $Plan.Url
            FinalUrl = $FinalUrlResult.Output
            PageTitle = $TitleResult.Output
            Filename = [System.IO.Path]::GetFileName($FailedPath)
            AbsolutePath = $FailedPath
            CapturedAt = Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz'
            Width = $Info.Width
            Height = $Info.Height
            Bytes = $Info.Bytes
            PopupAction = ''
            AuthenticationState = Get-AuthenticationState -FinalUrl $FinalUrlResult.Output -PageText ''
            Status = 'FAILED'
            FailureReason = 'Capture failed after three attempts.'
            RelatedFigure = $Plan.RelatedFigure
            RelatedUseCase = $Plan.RelatedUseCase
            Notes = 'Error state was captured after three attempts.'
        }
        Write-CaptureLog "File output: $FailedPath"
    }
    else {
        Add-MissingState -Plan $Plan -Reason 'Capture failed after three attempts and no error screenshot was created.' -FinalUrl $FinalUrlResult.Output -Title $TitleResult.Output -Status 'FAILED'
    }
}

function New-Plan {
    param(
        [string]$Product,
        [string]$Viewport,
        [string]$Area,
        [string]$State,
        [string]$Url,
        [string]$Figure,
        [string]$UseCase,
        [string]$Action = '',
        [string]$TargetText = '',
        [bool]$ExpectScrollable = $true,
        [bool]$RequiresAuth = $false,
        [string]$Notes = ''
    )
    $IsMobile = $Viewport -eq 'mobile'
    [pscustomobject]@{
        Product = $Product
        Viewport = $Viewport
        Area = $Area
        State = $State
        Url = $Url
        RelatedFigure = $Figure
        RelatedUseCase = $UseCase
        Action = $Action
        TargetText = $TargetText
        ExpectScrollable = $ExpectScrollable
        RequiresAuth = $RequiresAuth
        Notes = $Notes
        Width = if ($IsMobile) { 390 } else { 1440 }
        Height = if ($IsMobile) { 844 } else { 1000 }
        Session = if ($Product -eq 'fifa') {
            if ($IsMobile) { 'pa2-fifa-mobile' } else { 'pa2-fifa-desktop' }
        }
        else {
            if ($IsMobile) { 'pa2-chess-mobile' } else { 'pa2-chess-desktop' }
        }
    }
}

$Plans = @(
    (New-Plan fifa desktop home default 'https://www.fifa.com/en' 'F-01; F-02; F-09B' 'F-UC1; F-UC3; F-UC4' -Notes 'Full-page capture includes the page header and footer.'),
    (New-Plan fifa mobile home default 'https://www.fifa.com/en' 'F-08; F-08A' 'F-UC1; F-UC2; F-UC3'),
    (New-Plan fifa mobile navigation open 'https://www.fifa.com/en' 'F-03' 'F-UC1; F-UC3; F-UC4' 'mobile-menu'),
    (New-Plan fifa desktop match-centre default 'https://www.fifa.com/en/match-centre' 'F-04' 'F-UC1; F-UC2'),
    (New-Plan fifa desktop match-centre today 'https://www.fifa.com/en/match-centre' 'F-04' 'F-UC1; F-UC2' 'click-text' 'Today'),
    (New-Plan fifa desktop match-centre live 'https://www.fifa.com/en/match-centre' 'F-04' 'F-UC2' 'click-text' 'Live'),
    (New-Plan fifa desktop match-centre results 'https://www.fifa.com/en/match-centre' 'F-04' 'F-UC2' 'click-text' 'Results'),
    (New-Plan fifa mobile match-centre default 'https://www.fifa.com/en/match-centre' 'F-04M' 'F-UC1; F-UC2'),
    (New-Plan fifa desktop search mixed-results 'https://www.fifa.com/en/search?q=world+cup' 'F-05' 'F-UC5'),
    (New-Plan fifa desktop article default 'https://inside.fifa.com/tournament-organisation/commercial/media-releases/world-cup-26-ticketing-programme-launch-september' 'F-06' 'F-UC3'),
    (New-Plan fifa mobile article default 'https://inside.fifa.com/tournament-organisation/commercial/media-releases/world-cup-26-ticketing-programme-launch-september' 'F-06M' 'F-UC3'),
    (New-Plan fifa desktop tournament default 'https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026' 'F-07' 'F-UC4'),
    (New-Plan fifa desktop tournament subnavigation 'https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026' 'F-07' 'F-UC4' 'require-text' 'Matches'),
    (New-Plan fifa desktop rankings default 'https://inside.fifa.com/fifa-world-ranking/men' '' 'F-UC4'),
    (New-Plan fifa desktop tickets default 'https://www.fifa.com/en/tickets' '' 'F-UC4'),
    (New-Plan fifa mobile tickets default 'https://www.fifa.com/en/tickets' '' 'F-UC4'),
    (New-Plan fifa desktop tickets explore-details 'https://www.fifa.com/en/tickets' '' 'F-UC4' 'require-text' 'Explore details'),
    (New-Plan fifa desktop tickets buy-now 'https://www.fifa.com/en/tickets' '' 'F-UC4' 'require-text' 'Buy now'),
    (New-Plan fifa desktop tickets buy-packages-now 'https://www.fifa.com/en/tickets' '' 'F-UC4' 'require-text' 'Buy Packages Now'),
    (New-Plan fifa desktop tickets register-interest 'https://www.fifa.com/en/tickets' '' 'F-UC4' 'require-text' 'Register your interest'),
    (New-Plan fifa desktop tickets coming-soon 'https://www.fifa.com/en/tickets' '' 'F-UC4' 'require-text' 'Coming soon'),
    (New-Plan fifa desktop tickets sold-out 'https://www.fifa.com/en/tickets' '' 'F-UC4' 'require-text' 'Sold out'),
    (New-Plan fifa desktop tickets waiting-room 'https://www.fifa.com/en/tickets' '' 'F-UC4' 'require-text' 'Waiting room'),
    (New-Plan fifa desktop tickets resale 'https://www.fifa.com/en/tickets' '' 'F-UC4' 'require-text' 'Resale'),
    (New-Plan fifa desktop tickets pre-partner-handoff 'https://www.fifa.com/en/tickets' '' 'F-UC4'),
    (New-Plan fifa desktop tickets partner-handoff 'https://www.fifa.com/en/tickets' '' 'F-UC4' 'ticket-handoff'),
    (New-Plan fifa desktop fifa-plus entry 'https://www.fifa.com/en/fifa-plus' 'F-10B' 'F-UC3'),
    (New-Plan fifa mobile fifa-plus entry 'https://www.fifa.com/en/fifa-plus' 'F-10B' 'F-UC3'),
    (New-Plan fifa desktop fifa-plus content-rails 'https://www.plus.fifa.com/' 'F-10B' 'F-UC3' -Notes 'Full-page capture records the public FIFA+ landing surface and visible media rails.'),
    (New-Plan fifa desktop dazn landing 'https://www.dazn.com/en-VN/competition/Competition:50kvbmxi5r9amj2e39hznggqj' 'F-10B' 'F-UC3'),
    (New-Plan fifa mobile dazn landing 'https://www.dazn.com/en-VN/competition/Competition:50kvbmxi5r9amj2e39hznggqj' 'F-10B' 'F-UC3'),
    (New-Plan fifa desktop stories default 'https://inside.fifa.com/all-stories' '' 'F-UC3; F-UC5'),
    (New-Plan fifa desktop tournament-blog default 'https://inside.fifa.com/blogs/fwc-2026' '' 'F-UC3; F-UC4'),
    (New-Plan fifa desktop store default 'https://store.fifa.com/' 'F-09B' 'F-UC4'),
    (New-Plan fifa desktop collect default 'https://collect.fifa.com/' 'F-09B' 'F-UC4'),
    (New-Plan fifa desktop rewards default 'https://www.fifa.com/en/rewards' 'F-09B' 'F-UC4'),
    (New-Plan chess desktop home-navigation default 'https://www.chess.com/' 'C-01; C-06' 'C-UC1; C-UC2; C-UC3; C-UC5'),
    (New-Plan chess mobile home default 'https://www.chess.com/' 'C-08' 'C-UC1; C-UC2; C-UC3; C-UC5'),
    (New-Plan chess mobile navigation open 'https://www.chess.com/' 'C-06M' 'C-UC1; C-UC2; C-UC3; C-UC5' 'mobile-menu'),
    (New-Plan chess desktop play start-game 'https://www.chess.com/play/online' 'C-02' 'C-UC1'),
    (New-Plan chess desktop play time-control-selection 'https://www.chess.com/play/online' 'C-02' 'C-UC1' 'click-text' '10 min'),
    (New-Plan chess mobile play start-game 'https://www.chess.com/play/online' 'C-02M' 'C-UC1'),
    (New-Plan chess desktop bot-board default 'https://www.chess.com/play/computer' 'C-03' 'C-UC1; C-UC4'),
    (New-Plan chess desktop bot-board active-game 'https://www.chess.com/play/computer' 'C-03; C-07' 'C-UC1' 'bot-start'),
    (New-Plan chess mobile bot-board active-game 'https://www.chess.com/play/computer' 'C-03; C-07' 'C-UC1' 'bot-start'),
    (New-Plan chess desktop puzzle before-move 'https://www.chess.com/puzzles' 'C-04; C-04A' 'C-UC2'),
    (New-Plan chess mobile puzzle before-move 'https://www.chess.com/puzzles' 'C-04M' 'C-UC2'),
    (New-Plan chess desktop lessons cards-loaded 'https://www.chess.com/lessons' 'C-05' 'C-UC3'),
    (New-Plan chess mobile lessons cards-loaded 'https://www.chess.com/lessons' 'C-05' 'C-UC3'),
    (New-Plan chess desktop study-plan default 'https://www.chess.com/article/view/study-plan-directory' '' 'C-UC3; C-UC5'),
    (New-Plan chess desktop analysis default 'https://www.chess.com/analysis' '' 'C-UC4'),
    (New-Plan chess desktop game-review entry 'https://www.chess.com/analysis/game/live' '' 'C-UC4' -RequiresAuth $true),
    (New-Plan chess desktop account-prompt default 'https://www.chess.com/login' 'C-10B' 'C-UC1; C-UC4' -ExpectScrollable $false)
)

Initialize-Session -Session 'pa2-fifa-desktop' -Width 1440 -Height 1000
Initialize-Session -Session 'pa2-fifa-mobile' -Width 390 -Height 844
Initialize-Session -Session 'pa2-chess-desktop' -Width 1440 -Height 1000
Initialize-Session -Session 'pa2-chess-mobile' -Width 390 -Height 844

foreach ($Plan in $Plans) {
    try {
        Invoke-CapturePlanItem -Plan $Plan
    }
    catch {
        Start-LogSection -Url $Plan.Url
        Write-CaptureLog "Error: $($_.Exception.Message)"
        Add-MissingState -Plan $Plan -Reason $_.Exception.Message -Status 'FAILED'
    }
}

foreach ($Session in @('pa2-fifa-desktop', 'pa2-fifa-mobile', 'pa2-chess-desktop', 'pa2-chess-mobile')) {
    Invoke-AgentBrowser -Session $Session -Arguments @('close') | Out-Null
}

Write-Output "Capture plan complete. Manifest: $ManifestPath"
