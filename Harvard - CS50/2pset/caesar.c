#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    if (argc != 2)
        return 1;

    int k = atoi(argv[1]);
    if (k > 26)
    {
        k = k % 26;
    }
    string plaintext = get_string("plaintext: ");

    printf("ciphertext: ");
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        if (islower(plaintext[i]))
        {
            int getCharPlace = plaintext[i] % 97;
            printf("%c", 'a' + ((getCharPlace + k) % 26));
        }
        else if (isupper(plaintext[i]))
        {
            int getCharPlace = plaintext[i] % 65;
            printf("%c", 'A' + ((getCharPlace + k) % 26));
        }
        else
        {
            printf("%c", plaintext[i]);
        }
    }
    printf("\n");
}