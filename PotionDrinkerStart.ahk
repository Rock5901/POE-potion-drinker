#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
#SingleInstance Force

Run, python.exe PotionDrinker.py

FileRead, Msgboxblocker, Msgboxblocker.txt
if (Msgboxblocker = 1) {
	return
} else {
	MsgBox, 4100, ,
	(Ltrim 
		Press UP-ARROW to pause. Press DOWN-ARROW to exit script. 
		STARTS PAUSED
		
		Press YES to hide this messagebox forever. Press NO to see it at next launch.
	)
	IfMsgBox Yes
		FileAppend, 1, Msgboxblocker.txt
}