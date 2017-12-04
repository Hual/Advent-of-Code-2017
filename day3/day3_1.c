#include <stdio.h>
#include <math.h>

int main()
{
    int input;
    scanf("%i", &input);
    int layer = floor(ceil(sqrt(input)) / 2);
    int layer_size = layer * 2;
    int distance = abs((layer_size - (input - (layer_size - 1) * (layer_size - 1)) % layer_size) - layer) + layer;
    printf("%i\n", distance);

    return 0;
}
