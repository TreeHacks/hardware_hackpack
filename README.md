# hardware_hackpack

This is an overview of how to use a microcontroller- specifically the Raspberry Pi Pico! We nail down some foundations here and will have more hardware-related even ... We hope the skills you learn from this hackpack help you get a footing in hardware hacks and think in hardware :))

#### Parts:
1. Raspberry Pi Pico
2. Micro USB cable 
3. Your computer!
4. TCS3200 Color Sensor (optional)
5. Jumper wires (optional)
6. Breadboard (optional)
7. i2c display (optional)

## Setup

1) Download Thonny: From https://thonny.org/, click on the download button for your requisite OS that is on the top right corner of the screen. 

2) Connect the pico to your computer: You will need a micro-usb wire that connects the pico to your computer. While connecting it, you need to press down on the white bootsel button on the pico and then release it. 



A folder should pop up titled RPI-RP2- this means that the pico has successfully been flashed to your computer. 
<img width="950" alt="Screenshot 2022-12-23 at 3 55 32 PM" src="https://user-images.githubusercontent.com/93958307/209323810-9fbea274-6d98-4ac1-99fc-a80f2b072a6d.png">

3) Download uf2 file: In this RPI-RP2 folder, click on the INDEX.HTM file which will redirect you to a webpage titled "Raspberry Pi Documentation". Scroll down on this page and under the "Microcontrollers" tab you will see "Micropython". Click on that. 
<img width="1238" alt="Screenshot 2022-12-23 at 3 58 57 PM" src="https://user-images.githubusercontent.com/93958307/209320266-1950d801-a727-43f0-8ea8-959ff351c047.png">

Now, on the page about Micropython scroll down to the "Drag-and-Drop MicroPython" section under which you will see instructions to download micropython for different boards. Click on the "Raspberry Pi Pico" option and a uf2 file should begin downloading (file named something like rp2-pico-......uf2).
<img width="1224" alt="Screenshot 2022-12-23 at 4 01 33 PM" src="https://user-images.githubusercontent.com/93958307/209320961-1aadbe9c-0a17-40eb-b862-4ff817c19e52.png">

5) Add file to pico: Drag and drop the file into the RPI-RP2 folder. This will cause the pico to disconnect which is what is expected to happen. Then, unplug the pico from the mac. This process of setup is only required once for setting up micropython, and you do not need to do this everytime you connect the pico to your computer. 

![gif_pico](https://user-images.githubusercontent.com/93958307/209324715-f7351ff9-e491-4e9c-a86c-b4222e115b00.gif)

## Micropython on the Pico

1) Connect the pico: Connect the pico to your computer by simply plugging it in. Do not press the bootsel button. Furthermore, no folder will be appearing this time. 

2) Connect to Thonny: Next, open up the thonny editor we downloaded in step 1 of "Setup". 

7) Hello world: Let us check if there are any errors by running a simple print ... 

8) do sample blink.py code

9) explain main.py aspect

## The Pico

go over the pins on the board

## Example: color sensing


## Conclusion


