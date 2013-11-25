#include <stdio.h>
#include <stdlib.h>

int main()
{
	char *t;
	char *c;
	char *num;
	
	printf("Enter a string with commas (number format): \n");
	scanf("%s", num);
	
	c = &num[0];
	t = c;
	while(*c != '\0') {
		if(*c != ',') {
			*t = *c;
			t++;
		}
		c++;
	}
	
	*t = '\0';
	
	printf("Final string:\t%s", num);
}
