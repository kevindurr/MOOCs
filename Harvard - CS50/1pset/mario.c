#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;
    // Get height until proper value inputted
    do{
        height = get_int("Height is: ");
    }while(height < 0 || height > 23);

    for (int i = 0; i < height; i++){

        int hash = i + 1;
        int space = height - hash;

        //print out spaces
        for (int j = 0; j < space; j++){
            printf(" ");
        }
        // print left pyramid hashes
        for (int j = 0; j < hash; j++){
            printf("#");
        }
        // print pyramid separator spaces
        for (int j = 0; j < 2; j++){
            printf(" ");
        }
        // print right pyramid hashes
        for (int j = 0; j < hash; j++){
            printf("#");
        }
        printf("\n");
    }
}