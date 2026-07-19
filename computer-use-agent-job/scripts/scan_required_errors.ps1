param(
  [string]$TitleContains = "",
  [string]$Pattern = "必填项未填写"
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

for ($i = 0; $i -lt $items.Count; $i++) {
  $el = $items.Item($i)
  if ($el.Current.Name -like "*$Pattern*") {
    $rect = $el.Current.BoundingRectangle
    [PSCustomObject]@{
      Index = $i
      Text = $el.Current.Name
      X = [int]$rect.X
      Y = [int]$rect.Y
      W = [int]$rect.Width
      H = [int]$rect.Height
    }
  }
}
