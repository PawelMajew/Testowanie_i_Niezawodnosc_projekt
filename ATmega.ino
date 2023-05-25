//#define DEBUG
#include "math.h"
void setup() {
  Serial.begin(9600); //inicjalizacja portu szeregowego
}

void loop() {
  while (Serial.available() == 0) {} //oczekiwanie na dane wejściowe

  float data[4] = {0.0f, 0.0f, 0.0f, 0.0f};
  float a, b, c;
  int i = 0;
  int stopien;
  while (Serial.available() && i < 4) {
    data[i] = Serial.parseFloat();
    i++;
    delay(10); // opóźnienie, aby dać czas na odczytanie kolejnych bajtów
  }

  stopien = 3;
  while (data[stopien] == 0.0f) {
    --stopien;
  }

  a = data[2];
  b = data[1];
  c = data[0];
#ifdef DEBUG
  for (int j = 0; j < 4; j++) {
    Serial.print(data[j]);
    Serial.print(" ");
  }

  Serial.print("stopien: ");
  Serial.println(stopien);
#endif
  if (stopien == 2) {

    float delta = b * b - 4 * a * c; //obliczenie delty

    if (delta > 0) { //jeśli delta > 0, istnieją dwa miejsca zerowe
      float x1 = (-b + sqrt(delta)) / (2 * a);
      float x2 = (-b - sqrt(delta)) / (2 * a);
      Serial.print(x1);
      Serial.print(" ");
      Serial.println(x2);
    }
    else if (delta == 0) { //jeśli delta = 0, istnieje jedno miejsce zerowe
      float x = -b / (2 * a);
      Serial.println(x);
    }
    else { //jeśli delta < 0, nie ma miejsc zerowych
      Serial.println("NULL");
    }
  }
  if (stopien == 1) {
    Serial.println(-c / b);
  }

  if (stopien == 3) {
#ifdef DEBUG
    Serial.println("3 stopien");
#endif
    float coeff3, coeff2, coeff1, coeff0;
    float res;
    float i;
    float res1, res2, res3, res4;
    float discriminant;
    float root2, root3;
    float sqrtDiscriminant;

    coeff3 = data[0];
    coeff2 = data[1];
    coeff1 = data[2];
    coeff0 = data[3];

    //finding the 1st root  by trial and error method
    for (i = 0; i < 10; i++)
    {
      res = (pow(i, 3) * coeff3) + (pow(i, 2) * coeff2) + (i * coeff1) + (coeff0);
      if (res == 0)
      {
        break;
      }

      else continue;
    }

    for (i = -10; i < 0; i++)
    {
      res = (pow(i, 3) * coeff3) + (pow(i, 2) * coeff2) + (i * coeff1) + (coeff0);
      if (res == 0)
      {
        break;
      }

      else continue;
    }

    //Applying synthetic division and reducing cubic to quadratic eqaution
    res1 = (i * 0) + coeff3;
    res2 = (res1 * i) + coeff2;
    res3 = (res2 * i) + coeff1;
    res4 = (res3 * i) + coeff0;

    //Solving the reduced Quadratic equation using the quadratic formula
    discriminant = ((res2 * res2) - (4 * res1 * res3));

    sqrtDiscriminant = sqrt(discriminant);

    root2 = ((-1 * res2) - (sqrtDiscriminant)) / (2 * res1);

    root3 = ((-1 * res2) + (sqrtDiscriminant)) / (2 * res1);

    Serial.print(i);
    Serial.print(" ");
    Serial.print(root2);
    Serial.print(" ");
    Serial.println(root3);
  }

  while (Serial.available() > 0) { //oczekiwanie na wyczyszczenie bufora wejściowego
    char c = Serial.read();
  }
}
