#include <stdio.h>

int main(){
	char string[10];
	int num;
	char symbols;
	scanf("%s %d %c", string, &num, &symbols);
	printf("%s %d %c", string, num, symbols);

	return 0;
}