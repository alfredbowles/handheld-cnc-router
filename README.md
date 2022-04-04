# Handheld CNC Router - Frebujar

The handheld CNC router is a project developed by Alfred Bowles, Shamanth Thenkan & Vincent Verster for a 2 month hardware seminar at the Institute for Advanced Architecture of Catalonia

The project aim is to develop a handheld CNC router which could be used for milling and inscribing into planar msheets of material.
The router will be hand-guided by the user while motors which control the position of the mill bit will activate to correct for the error made by the user between the actual and target position of the bit.

# Hardware & Materials #

### Complete Assembly ###
* 4x Milled - Particle board, laminated on both sides : Thickness = 10mm
* 3x Lasercut - Plexiglass : Thickness = 6mm
* 2x Radial ball bearings : ID = 10mm
* 2x Radial ball bearings : ID = 50mm
* 2x Linear Bearings: ID = 10mm (For z-axis movement)
* 10mm thick calibrated steel rod
* 1x Shaft support
* 1x Threaded shaft bearing
* Various 3D Printed parts

![LabeledPrototypeWhite](https://user-images.githubusercontent.com/61389567/161610991-9457924f-5f27-4508-97f6-68dbff60ef82.png)

### Control, Power and Actuation ###
* 1x Raspberry Pi 4
* 1x Arduino Uno
* 1x 8MP Raspberry Pi Camera Module v2.1
* 1x Waveshare Raspberry Pi LCD Screen 3.5inch
* 3x Nema 17 Stepper Motors
* 3x A4988 Stepper Motor Drivers
* 1x 5v Fan
	
![image44](https://user-images.githubusercontent.com/61389567/161609687-d3d0913a-68f3-436f-ba99-99cd2eb053f7.png)

# Use Process

The user would either print or draw the desired pattern to be routed onto the piece of material. He would then activate the router and pass it over the material approximately following the printed path. The mounted camera which is aimed at the region around the bit tip will calculate the deviation needed to be made to account and correct for the user error and order the motors to move the mill head to the calculated point. As the user progresses through the material only the black areas which were printed or drawn will be removed and the piece would be complete.

# Control

Since we are using a double cam mechanism we need to calculate how the bit would move with respect to the given motor rotations. In order to calculate the bit deviation, we use trigonometry and the law of cosines and sines.

### Angle Calculation ###
This code attempts to solve for those angles. (Angle calculation still to be optimized):
* Final_motion_calculation.py

The variables defined in the code are shown in the below diagram:
![WhiteKinematics](https://user-images.githubusercontent.com/61389567/161617604-2ef2f1a4-26f8-41f6-8471-3f9bb0f43054.png)

### Adruino Motor control code ###
The file to convert the desired angles to microsteps and control the motors according to those steps
* Arduino_Motor_Control.ino

### Camera Calibration & Homography: ###
This file is run only once at the beginning in order to calibrate the camera and account for the exact distance and orientation of the camera with respect to the bit
* Homgraphy_Calibration.py

### Main Code - Line Tracking ###
The following file is used to detect object contours, calculate their centroids and fine the distance and angle between the camera center and the object center. These numbers are then outputted to the Final_motion_calculation.py file which then finds the desired motor angles.
* LineTracking.py 
