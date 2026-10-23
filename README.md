# AURA 

AURA is a custom mechanical desktop controller designed for media navigation and other things basic need in my life. It is built around a Raspberry Pi Pico, it has 6 mechanical keys, an 0.91 inch OLED display, and a multi-function rotary knob.

In simple words, I have made a PCB which has the neccessary areas and cutout (inside the PCB) to solder the parts in. 

Here the Rasberry Pi Pico works as the main controller of this project which handels all the working from presseng the switches, turning the knob to the text in the display. It controls almost everything. 

For the controls I have used the Key which will help me do a the kind of shortcut which i like to have on it. 

The knob is there for the up/down scrolling and the left/right scrolling in PDFs, webpages, CAD apps, 3D modeling, volume control, etc. 

The display is for showing wither the time or the current sony which is being play, with basic info in it. (this can also be coustomised from the firmware of the project).


I have specially designed a coustom enclosure for this, which is in 2 parts.

Base part:
    Here is where the PCB will be sitting. It will be mounted securly by the M3 mounting holes. There is a cutout on the back side of the Base so that we can connect the power/data cable to the Rasberry Pi Pico. 

Top Lid:
    The lid will be placed on the base lid securly. There are required cutouts for the display, the keys and the knob. 

I have made the colour of base as the default color, and the top in orange color to differential between them and make it easier for me to make and assemble the full enclosure with the PCB and all the parts. 
In the final printing, the enclosure will have a black colour (from the black PLA filament from the printing legion).





## Instructions AURA enclosure files

The .step file of the PCB is in the folder named**Hardware**. The name of the exact file is **AURA V2.step**
The rest of the file are in the folder named **Enclosure**.

The base part is of the name **AURA base.step**. 
The top Lid is of the name **AURA lid.step**.
The complete assembly of the enclosure with the PCB is of the name **AURA Full Assembly.step**.



## INSTRUCTIONS TO FOLLOW TO GET THE THE ASSEMBLED .STEP FILE

Unfortunatily, there is a specify way in which you have to open the **AURA Full Assembly.step** to actully get the the fully assembled file which has the base, top lid and the PCB with all the parts. 

This is the way (for this I am using Onshape. I think it will almost similar for all the different softwares):

* **uploading the file:** Click import (wherever the option is in your software) and select the specific file named **AURA Full Assembly.step**
* It will take 1-2 mins in importing all the parts. 
* **Selecting the file:** After all the parts are successfully imported, from all the different files, you have to select the one which is named **AURA V2 1**. This is the file which will contain the fully assembled file.

![alt text](<Screenshot 2026-10-24 003430.png>)



---
## Key Features

* **Microcontroller:** Powered by the Raspberry Pi Pico (RP2040).
* **Macro Matrix:** 6 mechanical keys (`SW2` through `SW7`).
* **Interactive OLED Display:** A 0.91-inch SSD1306.
* **Multi-Function Rotary Encoder (The Crown):** 
  * *Default:* Vertical scrolling.
  * *Shift + Rotate:* Horizontal scrubbing / zooming.
  * *Fn + Rotate:* System volume control.
  * *Push Switch:* Quick action trigger.
* **Smart Power-Saving:** Automatic 15-minute inactivity sleep timer to preserve screen life.
* **Dynamic Configuration:** Easily remap keys without rewriting firmware by editing a simple `config.json` file stored directly on the device.
* **Secure Enclosure Ready:** Integrated corner M3 mounting holes (`H1`–`H4`) for robust case assembly.
---

![alt text](<Screenshot 2026-10-11 125142.png>)
![alt text](<Screenshot 2026-10-23 234108.png>)
![alt text](<Screenshot 2026-10-11 124917.png>)
![alt text](<Screenshot 2026-10-22 214454.png>)
![alt text](<Screenshot 2026-10-22 214441.png>)
![alt text](<Screenshot 2026-10-11 125030-1.png>)
