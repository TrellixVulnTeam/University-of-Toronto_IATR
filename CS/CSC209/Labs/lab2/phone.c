#include <stdio.h>

int main(){
  char phone[11];
  int num;
  scanf("%s %d", &phone, &num);


  if(num == 0){
    printf("%s\n", phone);
    return 0;
  }

  if(num >= 1 && num <=9){
    printf("%c\n", phone[num]);
    return 0;
  }

  if(num < 0 || num > 9){
    printf("ERROR\n");
    return 1;
  }
}
