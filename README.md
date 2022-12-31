# hardware_hackpack

This is is a beginners tutorial of how to use a microcontroller- specifically the Raspberry Pi Pico. It's made to be accessible for anyone, no matter your experience level! We nail down some foundations here and will have more hardware-related events at the hackathon. We hope the skills you learn from this hackpack help you get a footing in hardware hacks and come up with creative ideas of your own! 

#### Parts:
1. Raspberry Pi Pico 
2. Micro USB cable 
3. Your computer!
4. Servo Motor (optional)
5. Jumper wires (optional)
6. Breadboard (optional)

# Setup ⚙️

1) Download Thonny: From https://thonny.org/, click on the download button for your requisite OS that is on the top right corner of the screen. 

2) Connect the pico to your computer: You will need a micro-usb wire that connects the pico to your computer. While connecting it, you need to press down on the white bootsel button on the pico and then release it. 

![picobootsel](https://user-images.githubusercontent.com/93958307/209513036-7c1e759a-7dba-4e99-8e2a-449fc67138fd.gif)

A folder should pop up titled RPI-RP2 which means that the pico has successfully been flashed to your computer. 

<img width="950" alt="Screenshot 2022-12-23 at 3 55 32 PM" src="https://user-images.githubusercontent.com/93958307/209323810-9fbea274-6d98-4ac1-99fc-a80f2b072a6d.png">

3) Download uf2 file: In this RPI-RP2 folder, click on the INDEX.HTM file which will redirect you to a webpage titled "Raspberry Pi Documentation". Scroll down on this page and under the "Microcontrollers" tab you will see "Micropython". Click on that. 

<img width="1238" alt="Screenshot 2022-12-23 at 3 58 57 PM" src="https://user-images.githubusercontent.com/93958307/209320266-1950d801-a727-43f0-8ea8-959ff351c047.png">

Now, on the page about Micropython scroll down to the "Drag-and-Drop MicroPython" section under which you will see instructions to download micropython for different boards. Click on the "Raspberry Pi Pico" option and a uf2 file should begin downloading (file named something like rp2-pico-......uf2).

<img width="1224" alt="Screenshot 2022-12-23 at 4 01 33 PM" src="https://user-images.githubusercontent.com/93958307/209320961-1aadbe9c-0a17-40eb-b862-4ff817c19e52.png">

5) Add file to pico: Drag and drop the file into the RPI-RP2 folder. This will cause the pico to disconnect which is what is expected to happen. Then, unplug the pico from the mac. This process of setup is only required once for setting up micropython, and you do not need to do this everytime you connect the pico to your computer. 

![gif_pico](https://user-images.githubusercontent.com/93958307/209324715-f7351ff9-e491-4e9c-a86c-b4222e115b00.gif)

# Micropython on the Pico 🖥️ 

1) Connect the pico: Connect the pico to your computer by simply plugging it in. Do not press the bootsel button. Furthermore, no folder will be appearing this time. 

2) Connect to Thonny: Next, open up the thonny editor we downloaded in step 1 of "Setup". Click on the bottom right tab as depicted in the image below and select "MicroPython (Raspberry Pi Pico).

<img width="833" alt="Screenshot 2022-12-23 at 7 53 37 PM" src="https://user-images.githubusercontent.com/93958307/209351487-b61eea61-8820-4dae-b442-fc549c4d8fbf.png">

7) Hello world: Let us check if there are any errors by running a simple print statement in Thonny's shell. 

<img width="868" alt="thonnyimg" src="https://user-images.githubusercontent.com/93958307/209351907-ad8aebe6-2af4-4548-966e-e4f059ec8c0e.png">

8) Blink.py: Now, we run an actual program on our Pico. Open up a new file in thonny and copy-paste the contents of blink.py that is available in this repository. Click on "Save" after doing so, where you will be prompted to choose where- choose "This Computer". Save your file as "blink.py". 

![thonnyblink](https://user-images.githubusercontent.com/93958307/209460037-6b61313e-6b9e-46f7-a0f9-b63856220c82.gif)

10) Run it: Then, click on the run button in the top tab of the Thonny editor. To stop running the program, click "stop" button that is in the same tab.

