# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['automate_UCLsport.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['selenium', 'selenium.webdriver.firefox.service', 'selenium.webdriver.firefox.options', 'selenium.webdriver.common.by', 'selenium.webdriver.support.ui', 'selenium.webdriver.support', 'cv2', 'os', 're', 'time', 'sys', 'datetime', 'ffpyplayer.player'],
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
    a.binaries,
    a.datas,
    [],
    name='automate_UCLsport',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
