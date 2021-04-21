HOW TO USE THIS TOOL:
I'm sharing the full source code files, to change something if you want to, but you can use the .exe file
The executable file and the .txt you need are in pythonproject/dist
1. Copy the files to the directory you need
2. Open the ftps.txt file, and copy the ftp users and password in this format:
    user:password 
you will only need this, in the file ftps.txt you can find a lot of examples.
4. Once you finished to complete your ftps.txt, you can open the FTPdownloaderEN.exe file
5. Wait until the download is finished.

HOW THIS TOOL WORKS?
This tool is written in Python 3.8
It's simple, the script use the ftps.txt you provide to get the full link to acces, for an example: ftp://user:password@alfalaval.com/
when it opens the link, the script try to check what is a directory and what is a file, if is a directory, it creates a new directory on your folder, or if was a file, download the file.
If for some reasons the script show errors to download or enter in a specified url, you have 2 logs you can access to verify the problems: log.txt and cantdownload.txt
log.txt shows all urls the script was having trouble to access, and the cantdownload.txt shows all files the script cant download for some reason.
**THIS ONLY WORKS IN THE FTP ALFALAVAL**
