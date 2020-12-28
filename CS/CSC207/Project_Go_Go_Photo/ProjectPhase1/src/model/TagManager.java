package model;

import java.io.*;
import java.lang.System;
import java.util.*;

public class TagManager implements Observer,Serializable{
    // a HaspMap to store tags of system
    public HashMap<String, Integer> tags;

    // constructor
    public TagManager(){
            tags = new HashMap<>();
    }

////    @Override
//    public static void updateUp(String key){
//        if(! tags.containsKey(key)){
//            tags.put(key, 1);}
//        else{
//            Integer value = tags.get(key);
//            tags.put(key, tags.get(key)+1);
//        }
//    }
//
////    @Override
//    public static void updateDown(String key){
//        Integer value = tags.get(key);
//        if (value == 1){
//            tags.remove(key);
//        }else{tags.put(key, tags.get(key)-1);
//        }
//    }


    public void saveToTagManagerFile(String filePath) throws IOException {
        OutputStream file = new FileOutputStream(filePath);
        OutputStream buffer = new BufferedOutputStream(file);
        ObjectOutput output = new ObjectOutputStream(buffer);

        // serialize the tagManager
        output.writeObject(tags);
        output.close();
    }

    public ArrayList<Tag> getExistingTags(){
        Set<String > tagSet = tags.keySet();
        ArrayList<Tag> res = new ArrayList<>();
        for( String s : tagSet){
            res.add(new Tag(s));

        }
        return res;
    }

    @Override
    public void update(Observable o, Object arg) {
        String key = ((String[]) arg)[0];
        String upOrDown = ((String[]) arg)[1];
        if (upOrDown == "U"){
            if(! tags.containsKey(key)){
                tags.put(key, 1);
            }else{
                tags.put(key, tags.get(key)+1);}
        } else {
            Integer value = tags.get(key);
            if (value == 1){
                tags.remove(key);
            }else{
                tags.put(key, value-1);
            }
        }
    }
}



