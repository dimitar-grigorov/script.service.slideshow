import xbmc
import os.path
import subprocess

# import xbmcgui

# Path to script to be executed on Kodi/Service start
SCRIPT_PATH = 'D:\empty.bat'

if __name__ == '__main__':
    xbmc.log("Slideshow Service Started", level=xbmc.LOGNOTICE)

    # If file exists
    if os.path.isfile(SCRIPT_PATH):
        subprocess.call([SCRIPT_PATH])
        #xbmc.executebuiltin('SlideShow(D:\Pictures, recursive)')
    else:
        # Start Screensaver
        xbmc.executebuiltin('ESC')
        xbmc.executebuiltin('ActivateScreensaver')

    # TODO: To check if slideshow is still running
    monitor = xbmc.Monitor()
    while not monitor.abortRequested():
        # Sleep/wait for abort for 10 seconds
        if monitor.waitForAbort(10):
            xbmc.log("Slideshow Service Stopped", level=xbmc.LOGNOTICE)
            # Abort was requested while waiting. We should exit
            break
