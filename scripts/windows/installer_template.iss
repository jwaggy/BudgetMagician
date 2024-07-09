[Setup]
AppId={{33ECFE77-75E2-422E-8892-40CC7E59F124}
AppName={app_display_name}
AppVersion={app_version}
AppVerName={app_name}
AppPublisher={app_author}
AppPublisherURL={app_url}
WizardStyle=modern
DefaultDirName={autopf}\{app_name}
DefaultGroupName={app_display_name}
UninstallDisplayIcon={app}\{app_name}.exe
Compression=lzma2
LZMAUseSeparateProcess=yes
SolidCompression=yes
ShowLanguageDialog=no
VersionInfoVersion={app_version}
VersionInfoCompany={app_author}
VersionInfoCopyright=(c) 2024 {app_author}
VersionInfoProductName={app_display_name}
VersionInfoProductVersion={app_version}
ArchitecturesAllowed=x64
ArchitecturesInstallIn64BitMode=x64
SourceDir={app_source}

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"

[Files]
Source: "*"; DestDir: "{app}"; Flags: recursesubdirs;

[Icons]
Name: "{group}\{app_display_name}"; Filename: "{app}\{app_name}.exe"
Name: "{group}\{cm:UninstallProgram,{app_name}}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\{app_display_name}"; Filename: "{app}\{app_name}.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\{app_name}.exe"; Flags: nowait postinstall skipifsilent 64bit; Description: "{cm:LaunchProgram,{app_name}}"

[Registry]
Root: HKCR; SubKey: "Local Settings\Software\Microsoft\Windows\Shell\MuiCache"; ValueType: string; ValueName: "{app}\{app_name}.exe.FriendlyAppName"; ValueData: "{app_display_name}"; Flags: uninsdeletevalue
Root: HKCR; SubKey: "Local Settings\Software\Microsoft\Windows\Shell\MuiCache"; ValueType: string; ValueName: "{app}\{app_name}.exe.ApplicationCompany"; ValueData: "{app_author}"; Flags: uninsdeletevalue
