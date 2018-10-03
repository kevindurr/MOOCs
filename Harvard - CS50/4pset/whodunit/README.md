# Questions

## What's `stdint.h`?

The <stdint.h> header shall declare sets of integer types having specified widths, and shall define corresponding sets of macros. It shall also define macros that specify limits of integer types corresponding to types defined in other standard headers.

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

The point of using these data types is to document intent for the amount of bits and how you will use them.

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

BYTE = 1 byte
DWORD = 4 bytes;
LONG = 4 bytes;
WORD = 2 bytes;

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

Hexadecimal file header for BMP must be: 424d

## What's the difference between `bfSize` and `biSize`?

biSize is the number of bytes required by the structure. While, bfSize is the size of the bitmap file

## What does it mean if `biHeight` is negative?

A positive biHeight means the bitmap is a bottom-up device-independent bitmap originating from its lower-left corner.
A negative biHeight means the bitmap is top-down, originating from its upper-left corner.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount specifies bits per pixel.

## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?

There are many ways fopen might return NULL. But the most common ways in this context is:
24. If the infile does exist or have read permissions, fopen will return NULL.
32. If the outfile does not have write permissions, fopen will return NULL
and if any of the files are actually directories, fopen will return NULL

## Why is the third argument to `fread` always `1` in our code?

The third argument specifies the number of items we want to read. We only want to fread one item.

## What value does line 65 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?

padding is 3 when biWidth is 3.

## What does `fseek` do?

Sets the position indicator associated with the stream to a new position.

## What is `SEEK_CUR`?

Current position of file pointer.

## Whodunit?

It was professor plum with the candlestick in the library