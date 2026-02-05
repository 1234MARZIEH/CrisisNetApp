; -- Example1.iss --
; Demonstrates copying 3 files and creating an icon.

; SEE THE DOCUMENTATION FOR DETAILS ON CREATING .ISS SCRIPT FILES!

[Setup]
AppName=CrisisNet
AppVersion=1.0
DefaultDirName={autopf}\CrisisNet
DefaultGroupName=CrisisNet
OutputDir=installer
OutputBaseFileName=CrisisNetSetup
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\CrisisNet.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\CrisisNet"; Filename: "{app}\CrisisNet.exe"
Name: "{commondesktop}\CrisisNet"; Filename: "{app}\CrisisNet.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a desktop icon"; Flags: unchecked