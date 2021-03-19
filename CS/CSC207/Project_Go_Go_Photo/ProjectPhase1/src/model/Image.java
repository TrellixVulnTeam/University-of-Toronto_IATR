package model;

import java.io.Serializable;
import java.util.ArrayList;

/**
 * This class is used to track all the image changes.
 */
public class Image implements Serializable{
    private String name;
    private String path;
    private String type;
    private ArrayList<String> tags;
    private ArrayList<UsedName> renamingHistory;


    /**
     * Name is the image name without the suffix type. Type is the type of the image(as the suffix of of the type).
     * Path is the string of the image's path.
     *
     * @param name The name of the Image that doesn't include the suffix type.
     * @param type The type of the image that is shown after the last index of the "."
     * @param path The string representation of the image path
     */
    public Image(String name, String type, String path){
        this.name = name;
        this.type = type;
        this.tags = new ArrayList<>();
        this.path = path;
        this.renamingHistory = new ArrayList<>();
        this.renamingHistory.add(new UsedName(this.name+"."+this.type));
    }

    /**
     * This is type of the image. This is suffix of the Image's filename.
     *
     * @return The image type of the image. This is suffix of the name of the image.
     */
    //No setter for Type since it won't change once created
    public String getType(){
        return this.type;
    }

    /**
     * Gets the name of the image object. The returned name is the name without the suffix image type.
     * @return
     */
    public String getName() {
        return this.name;
    }

    /**
     * Sets the name of the image to newName.
     *
     * @param newName This is the new name of the image to be set for the image.
     */
    public void setName(String newName){
        this.name = newName;
    }

    /**
     * Gets an ArrayList of tags that the image has. There is no duplicate tag exists in the
     * arraylist of the image.
     *
     * @return an ArrayList of tags that the image has.
     */
    public ArrayList<Tag> getTagList() {
        ArrayList<Tag> tagContainer = new ArrayList<>();
        for (String tag : this.tags) {
            tagContainer.add(new Tag(tag));
        }
        return tagContainer;
    }

    /**
     * Gets an ArrayList of usednames. This is used for GUI to display all the names the image
     * has ever used.
     *
     * @return an ArrayList of usednames. This is used for GUI to display all the names the image
     * has ever used.
     */
    public ArrayList<UsedName> getRenamingHistory() {
        return renamingHistory;
    }

    /**
     * Adds the new name to the image's renaming history.
     *
     * @param newName the new name of the image that to be added to the ArrayList
     *                of the renaming history.
     */
    public void addNewNameToHistory(String newName){
        this.renamingHistory.add(new UsedName(newName+"."+this.type));
    }

    /**
     * Gets the string representation of the image's path.
     * @return The string representation of the image's path.
     */
    public String getPath(){
        return this.path;
    }

    /**
     * The new path of the image to be set.
     *
     * @param newPath Sets the image's path to be newPath.
     */
    public void setPath(String newPath){
        this.path = newPath;
    }

    /**
     * Gets an arrayList of string which contains of the tags that are represented in string format.
     *
     * @return an ArrayList of string which contains of the tags that are represented in string format.
     */
    public ArrayList<String> getTags() {
        return this.tags;
    }

    /**
     * Gets the full name of the image that includes the suffix of the image type.
     *
     * @return the complete name of the image that includes the suffix image type.
     */
    public String getFullName(){
        return this.name + "." + this.type;
    }

}
