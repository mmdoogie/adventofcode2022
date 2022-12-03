#include <stdio.h>

int rps(char opp, char me) {
	int resultPoints = (me - 'X') * 3;
	int shapePoints;

	if (opp == 'A') {
		if (me == 'X') {
			shapePoints = 3;
		} else if (me == 'Y') {
			shapePoints = 1;
		} else if (me == 'Z') {
			shapePoints = 2;
		} else {
			printf("PANIC!");
		}
	} else if (opp == 'B') {
		if (me == 'X') {
			shapePoints = 1;
		} else if (me == 'Y') {
			shapePoints = 2;
		} else if (me == 'Z') {
			shapePoints = 3;
		} else {
			printf("PANIC!");
		}
	} else if (opp == 'C') {
		if (me == 'X') {
			shapePoints = 2;
		} else if (me == 'Y') {
			shapePoints = 3;
		} else if (me == 'Z') {
			shapePoints = 1;
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
