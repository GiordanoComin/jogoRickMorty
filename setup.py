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

