# Pylodica
A Python library for for creating music algorithmically

## WIP
### Enabling Sound support in WSL2
Right now, WSL2 does not support playing audio but this may not be necessary later on down the line as WSL2 receives more features.

This workaround is based on [this article](https://x410.dev/cookbook/wsl/enabling-sound-in-wsl-ubuntu-let-it-sing/), as well as [comments on this issue](https://github.com/microsoft/WSL/issues/4205#issuecomment-555303157).  
It assumes you already have [WSL2 as well as your preferred linux distribution installed](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

1. Download PulseAudio binaries built for Windows by the OpenSUSE BuildService. It should come in a zipfile.  [https://www.freedesktop.org/wiki/Software/PulseAudio/Ports/Windows/Support/](https://www.freedesktop.org/wiki/Software/PulseAudio/Ports/Windows/Support/).
2. Unzip the folder and place it in your directory of choice.  
For example, you could create a folder at `C:\wsl` such that the binaries are located in `C:\wsl\pulseaudio-1.1`  
3. Modify the following files wiithin the binary folder:  
    * `etc\pulse\default.pa`  
        * *line 42*  
            This disables recording audio via PulseAudio as WSL2 restricts access to recording devices.  
            Replace
            > `load-module module-waveout sink_name=output source_name=input`  

            With  
            > `load-module module-waveout sink_name=output source_name=input record=0`

        * *line 61*  
            This sets the  PulseAudio server to accept anonymous connections from `127.0.0.1` via TCP.  
            Replace  
            > `#load-module module-native-protocol-tcp`  

            With
            > `load-module module-native-protocol-tcp auth-ip-acl=127.0.0.1 auth-anonymous=1`

    * `etc\pulse\daemon.conf`  
        * *line 39*  
            The value of this variable is how many seconds to wait before the PulseAudio server kills itself after the last client disconnects. Setting this variable to a negative number keeps the PulseAudio server running.  
            Replace  
            > `; exit-idle-time = 20` 

            With
            > `exit-idle-time = -1`  

4. Run 'bin\pulseaudio.exe' via powershell to check that you've made the changes correctly.  
    You might see the following shell output:
    ```powershell
    PS C:\wsl\pulseaudio-1.1\bin> .\pulseaudio.exe
    W: [(null)] pulsecore/core-util.c: Secure directory creation not supported on Win32.
    W: [(null)] pulsecore/core-util.c: Secure directory creation not supported on Win32.
    W: [(null)] pulsecore/core-util.c: Secure directory creation not supported on Win32.
    W: [(null)] pulsecore/core.c: failed to allocate shared memory pool. Falling back to a normal memory pool.
    W: [(null)] pulsecore/core-util.c: Secure directory creation not supported on Win32.
    W: [(null)] pulsecore/core-util.c: Secure directory creation not supported on Win32.
    W: [(null)] pulsecore/core-util.c: Secure directory creation not supported on Win32.
    E: [(null)] daemon/main.c: Failed to load directory.
    W: [(null)] pulsecore/core-util.c: Secure directory creation not supported on Win32.
    ```
    > If there's an error, the server should exit immediately, in which case you might have to go back to step 3 and make sure you made the changes correctly. If you've made the changes and the server still fails to run, then this workaround is broken. 😔

    Press `ctrl+c` with the shell in focus to stop the server

5. Ensure the PulseAudio server runs whenever we run linux via WSL2.
    This can be achieved in a number of ways, depending on how you'd normally launch linux/WSL2.

    * Create a batch file that you'll use to run linux that also starts the pulseaudio server 
        `C:\wsl\start_with_pulse.bat`
        ```powershell
        start "" /B "C:\<path>\<to>\<pulseaudio>\pulseaudio.exe"
        <distro_executable>.exe run "export PULSE_SERVER=tcp:127.0.0.1; pkill '(gpg|ssh)-agent'; taskkill.exe /IM pulseaudio.exe /F; fi;"
        ```

        Filled with proper filepaths it might look like.
        ```powershell
        start "" /B "C:\wsl\pulseaudio\bin\pulseaudio.exe"
        ubuntu.exe run "export PULSE_SERVER=tcp:127.0.0.1; pkill '(gpg|ssh)-agent'; taskkill.exe /IM pulseaudio.exe /F; fi;"
        ```
        You'd then run this batch file to run WSL2.

        ---

        If you're already using another batch file to launch linux, for example to [launch X410 and Xfce](https://x410.dev/cookbook/wsl/customizing-xfce-desktop-for-ubuntu-wsl/), the key commands to add to your batch file are
        * `start "" /B "C:\<path>\<to>\<pulseaudio>\pulseaudio.exe"`
        * `export PULSE_SERVER=tcp:127.0.0.1;`
        * `taskkill.exe /IM pulseaudio.exe /F;` after `pkill '(gpg|ssh)-agent';`

6. Run your linux instance and install PulseAudio if you haven't already.  
    On ubuntu, this is achieved by running  
    ```bash
    sudo apt-get update && apt-get install pulseaudio
    ```

7. Get your WSL's ip with this command for ubuntu `ifconfig eth0 | grep 'inet '`  
this should print several ip addresses like so:  
`inet 172.20.152.100  netmask 255.255.240.0  broadcast 172.20.159.255`
* Hello
> Something
