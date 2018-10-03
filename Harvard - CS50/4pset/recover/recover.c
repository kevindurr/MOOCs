#include <stdio.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        fprintf(stderr, "Expected one command-line argument\n");
        return 1;
    }

    char *infile = argv[1];
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    int counter = 0;
    uint8_t buffer[512];
    FILE *img = NULL;

    while (fread(buffer, 512, 1, inptr) == 1)
    {
        if (buffer[0]== 0xff && buffer[1]== 0xd8 && buffer[2]== 0xff && (buffer[3] & 0xf0) == 0xe0){
            if (counter > 0)
            {
                fclose(img);
            }
            char filename[7];
            sprintf(filename, "%03d.jpg", counter);
            img = fopen(filename, "w");
            counter++;
        }
        if (img){
            fwrite(buffer, 512, 1, img);
        }
    }
    if (counter > 0){
        fclose(img);
    }
    fclose(inptr);
}
