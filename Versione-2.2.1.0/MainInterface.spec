# -*- mode: python -*-

block_cipher = None


a = Analysis(['MainInterface.py'],
             pathex=['C:\\Users\\Juri Francia\\Dropbox\\10. Control Room\\10. [TM] Training Material\\JaSONx\\Sorgenti JaSONx\\JaSONx v.2.2.1'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='MainInterface',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='C:\\Users\\Juri Francia\\Dropbox\\10. Control Room\\10. [TM] Training Material\\JaSONx\\Sorgenti JaSONx\\JaSONx v.2.2.1\\image\\logo_ico.ico')
