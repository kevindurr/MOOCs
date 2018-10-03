#define _XOPEN_SOURCE
#include <unistd.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    string input = argv[1];
    int size = strlen(input);

    char salt[1];
    memcpy( salt[0], input[0]);
    memcpy( salt[1], input[1]);

    if (argc !=  2)
    {
        return 1;
    }

    printf("salt is: %c\n", salt);

}