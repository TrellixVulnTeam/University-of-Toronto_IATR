import java.util.HashMap;
import java.util.Map;

    import java.util.HashMap;

    public class StudentMarkHashMap {
        // TODO: declare your variables
        private String course;
        private int course_num;
        private Map<String, Integer> myMap;

        /**
         * TODO: Implement a constructor that takes a course code and course number
         * and initializes the HashMap.
         *
         * @param courseCode the course code. e.g. CSC
         * @param courseNumber the course number. e.g. 207
         */
        public StudentMarkHashMap(String course, int num){
            this.course = course;
            this.course_num = num;
            this.myMap = new HashMap<String, Integer>();
        }

        /**
         * TODO: Implement the toString according to the example output shown above.
         *
         *  @return formatted String representation of this class's instance
         */
        @Override
        public String toString() {
            String res = "";
            for (Map.Entry<String, Integer> entry : myMap.entrySet()){
                res += entry.getKey() + " scored:" + " " + entry.getValue() + "\n";
            }

            return "HashMap for course" + " " + this.course + String.valueOf(this.course_num) +":" + "\n" + res;
        }

        /**
         * TODO: Define a addStudentWithMark method that tries to add a student mark information to the HashMap,
         * and returns a boolean value to nidicate whether it was successfully added.
         *
         * @param studentName the student name to be added
         * @param mark the mark that student scored
         * @return true if the student information was recorded successfully. If the student
         *          already exist in the HashMap, then return false.
         */
        public boolean addStudentWithMark(String name,Integer mark){
            if(! myMap.containsKey(name)){
                myMap.put(name, mark);
                return true;}
            else{return false;}
            }


        /**
         * TODO: Define a hasStudent method that tells if the HashMap contains a specific student.
         * @param studentName the student name to check for
         * @return true if the student is in the HashMap otherwise false
         */
        public boolean hasStudent(String name){
            return myMap.containsKey(name);
        }

        /**
         * TODO: Define a hasMark method that return whether the course has a student who scored a given mark.
         * @param mark the mark to check for
         * @return true if the mark exists otherwise false
         */

        public boolean hasMark(Integer mark){
            return myMap.containsValue(mark);
        }
    }

