#include <stdio.h>

int main(){
  char phone[11];
  int num;
  int num_error = 0;

  scanf("%s", &phone);

  while (scanf("%d", &num) != EOF){
  if(num == 0){
    printf("%s\n", phone);

  }

  if(num >= 1 && num <=9){
    printf("%c\n", phone[num]);

  }

  if(num < 0 || num > 9){
    printf("ERROR\n");
    num_error +=1;

  }
}
if (num_error == 0){
  return 0;
}
else{
  return 1;
}

}
