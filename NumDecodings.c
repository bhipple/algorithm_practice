#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int numDecodings(char *str);

int main() {
	int res;
	char *str;
	
	printf("Enter a number. Any '0's must be preceded by a 1 or 2\n");
	scanf("%s", str);
	
	res = numDecodings(str);
	
	printf("There are %d decodings", res);
	
}

int numDecodings(char *str) {
	char *t;
	char *p;
	if(strlen(str) < 2)
		return 1;
	
	t = str;
	p = str + 1;
	if( (*t == '1' && *p > '0') || (*t == '2' && *p > '0' && *p <= '6'))
		return numDecodings(t + 1) + numDecodings(t + 2);
	else
		return numDecodings(t + 1);
}
