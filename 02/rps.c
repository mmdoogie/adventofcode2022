#include <stdio.h>

int rps(char opp, char me) {
	int shapePoints = me - 'X' + 1;
	const int win = 6;
	const int draw = 3;
	const int lose = 0;
	int resultPoints = 0;

	if (opp == 'A') {
		if (me == 'X') {
			resultPoints = draw;
		} else if (me == 'Y') {
			resultPoints = win;
		} else if (me == 'Z') {
			resultPoints = lose;
		} else {
			printf("PANIC!");
		}
	} else if (opp == 'B') {
		if (me == 'X') {
			resultPoints = lose;
		} else if (me == 'Y') {
			resultPoints = draw;
		} else if (me == 'Z') {
			resultPoints = win;
		} else {
			printf("PANIC!");
		}
	} else if (opp == 'C') {
		if (me == 'X') {
			resultPoints = win;
		} else if (me == 'Y') {
			resultPoints = lose;
		} else if (me == 'Z') {
			resultPoints = draw;
		} else {
			printf("PANIC!");
		}
	} else {
		printf("PANIC!");
	}

	return resultPoints + shapePoints;
}

int main() {
	FILE* f = fopen("input", "r");
	char buff[4];
	int totalScore = 0;
	while (!feof(f)) {
		char c = fread(&buff, 1, 4, f);
		if (c != 4) break;
		int score = rps(buff[0], buff[2]);
		totalScore += score;
		printf("%c %c = %d\n", buff[0], buff[2], score);
	}
	printf("Total Score: %d\n", totalScore);
}
