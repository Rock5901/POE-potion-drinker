#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
#SingleInstance Force


MsgBox, 4, Installer, Would you like to install required modules? (press Yes or No)?
IfMsgBox Yes 
{
	Run, cmd.exe /c pip install Pillow
	Run, cmd.exe /c pip install pyautoit
	Run, cmd.exe /c pip install keyboard
	Run, cmd.exe /c pip install mouse
	Run, cmd.exe /c pip install pywin32
	Run, cmd.exe /c pip install threading
}
