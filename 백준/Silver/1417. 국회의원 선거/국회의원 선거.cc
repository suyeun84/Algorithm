#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

int main() {
	int total;
	int result = 0;
	int vote[50];
	int max;
	int index = 0;

	
	scanf("%d", &total);
	for (int i = 0; i < total; i++) {
		scanf("%d", &vote[i]);
	}

	while (1) {
		max = 0;
		for (int z = 1; z < total; z++) {
			if (max <= vote[z]) {
				max = vote[z];
				index = z;
			}
		}
		if (vote[0] > max) {
			printf("%d", result);
			break;
		}
		vote[index]--;
		vote[0]++;
		result++;
	}
}