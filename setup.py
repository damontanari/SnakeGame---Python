import cx_Freeze

executables = [cx_Freeze.Executable('C:\Users\dsm_m\Desktop\Scripts - Planilhas\Scripts Python\Py Games\snake_Game.py')]

cx_Freeze.setup(
    name="Snake Game",
    options={'build_exe': {'packages':['pygame'],
                            'include_files':['C:\Users\dsm_m\Desktop\Scripts - Planilhas\Scripts Python\Py Games\misc']}},
    executables = executables
                            
)