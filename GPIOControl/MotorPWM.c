#include <stdio.h>
#include <stdlib.h>

#include <wiringPi.h>

void delay(unsigned int milliseconds) {
    clock_t pause;
    clock_t start;

    pause = milliseconds * (CLOCKS_PER_SEC / 1000);
    start = clock();
    while( (clock() - start) < pause );
}

int main() {
    if(wiringPiSetup() == -1) {
        puts("Error in setting up the raspberry pi wiring library\n");
        exit(1);//exit if error in setting the library
    }

    pinMode(1,PWM_OUTPUT);// setting GPIO 1 as PWM analog output pin

    pwmWrite(1,0); // duty cycle 0
    delay(1000);
    
    printf("[+] Gradually increasing the duty cycle by 1 after 10ms [+]\n");

    for(int i =0;i<1023;i+=1) {
        pwmWrite(1,i);
        printf("Duty Cycle Number : %i\r",i);
        delay(10);
    }
    
    puts("\n");
    printf("[+] Gradually decreasing the duty cycle by 1 after 10ms [+]\n");

    for(int i = 1023;i>=0;i-=1){
        pwmWrite(1,i);
        printf("Duty Cycle Number : %i\r",i);
        delay(10);
    }
    
    puts("[-] End of the program [-]");
    return 0;
}
