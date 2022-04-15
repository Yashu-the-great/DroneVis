from Movement.movement import move_forward,move_backward,move_left,move_right,no_horizontal_movement,no_vertical_movement
from VisionFiles.vision import recognise

process_this_frame = True
fl = 100

width = 640
height = 480

# 640 X 480 img

def main():
    var = recognise(process_this_frame,fl)
    if var != None:
        center_of_face,d=var
        if d > 3:
            move_forward()
        elif d < 3:
            move_backward()
        else:
            no_horizontal_movement()
        if center_of_face[0] > width/2:
            move_left()
        elif center_of_face[0] < width/2:
            move_right()
        else:
            no_vertical_movement()


if __name__ == "__main__":
    while True:
        main()
