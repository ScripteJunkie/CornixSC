#SingleInstance, Force

VisibleToggle := 1
CollectCoords := 0

gui, add, button,w180 vGetCoordsStart gGetCoordsStart, Start
gui, add, button,w180 vGetCoordsStop gGetCoordsStop Hidden, Stop
gui, show

Return


GetCoordsStart:

	If VisibleToggle = 1     
	{
		GuiControlShowHide("GetCoordsStart","hide")
		GuiControlShowHide("GetCoordsStop","show")                                          
		VisibleToggle = 0
		CollectCoords = 1
	}

	While CollectCoords = 1
	{
		WinWaitActive, Star Citizen
		Sleep, 10000
		BlockInput, On
		Sleep, 10
		Send {enter}
		Sleep, 100
		SendRaw /showlocation
		Sleep, 100
		Send {enter}
		Sleep, 10
		BlockInput Off
	}
	
Return


GetCoordsStop:

	If VisibleToggle = 0
	{
		GuiControlShowHide("GetCoordsStop","hide")  
		GuiControlShowHide("GetCoordsStart","show")                                          
		VisibleToggle = 1
		CollectCoords = 0
	}

Return

;-------------------------------------------------------------

GuiControlShowHide(controls,showhide="Hide"){

           Loop,Parse,controls,|

           GuiControl, %showhide%,%A_LoopField%

}

;-------------------------------------------------------------

esc::exitApp ; <- press escape to exit

GuiClose:
ExitApp
