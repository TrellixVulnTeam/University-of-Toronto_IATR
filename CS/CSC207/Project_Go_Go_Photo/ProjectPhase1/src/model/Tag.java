package model;

/**
 * This Tag class is used for serialize tags objects in order to display all the tag's name via GUI.
 */
public class Tag {
    private String name;

    /**
     * Tag's constructor that includes the name of the tag. This includes "@" as the prefix of
     * the name.
     *
     * @param name
     */
    public Tag(String name){
        this.name = "@" + name;
    }

    /**
     * Gets the name of the tag. This includes "@" as the prefix of the name.
     *
     * @return the name of the tag.
     */
    public String getName(){
        return this.name;
    }

    /**
     * Gets the naked name of the tag. This doesn't include "@" as the prefix of the name.
     * @return the naked name of the tag. This doesn't include "@" as the prefix of the name.
     */
    public String getOriginalName() {return this.name.substring(1);}
}
