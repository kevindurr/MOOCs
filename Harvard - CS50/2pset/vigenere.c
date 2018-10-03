#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    if (argc != 2)
        return 1;

    string k = argv[1];
    int keylength = strlen(k);
    int putValue[keylength];
    for (int i =0; i < keylength; i++){
        if (islower(k[i]))
        {
            putValue[i] = (k[i] % 97);
        }
        else if (isupper(k[i]))
        {
            putValue[i] = (k[i] % 65);

        }
        else
        {
            return 1;
        }
    }
    string plaintext = get_string("plaintext: ");

    printf("ciphertext: ");
    for (int i = 0, j = 0, n = strlen(plaintext); i < n; i++)
    {
        if (islower(plaintext[i]))
        {
            int getCharPlace = plaintext[i] % 97;
            printf("%c", 'a' + ((getCharPlace + putValue[j%keylength] ) % 26));
            j++;
        }
        else if (isupper(plaintext[i]))
        {
            int getCharPlace = plaintext[i] % 65;
            printf("%c", 'A' + ((getCharPlace + putValue[j%keylength] ) % 26));
            j++;
        }
        else
        {
            printf("%c", plaintext[i]);
        }
    }
    printf("\n");
}