![thonnyconnect](https://user-images.githubusercontent.com/93958307/209353975-ccd6c73e-5579-4516-95b4-28d00ec2a4f3.gif)

This is the result of blink.py- the onboard LED of your pico blinking periodically! 

![picoblink](https://user-images.githubusercontent.com/93958307/209513748-d9da48de-b6f2-4129-8602-bc48b2bc1d44.gif)

9) Automatically Run Code: If you wish to run this code whithout having to click the "run" button and using Thonny, you can merely rename the file to be main.py and save it to "Raspberry Pi Pico" instead of "This Computer". The Pico is always on the lookout for the main.py file and automatically runs it. Hence, whenever the pico would be connected to a power source, it would automatically run the code in its main.py.

https://user-images.githubusercontent.com/93958307/209356017-308ecaa8-3088-4eb6-9975-39af675000bc.mov

//video showing me connecting and disconnecting it



#### Congrats on running a Micropython program on your Pico!! 🎉

Now, you can experiment with different micropython programs and make your pico do cool stuff. In the next section, we go over how to further connect your pico to other objects which will allow for much more scope with what you can build! 

### The Pico ⚡ 

The pico is a microcontroller much like the arduino or adafruit's infamous m4 feather express. It has digital input and output pins (GPIO) and analog ones (ADC). These pins are what's used when we connect the pico to other objects such as sensors, motors, LEDs, etc. You can read more about the pico in its datasheet: https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf

<img width="795" alt="Screenshot 2022-12-25 at 12 36 18 PM" src="https://user-images.githubusercontent.com/93958307/209459854-3e409013-b438-4ffc-b3a4-9d9e7befde19.png">

# Example: IR Sensor + Servo Motor

We're going to demonstrate how to use an IR sensor in conjunction with a servo motor. Our final result is going to be a servo motor that starts when an object gets close to the sensor!

## Sensor

#### Connections:

If you've never used a breadboard before and want to know more about it, you can check out ... , (though this isn't required)   
To connect the ir sensor, follow the image below:

![irpico](https://user-images.githubusercontent.com/93958307/210133069-0b2d2199-9dbe-45cd-a366-eba8e0e84daa.png)

The pins we have connected to are:  ////change
  Servo's red wire (VCC) to pico's 3V3(OUT) 
  Servo's black wire (GND) to pico's GND
  Servo's orange wire (OUT) to pico's GPIO-0

The process should look something like this:

#### Code

#### Demo

## Adding the servo

#### Connections: 
If you've never used a breadboard before and want to know more about it, you can check out ... , (though this isn't required)   
To connect the servo, follow the image below:

![picoservo](https://user-images.githubusercontent.com/93958307/209617753-6e762a2f-15ff-4fe4-b924-08c4fc5ca186.png)

The pins we have connected to are: 
  Servo's red wire (VCC) to pico's 3V3(OUT) 
  Servo's black wire (GND) to pico's GND
  Servo's orange wire (OUT) to pico's GPIO-0

The process should look something like this:

https://user-images.githubusercontent.com/93958307/209615678-ab9aa838-0db8-4334-8671-44983f771de6.mov

#### Code
Follow the code in the irmotor.py file. Run the code either by saving it as main.py on the board or by running it through Thonny as we had done earlier with the 'blink' example. 

#### Demo

# Conclusion

Arduino- 

Adafruit M4- 

Raspberry Pi Pico also supports arduino software. Circuitpython. 

# About HackPacks 🌲
HackPacks are built by the TreeHacks team to help hackers build great projects at our hackathon that happens every February at Stanford. We believe that everyone of every skill level can learn to make awesome things, and this is one way we help facilitate hacker culture. We open source our hackpacks (along with our internal tech) so everyone can learn from and use them! Feel free to use these at your own hackathons, workshops, and anything else that promotes building :)

If you're interested in attending TreeHacks, you can apply on our website during the application period.

You can follow us here on GitHub to see all the open source work we do (we love issues, contributions, and feedback of any kind!), and on Facebook, Twitter, and Instagram to see general updates from TreeHacks.


