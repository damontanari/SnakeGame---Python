import cx_Freeze

executables = [cx_Freeze.Executable('snake_Game.py')]

cx_Freeze.setup(
    name="Snake Game",
    options={'build_exe': {'packages':['pygame'],
                            'include_files':['\misc']}},
    executables = executables
                            
)