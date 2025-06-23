# CDJ-File-Cleaner
The cdj-file-cleaner was a script that I got ChatGPT 3.5 to develop for me to make ease of batch converting lossless files that have questionable integrity into files that will 100% of the time work with CDJs.

## Note
As of reuploading, this script hasn't been touched once, so things may have broken. I intend to eventually update this with features such as automatic metadata conversion, but this may not happen. 

## Installation
1. Download and Install Python:
    Ensure Python is installed from python.org
    Make sure to check "Add Python to PATH" during installation.
2. Install FFmpeg:
    Download and install FFmpeg from ffmpeg.org.
    Extract the ZIP file and add the bin directory to the system PATH.
*** For help with installing FFmpeg, scroll to the bottom for a detailed tutorial ***
3. Install Dependencies:
    Open Command Prompt.
    Navigate to the AudioConverter directory. (type cd followed by the path to the directory, mine is as followed: cd C:\Users\Ethan\Documents\flac and shitty wav to epic CDJWAV)
    Run the following command to install the required Python libraries: 
    `pip install -r requirements.txt`

## How to run
- Open command prompt (click start button and type cmd)
- Enter the following: cd C:\Users\Ethan\Documents\flac and shitty wav to epic CDJWAV
	Note you will have to change the directory to the place you unzipped the folder
	to. Make sure it ends with "flac and shitty wav to epic CDJWAV".
- Enter the following: python Batch_Convert_to_WAV_16_1440.py
- Wait for the program to run through. It will say "Press any key to close" once it is finished.

## FFmpeg Installation
1. Locate the bin Directory Path:
	The path you need to add will look something like C:\ffmpeg\bin. This is the directory where the FFmpeg executables are located.
2. Add the bin Directory to the System PATH:
	Press Win + R to open the Run dialog.
	Type sysdm.cpl and press Enter. This opens the System Properties window.
	In the System Properties window, go to the "Advanced" tab and click on "Environment Variables" at the bottom.
	In the Environment Variables window, under the "System variables" section, scroll and find the variable named Path. Select it and click "Edit...".
	In the Edit Environment Variable window, click "New" and then enter the path to the bin directory, e.g., C:\ffmpeg\bin.
	Click "OK" to close the windows.
3. Verify the PATH Addition:
	Open a new Command Prompt window.
	Type ffmpeg -version and press Enter.
	If the PATH was set correctly, you should see the version information for FFmpeg.


This is a Warpath sanctioned script. Support us at @warpathpromotions on instagram,
or if you are looking for advice with the script, hit up the creator @arekatera__ on instagram   .
                                                                                                
                                                                      
                                                   &     @ @                                        
                                            @ @@@@  @@  @ @ @@    @                                 
                                     @%@@@@  @@.@@@ @@ @ @@@@ @                                     
                           @ @   @  @@@@* @ @ @ . ./ @  @@@@ @  @    @ @                            
                           @ @,@@ @ @, @@ @ @ @  @ @ @ @@ @@  @@ @@@@ @@ @@                         
                       @@ @ @ @@/ @@@   @  @@ (  @     ,  @@ @@@ @    @&@@@                         
                    ( @ @@ @  @ @@@   @ @  @ @.      @   @& @ @@ @  @  @ @ @                        
                    @,@@ @ @ % @@     @ @@ @ @  % @  @ @@ @ @       (  @ @ @                        
                     @@@ # @           @ @ @ @@ @   @ @@   ( @     @ @@ @@                          
                   @ @@@             , @@ @@@  @@@                @ @ @@@ @@@                       
                   @@ @        @@& @ @@ @    . &%             % @@   @@ @,  @                       
                 @@@    @ @    @      @          @                & @    @@ @                       
                 .@@.     ,       %                                     %   @@                      
                   @   @  @ /@@@ @ @                  @@@@@            @   ( @@                     
                  @    @                                                   @@ #                     
                 @          @@@@@@@ @             @         .@@@@@@@        @ @                     
                ,    @@     @      @    @@           @@     @    @           @    /                 
                    @ @             @@@     @  @         @ @                 @@@,&                  
                @  @ @  @ @     /@         @ @ @  @   (       @@@@@@@@@    @  @*@@                  
                  /                   @  @@ @       @ @@     @  @         @   @ @                   
               @ @/ / @  @ %  @ @  @@@ @      @@@@  # @ @@@  @ @@            @@ @                   
               @ @ &  @  @ @@ @    @ @    @        @@   @@@  @ @@ @@   @   @ @@                     
                   .@       @ @    @  @  @           @ @@ @  @  @ *@ @ @ @ @@ @@                    
                 @@@  @  @             @              @ @       @  @ @ @      @                     
                /@   @@ @      @      @ @              @ * .       @ @     @                        
                         @           @    @  @@ @@  @@  /   @          @   @                        
                      @ @            (  @@@@ @@ @@ @ @  @ #@ @@     / @ /                           
                    % @ #     @  @                      @    @@@@    @@ @                           
                            @ @ @     @@                   @ @@  @ @@  @ @                          
                  @   @   @  @      @    @@         @       @    @ @ @@ @ @@                        
                         @ @ .   @  @                          @ @ @  @@@ @                         
                          @ @% @   @   @    @          @  @  @ @ @  @ @@@ @  @                      
                       @     @    @@    #   ( @   @   @    @@  @ @@                                 
                      @     @ @    @    ,/ .@%@.    @ @    @  @ @  @   /                            
                    @ @ @                     @@ @ *    @   @ @@ @   @ @@@                          
                     @            @(  @           @    @     @@     @      @@@@                     
                        @            #  @ @  @  @  @@ @@ . @ @ *      @@ .   @@ @                   
                             @ @        @@@  @    @   @           .              @                  
                    @         @            @        @                        @  @   &               
                %  @      @ @   / @  (                       @ @  @   @    @ @ @@@                  
                . @  @ @         @   @   @    @  @    @   @@   @@#   @     @@     @                 
                   @    @                     @         @    @   @  @    @                          
                          @  @                   @      @@  @ ,     @                               
                                  @   @ @          @   @ @                                          
                                                    *                                               
                                                                                                    


Much love.

Warpath
Shadow Gov

