#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long long cardnumber= get_long_long("Enter a long long: ");
    if (!((cardnumber >= 1000000000000 && cardnumber < 10000000000000) || (cardnumber >= 100000000000000 && cardnumber < 10000000000000000)))
    {
        printf("INVALID\n");
        return 0;
    }
    int remainder = 0;
    int sum = 0;
    int i = 1;
    int creditcompany = 0;
    do{

        if(cardnumber < 100 && cardnumber > 10)
        {
            if (cardnumber == 34 || cardnumber == 37 )
            {
                creditcompany = 1;
            }
            if (cardnumber >= 51 && cardnumber <= 55 )
            {
                creditcompany = 2;
            }
        }
        remainder = cardnumber % 10;
        // if even, add to sum
        if(i % 2 != 0){
            sum += remainder;
        }// else, multiply by 2 then add to sum
        else{
            remainder *= 2;
            if (remainder >= 10){
                int temp = remainder % 10;
                sum += temp;
                remainder /= 10;
            }
            sum += remainder;

        }
        i++;
        cardnumber /= 10;


    }while(cardnumber >= 10);

    if (i % 2 != 0){
        sum += cardnumber;
    }
    else{
        remainder = cardnumber*2;
        if (remainder >= 10){
            int temp = remainder % 10;
            sum += temp;
            remainder /= 10;
        }
        sum += remainder;
    }

    if (sum % 10 != 0)
    {
        printf("INVALID\n");
        return 0;
    }
    else if (i == 15 && creditcompany == 1)
    {
        printf("AMEX\n");
    }
    else if (i == 16 && creditcompany == 2)
    {
        printf("MASTERCARD\n");
    }
    else if ((i == 13 || i == 16) && cardnumber == 4)
    {
        printf("VISA\n");
    }
    else{
        printf("INVALID\n");
    }
    return 0;
}