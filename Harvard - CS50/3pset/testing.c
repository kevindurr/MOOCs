#include <cs50.h>
#include <string.h>
#include <stdio.h>
#include <math.h>
int main(void)
{
    string note = get_string("Please enter string: " );
    char letter = note[0];
    int octave;

    bool sharp;
    if (note[1] == '#')
    {
        sharp = true;
        octave = note[2] - '0';
    }
    else
    {
        sharp = false;
        octave = note[1] - '0';
    }

    double frequency = 0.0;
    switch(letter)
    {
        case 'A':
            break;
        case 'B':
            break;
        case 'C':
            break;
        case 'D':
            break;
        case 'E':
            break;
        case 'F':
            break;
        case 'G':
            break;

    }
    if (letter == 'A' && !sharp)
    {
        if (octave > 4)
        {
           yolo = pow(2, octave - 4) * 440;
        }
        if (octave <= 4)
        {
           yolo = 440 / pow(2, 4 - octave);
        }
    }
    else if (letter == 'A' && sharp)
    {
        if (octave > 4)
        {
           yolo = pow(2, octave - 4) * 440;
        }
        if (octave <= 4)
        {
           yolo = 440 / pow(2, (4 - octave));
        }
    }
    printf("yolo is: %i\n", yolo);
}
