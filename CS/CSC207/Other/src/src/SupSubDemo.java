import java.util.ArrayList;

public class SupSubDemo {
    static int a = 9;
    SupSubDemo (int n){
        this.a = n;

    }
  public static void main(String[] args) {
//      Sup sup = new Sup();
//      sup.m();
//      Sub sub = new Sub();
//      sub.m();
//      // Java uses the type of the object to determine which method to run.
//      // Java uses the type of the expression to determine whether
//       code will compile.
//      sup = sub;
//      sup.m();
//
//      sub = (Sub) sup; // typecast: "I know better Java, this is a Sub"
//      // You'd better be right.
//      sub.m();
//      String a = new String("hahaha");
//      String b = new String("hahaha");
//      System.out.println( a == b);
//      SupSubDemo dubi = new SupSubDemo(5);
//      System.out.println(SupSubDemo.a);
//        Object a = new Object();
//        Object b = new Object();
//      System.out.println( a.equals(b));
//      System.out.println( a == b);
//
//
//
//      ArrayList a = new ArrayList();
//      (new Sub()).m1();
//      System.out.println("-----");
//      (new Sub()).m2();
//      System.out.println(SupSubDemo.a);
//      int i = 1;
//      System.out.println(i++);
//      System.out.println(i);
//      System.out.println(++i);
      try {System.out.println("hello");}
      catch (RuntimeException e){System.out.println("nihao");}
      finally {
          System.out.println("leihao");
      }

  }
}

class Super {
     void m1() {
        System.out.println("Super!");
    }
}

class Sub extends Super {
     void m1() {
         super.m1();
         System.out.println("And Sub!");
     }

     void m2(){
         ((Super)this).m1();
     }
}
