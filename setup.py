from cx_Freeze import setup, Executable

setup(name="Secret Santa Checker", version = "1.0", description = "A Tool to Decode and Reveal your secret santa", executables = [Executable("User-Access.py")])
