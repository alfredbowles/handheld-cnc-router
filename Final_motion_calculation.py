import math as m
import matplotlib.pyplot as plt

# Plot links, motors, bit location and target location

def plotkinematics():
    plt.plot(x0, y0, '-d')
    draw_circle = plt.Circle((m1x, m1y), 17.5,fill=False, color="C3") 
    draw_circle2 = plt.Circle((m2x, m2y), 17.5,fill=False, color="C3")
    draw_circlebit = plt.Circle((bitx, bity), 3,fill=False, color="C5")
    plt.gcf().gca().add_artist(draw_circle)
    plt.gcf().gca().add_artist(draw_circle2)
    plt.gcf().gca().add_artist(draw_circlebit)
    plt.plot(x,y,'-o')
    plt.plot(m1x,m1y, '-o')
    plt.plot(m2x,m1y, '-o')
    plt.plot(bitx,bity, '-d')
    plt.plot(Ax, Ay, '-o')
    plt.plot(Bx, By, '-o')
    plt.plot([m1x,Ax],[m1y,Ay],'k-')
    plt.plot([m2x,Bx],[m2y,By],'k-')
    plt.plot([x,Ax],[y,Ay],'k-')
    plt.plot([x,Bx],[y,By],'k-')
    plt.plot([Ax,Bx],[Ay,By],'k-')
    
    plt.show()   

# Initialize

r1 = 17.5
r2 = 17.5
L1 = 110
L2 = 219.32
x0 = 90.16
y0 = -65.41
xn = -217.44
bitx = x0 + 63.64
bity = y0 - 63.64
dx = 5
dy = 5

(m1x, m1y) = (0,0)
(m2x, m2y) = (307.59,0)

x = x0 + dx
y = y0 + dy
xn = dx - (m2x - 90.16)

# Calculate angles ThetaL2 & ThetaL1 for the left side link
thetaL2 = -round(m.acos((x**2+y**2-r1**2-L1**2)/(2*r1*L1)),2)
thetaL1 = round(m.degrees(m.atan(y/x)-m.atan((L1*m.sin(thetaL2))/(r1+L1*m.cos(thetaL2)))),2)

# Calculate angles Thetar2 & ThetaR1 for the right side link
thetaR2 = round(m.acos((xn**2+y**2-r2**2-L2**2)/(2*r2*L2)),2)
thetaR1 = 180+round(m.degrees(m.atan(y/xn)-m.atan((L2*m.sin(thetaR2))/(r2+L2*m.cos(thetaR2)))),2)

# Calculate the position of points A, B and C based on the angles previously found
(Ax, Ay) = (r1*m.cos(m.radians(thetaL1)), r1*m.sin(m.radians(thetaL1)))
(Bx, By) = (m2x+r2*m.cos(m.radians(thetaR1)), m2y+r2*m.sin(m.radians(thetaR1)))
(Cx, Cy) = (x,y)

# Determine bit position with respect to motor angles (63.64 = distance between point C and the bit)
bitx, bity = (Cx + 63.64, Cy - 63.64 )

# The above was calculated to determine the forward kinematics relations between the motor input and the the bit tip. However the opposite also needs to be done
# since we need to infer the motor angles based on the bot location. Therefore we procedd to find the needed lengths L3, L4 & L5 and angles A,B,C & D:
L3 = abs(m.sqrt((Ay - By)**2 + (Ax-Bx)**2))
L4 = m.sqrt(63.64**2 + 63.64**2)
L5 = 200

angleA = round(m.degrees(m.acos((L1**2+L3**2-L2**2)/(2*L1*L3))),2)
angleB = round(m.degrees(m.acos((L2**2+L3**2-L1**2)/(2*L2*L3))),2)
angleC = round(m.degrees(m.acos((L1**2+L2**2-L3**2)/(2*L1*L2))),2)
angleD = round(m.degrees(m.acos((L2**2+L4**2-L5**2)/(2*L2*L4))),2)

# Calculate gamma

gamma = (By - Ay) / (Bx - Ax)

alpha0 = 44.99 + 114.24
alpha = angleA + angleC - alpha0

bit_target_x=bitx*m.cos(alpha)
bit_target_y=bity*m.sin(alpha)

print(f"L3 = {L3} ; L4 = {L4} ; L5 = {L5}")
print(f"Angle A = {angleA}\nAngle B = {angleB}\nAngle C = {angleC}\nAngle D = {angleD}\n")

motor1angle = thetaL1 - 45
motor2angle = thetaR1 - 135

print(f"Theta L1 = {thetaL1} ; Theta L2 = {round(m.degrees(thetaL2),2)}\nTheta R1 = {thetaR1} ; Theta R2 = {round(m.degrees(thetaR2),2)}")
print(f"Motor 1 Angle = {round(motor1angle,1)} ; Motor 2 Angle = {round(motor2angle,1)}")
plotkinematics()