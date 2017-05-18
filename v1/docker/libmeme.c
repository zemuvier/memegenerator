//#include "/usr/local/include/gd.h"
//#include "/usr/local/include/gdfontl.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <gd.h>
#include <gdfontl.h>

void makeMeme(char *input, char *output, char *text)
{
    FILE *in, *out;
    gdImagePtr im;
    int black;
    int white;
    in = fopen(input, "r");
   // if (in == NULL) return 1;

    //im = gdImageCreateFromPng(in);
    im = gdImageCreateFromJpeg(in);
    fclose(in);

    black = gdImageColorAllocate(im, 0, 0, 0);
    white = gdImageColorAllocate(im, 255, 255, 255);

    gdImageString(im, gdFontGetLarge(),
                  im->sx / 2 - (strlen(text) * gdFontGetLarge()->w / 2),
                  im->sy - im->sy / 10,
                  text, black);

    //gdImagePng(im, out);
    out = fopen(output, "w");
//    printf("Meme created!\n");
    gdImageJpeg(im, out, 95);
    gdImageDestroy(im);
    //if (out == NULL) return 1;
    fclose(out);
    //return 0;
}

int main()
{
   // FILE *in, *out;
    char *text, *input, *output;

   // input = "ex.jpg";
    //output = "ex1.jpg";
    //text = "sss";

    //in = fopen(input, "r");

    //makeMeme(input, output, text);

    return 0;
}
