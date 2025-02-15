import os

APP_NAME = "{app_name}"
SRC_DIR = os.path.abspath("./{app_module}")
BUILD_DIR = os.path.abspath("./build")
MIGRATIONS_DIR = os.path.join(os.path.dirname(BUILD_DIR), "migrations")

a = Analysis(
    [os.path.join(SRC_DIR, "main.py")],
    pathex=[],
    binaries=[],
    datas=[(MIGRATIONS_DIR, "migrations")],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=APP_NAME,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    version=os.path.join(BUILD_DIR, "version_info.py"),
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name=APP_NAME,
)
