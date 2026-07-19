param(
  [string]$TitleContains = "",
  [int]$MaxItems = 200
)

Add-Type -AssemblyName UIAutomationClient
Add-Type -AssemblyName UIAutomationTypes

$root = [System.Windows.Automation.AutomationElement]::RootElement
$windows = $root.FindAll(
  [System.Windows.Automation.TreeScope]::Children,
  [System.Windows.Automation.Condition]::TrueCondition
) | Where-Object {
  $_.Current.ClassName -eq "Chrome_WidgetWin_1" -and
  ($TitleContains -eq "" -or $_.Current.Name -like "*$TitleContains*")
}

if (-not $windows -or $windows.Count -eq 0) {
  Write-Error "No Chrome window matched TitleContains='$TitleContains'."
  exit 1
}

$win = $windows | Select-Object -First 1
$items = $win.FindAll(
  [System.Windows.Automation.TreeScope]::Descendants,
  [System.Windows.Automation.Condition]::TrueCondition
)

$count = [Math]::Min($items.Count, $MaxItems)
for ($i = 0; $i -lt $count; $i++) {
  $el = $items.Item($i)
  $rect = $el.Current.BoundingRectangle
  [PSCustomObject]@{
    Index = $i
    ControlType = $el.Current.ControlType.ProgrammaticName
    Name = $el.Current.Name
    ClassName = $el.Current.ClassName
    X = [int]$rect.X
    Y = [int]$rect.Y
    W = [int]$rect.Width
    H = [int]$rect.Height
  }
}
