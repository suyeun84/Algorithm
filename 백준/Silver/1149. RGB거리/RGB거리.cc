#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

int min(int x, int y) {
	return x > y ? y : x;
}

int main() {

	//빨강0 초록1 파랑2
	int home, result;
	int cost[1001][3];
	int dp[1001][3];
	scanf("%d", &home);
	for (int i = 0; i < home; i++) {
		for (int j = 0; j < 3; j++) {
			scanf("%d", &cost[i][j]);
		}
	}
	dp[0][0] = cost[0][0];
	dp[0][1] = cost[0][1];
	dp[0][2] = cost[0][2];

	for (int i = 1; i < home; i++) {
		dp[i][0] = min(dp[i - 1][1]+ cost[i][0], dp[i - 1][2] + cost[i][0]);
		dp[i][1] = min(dp[i - 1][0]+ cost[i][1], dp[i - 1][2] + cost[i][1]);
		dp[i][2] = min(dp[i - 1][0]+ cost[i][2], dp[i - 1][1] + cost[i][2]);
	}

	if (dp[home - 1][0] < dp[home - 1][1]) {
		if (dp[home - 1][0] < dp[home - 1][2]) {
			result = dp[home - 1][0];
		}
		else {
			result = dp[home - 1][2];
		}
	}
	else {
		if (dp[home - 1][1] < dp[home - 1][2]) {
			result = dp[home - 1][1];
		}
		else {
			result = dp[home - 1][2];
		}
	}
	printf("%d", result);
}
