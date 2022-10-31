

from time import sleep
import paho.mqtt.client as paho
import pygame
broker="127.0.0.1"
port=1883
def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass
client1= paho.Client("control1")                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker,port)                                 #establish connection

angular_speed=0
linear_speed=0

pygame.init()
display = pygame.display.set_mode((300, 300))
print("Initialized")
running=True
while(running):
    for event in pygame.event.get():

        # Check for KEYDOWN event

        if event.type == pygame.KEYDOWN:
            #print("Key Pressed:")
            # If the Esc key is pressed, then exit the main loop

            if event.key == pygame.K_ESCAPE:
                running = False
                angular_speed = 0
                linear_speed = 0
            if event.key==pygame.K_UP :
                linear_speed += 0.25
            if event.key==pygame.K_DOWN :
                linear_speed -= 0.25
            if event.key==pygame.K_RIGHT:
                angular_speed += 0.25
            if event.key==pygame.K_LEFT:
                angular_speed -= 0.25

            message = str(linear_speed) + "/" + str(angular_speed)
            print(message)
            client1.publish("/topic", message)
        # Check for QUIT event. If QUIT, then set running to false.



    

    
    