#include <math.h>
#include <stdio.h>
#include <stdlib.h>

double answer;

void leibniz_pi(int iterations) {
  double i;
  for (i = 0; i < iterations; i++) {
    double numerator = pow(-1, i);
    double denominator = 2 * i + 1;
    double num = numerator / denominator;
    answer = answer + num;
  }
  answer = answer * 4;
}

int main(int argc, char *argv[]) {
  char *char_iterations = argv[1];
  int iterations = atoi(char_iterations);
  leibniz_pi(iterations);
  printf("%lf\n", answer);
}
