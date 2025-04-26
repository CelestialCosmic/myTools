import os
while True:
    try:
        os.remove("C:/Users/sirius/Desktop/xCon$.prgd")
    except FileNotFoundError:
        pass
    except PermissionError:
        pass