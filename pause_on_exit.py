import sys

def pause_on_exit(message="Program finished. Close this dialog or click OK to exit."):
    """Try to show a Windows MessageBox so the user must click OK/X to dismiss.

    Falls back to a console "press Enter to exit" prompt if GUI isn't available.
    """
    try:
        # Use ctypes to call MessageBoxW on Windows. This will force the user
        # to click the dialog's button (or the window's X) to continue.
        import ctypes
        MB_OK = 0x00000000
        ctypes.windll.user32.MessageBoxW(0, message, "Finished", MB_OK)
    except Exception:
        try:
            input("\nProgram finished. Press Enter to exit...")
        except Exception:
            # If even input() fails, silently continue
            pass
