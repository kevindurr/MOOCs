// Helper functions for music

#include <cs50.h>
#include <string.h>
#include "helpers.h"
#include <stdio.h>
#include <math.h>


// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{
    int X = atoi(&fraction[0]);
    int Y = atoi(&fraction[2]);
    return X * (8/Y);
}

// Calculates frequency (in Hz) of a note
int frequency(string note)
{
    char letter = note[0];
    int octave = note[strlen(note) - 1] - '0';
    double freq = 440;

    if (letter == 'A'){
        freq = 440;
    } else if (letter == 'B'){
        freq *= pow(2.0, 2.0 / 12.0);
    } else if(letter == 'C'){
        freq /= pow(2.0, 9.0 / 12.0);
    } else if (letter == 'D'){
        freq /= pow(2.0, 7.0 / 12.0);
    } else if(letter == 'E'){
        freq /= pow(2.0, 5.0 / 12.0);
    } else if (letter == 'F'){
        freq /= pow(2.0, 4.0 / 12.0);
    } else if(letter == 'G'){
        freq /= pow(2.0, 2.0 / 12.0);
    }

    if (octave > 4)
    {
        freq *= pow(2.0, octave - 4);
    } else if (octave < 4)
    {
        freq /= pow(2.0, 4 - octave);
    }

    if (note[1] == 'b')
    {
        freq /= pow(2.0, 1.0 / 12.0);
    } else if (note[1] == '#')
    {
        freq *= pow(2.0, 1.0 / 12.0);
    }

    return round(freq);
}

// Determines whether a string represents a rest
bool is_rest(string s)
{
    return !(strcmp(s, ""));
}
