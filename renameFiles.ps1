# Powershell snippet to rename all files in a folder.

$path = ".\"
$files = Get-ChildItem -Path $path
Foreach ($file in $files) {
	$random = Get-Random
	$file | Rename-Item -NewName {"$Random" + $_.extension}
}
