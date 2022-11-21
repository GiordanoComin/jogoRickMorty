<<<<<<< HEAD
import cx_Freeze

executables = [cx_Freeze.Executable(
    script="rickMorty.py",
    icon="assets/iconeRick.ico"
)]
cx_Freeze.setup(
    name="Rick And Morty",
    options={
        "build_exe":{"packages":["pygame"],
        "include_files":["assets"]
        }}
    ,executables = executables
)

=======
import cx_Freeze

executables = [cx_Freeze.Executable(
    script="rickMorty.py",
    icon="assets/iconeRick.ico"
)]
cx_Freeze.setup(
    name="Rick And Morty",
    options={
        "build_exe":{"packages":["pygame"],
        "include_files":["assets"]
        }}
    ,executables = executables
)

>>>>>>> b7a35787c960f8f18971929cbf8a1715c1988794
